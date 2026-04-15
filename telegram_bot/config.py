import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN: str = os.environ["TELEGRAM_BOT_TOKEN"]
GEMINI_API_KEY: str = os.environ["GEMINI_API_KEY"]

# Optional: comma-separated list of Telegram chat IDs allowed to use the bot
# Leave empty to allow everyone
ALLOWED_CHAT_IDS: list[int] = [
    int(x) for x in os.getenv("ALLOWED_CHAT_IDS", "").split(",") if x.strip()
]

MODEL = "gemini-2.0-flash"
MAX_TOKENS = 1024
