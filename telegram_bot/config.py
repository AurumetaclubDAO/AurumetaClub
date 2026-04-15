import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN: str = os.environ["TELEGRAM_BOT_TOKEN"]
ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]

# Optional: comma-separated list of Telegram chat IDs allowed to use the bot
# Leave empty to allow everyone
ALLOWED_CHAT_IDS: list[int] = [
    int(x) for x in os.getenv("ALLOWED_CHAT_IDS", "").split(",") if x.strip()
]

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 1024
