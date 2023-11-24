# Claudeに渡すパラメータの設定をします。
# ご利用のアプリケーションに合わせて調整してください。
# 参考: https://docs.anthropic.com/claude/reference/complete_post
GENERATION_CONFIG = {
    "max_tokens_to_sample": 100000,
    "temperature": 0.8,
    "top_k": 500,
    "top_p": 0.99,
    "stop_sequences": ["Human: ", "Assistant: ", "System: "],
}
