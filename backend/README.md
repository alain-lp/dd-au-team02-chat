# Backend API

Written in Python with [FastAPI](https://fastapi.tiangolo.com/).

- To get started, we need to deploy resources to create DynamoDB / Bedrock resource. To deploy, please see [Deploy using CDK](../README.md#deploy-using-cdk).
- Create virtual environment on your local machine

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
```

- Configure environment variables

```
export TABLE_NAME=BedrockChatStack-DatabaseConversationTable03F3FD7A-RMCEHJG7OV56
export ACCOUNT=916537346432
export REGION=us-east-1
export BEDROCK_REGION=us-east-1
```

- Run unit test

```
python tests/test_conversation.py TestConversationRepository
python tests/test_bedrock.py
python tests/test_usecase.py
```
