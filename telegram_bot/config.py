import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN: str = os.environ["TELEGRAM_BOT_TOKEN"]
GROQ_API_KEY: str = os.environ["GROQ_API_KEY"]

# Optional: comma-separated list of Telegram chat IDs allowed to use the bot
# Leave empty to allow everyone
ALLOWED_CHAT_IDS: list[int] = [
    int(x) for x in os.getenv("ALLOWED_CHAT_IDS", "").split(",") if x.strip()
]

MODEL = "llama-3.3-70b-versatile"
MAX_TOKENS = 1024
