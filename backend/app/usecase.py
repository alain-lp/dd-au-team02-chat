import json
import logging
from datetime import datetime
from app.context import get_context_setting_prompt, get_secondary_context_prompt
import app.context

from app.bedrock import _create_body, get_model_id, invoke
from app.repositories.conversation import (
    RecordNotFoundError,
    find_conversation_by_id,
    store_conversation,
)
from app.repositories.model import ContentModel, ConversationModel, MessageModel
from app.route_schema import ChatInput, ChatOutput, Content, MessageOutput
from app.utils import get_buffer_string
from ulid import ULID

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def prepare_conversation(
    user_id: str, chat_input: ChatInput
) -> tuple[str, ConversationModel]:
    try:
        # Fetch existing conversation
        conversation = find_conversation_by_id(user_id, chat_input.conversation_id)
        logger.debug(f"Found conversation: {conversation}")
        parent_id = chat_input.message.parent_message_id
    except RecordNotFoundError:
        logger.debug(
            f"No conversation found with id: {chat_input.conversation_id}. Creating new conversation."
        )
        # Create new conversation
        conversation = ConversationModel(
            id=chat_input.conversation_id,
            title="New conversation",
            create_time=datetime.now().timestamp(),
            message_map={
                # Dummy system message
                "system": MessageModel(
                    role="system",
                    content=ContentModel(
                        content_type="text",
                        body=get_context_setting_prompt(),
                    ),
                    model=chat_input.message.model,
                    children=[],
                    parent=None,
                    create_time=datetime.now().timestamp(),
                )
            },
            last_message_id="",
        )
        parent_id = "system"

    user_input = chat_input.message.content.body

    # List contexts
    if user_input == app.context.LIST_CONTEXT_COMMAND:
       logger.info("USER QUERY FOR MODES")
       query_id, query_message = create_context_message(user_input, chat_input, parent_id, True) 
       append_msg_to_conversation(conversation, query_message, query_id, parent_id)

       available = app.context.get_available_secondary_contexts()
       response_text = f"Available modes are: {available}"
       message_id, message = create_context_message(response_text, chat_input, query_id, False) 
       append_msg_to_conversation(conversation, message, message_id, query_id)



    # Select a new context
    elif user_input.startswith(app.context.SWAP_CONTEXT_COMMAND):
        selected_mode = user_input.split()[-1]
        logger.info(f"USER SETS MODE TO '{selected_mode}'")
        select_id, select_message = create_context_message(user_input, chat_input, parent_id, True) 
        append_msg_to_conversation(conversation, select_message, select_id, parent_id)
        
        message_id, message = create_secondary_context_message(selected_mode, chat_input, select_id)
        append_msg_to_conversation(conversation, message, message_id, parent_id)


    # Append user chat input to the conversation
    else:
        message_id, message = append_user_input(chat_input, conversation, parent_id)
        append_msg_to_conversation(conversation, message, message_id, parent_id)

    return (message_id, conversation)


def get_invoke_payload(conversation: ConversationModel, chat_input: ChatInput):
    messages = trace_to_root(
        node_id=chat_input.message.parent_message_id,
        message_map=conversation.message_map,
    )
    messages.append(chat_input.message)
    prompt = get_buffer_string(messages)
    body = _create_body(chat_input.message.model, prompt)
    model_id = get_model_id(chat_input.message.model)
    accept = "application/json"
    content_type = "application/json"
    return {
        "body": body,
        "model_id": model_id,
        "accept": accept,
        "content_type": content_type,
    }


def trace_to_root(
    node_id: str, message_map: dict[str, MessageModel]
) -> list[MessageModel]:
    """Trace message map from node to root."""
    result = []

    current_node = message_map.get(node_id)
    while current_node:
        result.append(current_node)
        parent_id = current_node.parent
        if parent_id is None:
            break
        current_node = message_map.get(parent_id)

    return result[::-1]


def chat(user_id: str, chat_input: ChatInput) -> ChatOutput:
    user_msg_id, conversation = prepare_conversation(user_id, chat_input)

    messages = trace_to_root(
        node_id=chat_input.message.parent_message_id,
        message_map=conversation.message_map,
    )
    messages.append(chat_input.message)

    # Invoke Bedrock if needed
    if conversation.message_map[conversation.last_message_id].role.startswith('user'):
        prompt = get_buffer_string(messages)
        reply_txt = invoke(prompt=prompt, model=chat_input.message.model)

        # Issue id for new assistant message
        assistant_msg_id = str(ULID())
        # Append bedrock output to the existing conversation
        message = MessageModel(
            role="assistant",
            content=ContentModel(content_type="text", body=reply_txt),
            model=chat_input.message.model,
            children=[],
            parent=user_msg_id,
            create_time=datetime.now().timestamp(),
        )
        conversation.message_map[assistant_msg_id] = message

        # Append children to parent
        append_msg_to_conversation(conversation, message, assistant_msg_id)
    else:
        message = conversation.message_map[conversation.last_message_id]

    # Store updated conversation
    store_conversation(user_id, conversation)        

    output = ChatOutput(
        conversation_id=conversation.id,
        create_time=conversation.create_time,
        message=MessageOutput(
            role=message.role,
            content=Content(
                content_type=message.content.content_type,
                body=message.content.body,
            ),
            model=message.model,
            children=message.children,
            parent=message.parent,
        ),
    )

    return output


def propose_conversation_title(
    user_id: str, conversation_id: str, model="claude-instant-v1"
) -> str:
    PROMPT = """Reading the conversation above, what is the appropriate title for the conversation? When answering the title, please follow the rules below:
<rules>
- Title must be in the same language as the conversation.
- Title length must be from 15 to 20 characters.
- Prefer more specific title than general. Your title should always be distinct from others.
- Return the conversation title only. DO NOT include any strings other than the title.
</rules>
"""

    # Fetch existing conversation
    conversation = find_conversation_by_id(user_id, conversation_id)
    messages = trace_to_root(
        node_id=conversation.last_message_id,
        message_map=conversation.message_map,
    )

    # Append message to generate title
    new_message = MessageModel(
        role="user",
        content=ContentModel(
            content_type="text",
            body=PROMPT,
        ),
        model=model,
        children=[],
        parent=conversation.last_message_id,
        create_time=datetime.now().timestamp(),
    )
    messages.append(new_message)

    # Invoke Bedrock
    prompt = get_buffer_string(messages)
    reply_txt = invoke(prompt=prompt, model=model)
    reply_txt = reply_txt.replace("\n", "")
    return reply_txt

def create_secondary_context_message(type, chat_input, parent_id):
    message_id = str(ULID())
    new_message = MessageModel(
        role="system",
        content=ContentModel(
            content_type=chat_input.message.content.content_type,
            body=get_secondary_context_prompt(type),
        ),
        model=chat_input.message.model,
        children=[],
        parent=parent_id,
        create_time=datetime.now().timestamp(),
    )
    return (message_id, new_message)

def create_context_message(body, chat_input, parent_id, human = False):
    if human:
        role = 'ctx-user'
    else:
        role = 'ctx'    
    
    message_id = str(ULID())
    new_message = MessageModel(
        role=role,
        content=ContentModel(
            content_type=chat_input.message.content.content_type,
            body=body,
        ),
        model=chat_input.message.model,
        children=[],
        parent=parent_id,
        create_time=datetime.now().timestamp(),
    )
    return (message_id, new_message)

def append_msg_to_conversation(conversation, msg, msg_id, parent_id = None):
    conversation.message_map[msg_id] = msg
   
    if parent_id is None:
        parent_id = conversation.last_message_id

    if conversation.message_map.get(parent_id) is not None:
        conversation.message_map[parent_id].children.append(msg_id)

    conversation.last_message_id = msg_id   

def append_user_input(chat_input, conversation, parent_id):
    message_id = str(ULID())
    new_message = MessageModel(
        role=chat_input.message.role,
        content=ContentModel(
            content_type=chat_input.message.content.content_type,
            body=chat_input.message.content.body,
        ),
        model=chat_input.message.model,
        children=[],
        parent=parent_id,
        create_time=datetime.now().timestamp(),
    )
    return (message_id, new_message)
    
