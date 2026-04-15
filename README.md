# AurumetaClub

A multi-agent AI company for quantitative finance and DeFi, built as a DAO.

## Agents

| Agent | Role |
|---|---|
| **Commander** | Strategic coordination and governance decisions |
| **Researcher** | Market analysis and on-chain research |
| **Marketer** | Community growth and content creation |
| **DevOps** | Infrastructure, smart contracts, and security |

## Telegram Bot

The Telegram bot is the primary interface for interacting with the agent team.

### Setup

1. **Create a Telegram bot** via [@BotFather](https://t.me/BotFather) and copy the token.

2. **Clone and configure**
   ```bash
   git clone <repo>
   cd AurumetaClub
   cp .env.example .env
   # Edit .env and fill in TELEGRAM_BOT_TOKEN and ANTHROPIC_API_KEY
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the bot**
   ```bash
   python -m telegram_bot.bot
   ```

### Commands

| Command | Agent | Description |
|---|---|---|
| `/start` or `/help` | — | Show welcome message |
| `/commander <message>` | Commander | Strategic coordination |
| `/research <query>` | Researcher | Market & on-chain research |
| `/market <topic>` | Marketer | Community & marketing copy |
| `/devops <question>` | DevOps | Infrastructure & smart contracts |
| _(plain text)_ | Commander | Default route |

### Access Control

Set `ALLOWED_CHAT_IDS` in `.env` to a comma-separated list of Telegram chat IDs
to restrict access. Leave empty to allow everyone.
