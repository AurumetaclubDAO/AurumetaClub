import google.generativeai as genai
from telegram_bot import config

genai.configure(api_key=config.GEMINI_API_KEY)

_model: genai.GenerativeModel | None = None


def _get_model() -> genai.GenerativeModel:
    global _model
    if _model is None:
        _model = genai.GenerativeModel(config.MODEL)
    return _model


def ask(system_prompt: str, user_message: str) -> str:
    model = _get_model()
    response = model.generate_content(
        f"{system_prompt}\n\nUser: {user_message}",
        generation_config=genai.GenerationConfig(max_output_tokens=config.MAX_TOKENS),
    )
    return response.text
