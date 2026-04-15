"""
AurumetaClub Telegram Bot

Entry point. Routes user messages to the appropriate agent:
  • /commander  (default) — strategic coordination
  • /research             — market & on-chain research
  • /market               — community & marketing copy
  • /devops               — infrastructure & smart contracts
"""

import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from telegram_bot import config
from telegram_bot.agents import commander, researcher, marketer, devops

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Access control
# ---------------------------------------------------------------------------

def _is_allowed(update: Update) -> bool:
    if not config.ALLOWED_CHAT_IDS:
        return True
    return update.effective_chat.id in config.ALLOWED_CHAT_IDS


async def _deny(update: Update) -> None:
    await update.message.reply_text("Sorry, you are not authorised to use this bot.")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def _reply_with_agent(update: Update, agent_module, text: str) -> None:
    if not text.strip():
        await update.message.reply_text("Please include a message, e.g. /research ETH L2 outlook")
        return
    await update.message.reply_text("Thinking...")
    try:
        answer = agent_module.respond(text.strip())
    except Exception as exc:
        logger.exception("Agent error: %s", exc)
        await update.message.reply_text(f"Agent error: {exc}")
        return
    await update.message.reply_text(answer)


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    await update.message.reply_text(
        "Welcome to *AurumetaClub* \u2014 your DAO AI team.\n\n"
        "Available commands:\n"
        "  /commander \u2039message\u203a \u2014 strategic coordination\n"
        "  /research \u2039query\u203a     \u2014 market & on-chain research\n"
        "  /market \u2039topic\u203a       \u2014 community & marketing copy\n"
        "  /devops \u2039question\u203a    \u2014 infrastructure & smart contracts\n\n"
        "Or just send a plain message to talk to the Commander.",
        parse_mode="Markdown",
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await cmd_start(update, context)


async def cmd_commander(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    text = " ".join(context.args) if context.args else ""
    await _reply_with_agent(update, commander, text)


async def cmd_research(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    text = " ".join(context.args) if context.args else ""
    await _reply_with_agent(update, researcher, text)


async def cmd_market(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    text = " ".join(context.args) if context.args else ""
    await _reply_with_agent(update, marketer, text)


async def cmd_devops(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    text = " ".join(context.args) if context.args else ""
    await _reply_with_agent(update, devops, text)


# ---------------------------------------------------------------------------
# Plain-message handler → Commander by default
# ---------------------------------------------------------------------------

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not _is_allowed(update):
        await _deny(update)
        return
    text = update.message.text or ""
    await _reply_with_agent(update, commander, text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    app = (
        Application.builder()
        .token(config.TELEGRAM_BOT_TOKEN)
        .build()
    )

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("commander", cmd_commander))
    app.add_handler(CommandHandler("research", cmd_research))
    app.add_handler(CommandHandler("market", cmd_market))
    app.add_handler(CommandHandler("devops", cmd_devops))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("AurumetaClub bot starting (polling)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
