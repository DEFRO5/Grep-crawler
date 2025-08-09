# Grep-crawler

A Python bot that monitors a webpage for specific keywords and sends Telegram alerts when found. Runs automatically via GitHub Actions at your scheduled time.

## Features

- Monitors any webpage for target keywords
- Sends professional Telegram notifications
- Automated scheduling via GitHub Actions
- No logging or file dependencies

## Quick Setup

### 1. Get Telegram Bot Token

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Save the bot token

### 2. Get Chat ID

1. Send any message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Find your `chat_id` in the response

### 3. Repository Setup

1. Fork/clone this repository
2. Go to **Settings → Secrets and variables → Actions**
3. Create repository secrets
4. Add these secrets:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Your bot token | `1234567890:ABC...` |
| `TELEGRAM_CHAT_ID` | Your chat ID | `123456789` |
| `MONITOR_URL` | URL to monitor | `https://example.com` |
| `SEARCH_WORD` | Target keyword | `james` |

### 4. Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Enable workflows if prompted
3. The bot will run automatically at your scheduled time.

## Manual Testing

Run locally with a `.env` file:

```bash
# Install dependencies
pip install requests python-dotenv
pip install requests

# Create .env file
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
MONITOR_URL=https://example.com
SEARCH_WORD=python

# Run once
python grep-crawler.py
```

## How it Works

- **Schedule**: Runs at your scheduled time via GitHub Actions
- **Detection**: Performs case-insensitive keyword matching
- **Alerts**: Sends Telegram message only when keyword is found
- **No Spam**: Each run is independent (no state tracking)

## Manual Trigger

You can manually trigger the bot from the **Actions** tab → **URL Monitor Bot** → **Run workflow**.

## Customization

Edit `.github/workflows/monitor.yml` to change the schedule:

```yaml
schedule:
  # Every 30 minutes
  - cron: '*/30 * * * *'
  
  # Every 6 hours
  - cron: '0 */6 * * *'
  
  # Daily at 9 AM
  - cron: '0 9 * * *'
```

## Troubleshooting

- **No alerts**: Check if the keyword exists on the webpage
- **Bot not responding**: Verify your bot token and chat ID
- **Action failing**: Check the Actions tab for error details
- **Wrong chat ID**: Make sure you messaged the bot first

---

**Note**: GitHub Actions have usage limits on free accounts. This setup uses minimal resources and should work within free tier limits.
