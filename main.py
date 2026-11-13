import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with an inline button to the channel."""
    # Read channel URL from environment variable
    channel_url = os.environ.get("CHANNEL_URL")
    
    if not channel_url:
        logger.error("CHANNEL_URL environment variable is not set.")
        await update.message.reply_text("Configuration error. Please contact the admin.")
        return

    # Build the inline keyboard button
    keyboard = [
        [InlineKeyboardButton("Open Channel", url=channel_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Reply to the user
    await update.message.reply_text(
        text="Welcome to Sure Betting Tips ⚽ Tap below to open our Telegram channel.",
        reply_markup=reply_markup
    )

def main() -> None:
    """Start the bot with long polling."""
    # Read bot token from environment variable
    token = os.environ.get("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN environment variable is not set.")
        return

    # Create the Application
    application = Application.builder().token(token).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot with long polling (no webhook, no web server)
    logger.info("Starting Sure Betting Tips bot with long polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
