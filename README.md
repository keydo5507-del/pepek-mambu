# KEY MD Bot

Telegram group management bot based on Miss Rose / Marie, fully rebranded to **KEY MD**.

All original features and modules are preserved.

## Features
- Admin tools, bans, mutes, warns, locks
- Welcome messages, notes, filters, antiflood
- Global bans/mutes, reporting, RSS, and many more modules
- Fully modular

## Requirements
- Python 3.8+ (recommended; original targeted 3.6)
- PostgreSQL database
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Set the bot name to **KEY MD** in BotFather (this becomes `bot.first_name`)

## Environment Variables
| Variable | Required | Description |
|----------|----------|-------------|
| `ENV` | Yes | Set to any value to enable env mode |
| `TOKEN` | Yes | Bot token from BotFather |
| `OWNER_ID` | Yes | Your Telegram user ID |
| `OWNER_USERNAME` | Yes | Your username (without @) |
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `WEBHOOK` | For Vercel | Set to `ANYTHING` / `True` |
| `URL` | For webhook | Your deployment URL (e.g. `https://your-app.vercel.app/`) |
| `PORT` | Optional | Default 5000 / Vercel handles it |
| `SUDO_USERS` | Optional | Space-separated user IDs |
| `SUPPORT_USERS` | Optional | Space-separated user IDs |
| `WHITELIST_USERS` | Optional | Space-separated user IDs |
| `MESSAGE_DUMP` | Optional | Chat ID for saved messages |
| `DEL_CMDS` | Optional | `True` to delete unauthorized commands |
| `STRICT_GBAN` | Optional | `True` |
| `ALLOW_EXCL` | Optional | `True` to allow `!` commands |
| `BAN_STICKER` | Optional | File ID of ban sticker |

## Deploy on Vercel (Webhook mode)

> **Important**: Vercel is serverless. This bot originally uses long-running polling.  
> On Vercel we force **webhook** mode. Cold starts and 10s/60s timeouts can cause issues with heavy modules.  
> For best reliability prefer **Railway**, **Render**, or **Heroku**.

1. Fork / upload this repo to GitHub.
2. Import project in [Vercel](https://vercel.com).
3. Add all required environment variables (especially `TOKEN`, `OWNER_ID`, `DATABASE_URL`, `WEBHOOK=True`, `URL=https://your-project.vercel.app/`).
4. Deploy.
5. After deploy, set the webhook:
   ```
   https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-project.vercel.app/api
   ```
6. Make sure your bot name is set to **KEY MD** via BotFather.

### Vercel notes
- Uses `/api` as the webhook endpoint (see `api/index.py`).
- Database must be external (Neon, Supabase, Railway Postgres, etc.).
- Some long-running or heavy operations may hit Vercel limits.

## Alternative Deployments (Recommended)

### Railway / Render / Heroku
- Use the included `Procfile` (`web: python3 -m tg_bot`)
- Set the same env vars
- Enable webhook or use polling (set `WEBHOOK=False` for polling)

## Local Run
```bash
pip install -r requirements.txt
# Create tg_bot/config.py based on sample_config.py
python3 -m tg_bot
```

## Credits
- Original base: [PaulSonOfLars/tgbot](https://github.com/PaulSonOfLars/tgbot) (Marie)
- Miss Rose fork
- Rebranded to **KEY MD** – all functions kept intact

## License
See LICENSE file.
