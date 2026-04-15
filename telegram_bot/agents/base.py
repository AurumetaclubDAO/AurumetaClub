import groq
from telegram_bot import config


_client: groq.Groq | None = None


def _get_client() -> groq.Groq:
    global _client
    if _client is None:
        _client = groq.Groq(api_key=config.GROQ_API_KEY)
    return _client


def ask(system_prompt: str, user_message: str) -> str:
    client = _get_client()
    response = client.chat.completions.create(
        model=config.MODEL,
        max_tokens=config.MAX_TOKENS,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content
