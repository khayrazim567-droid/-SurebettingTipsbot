import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Set this to the local filename of the image you want to send (e.g., 'banner.jpg')
# Make sure to upload the image to your project folder on Railway/GitHub.
IMAGE_PATH = os.environ.get("IMAGE_PATH", "banner.jpg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the promotional message with the image, text, and link (no button)."""
    
    channel_url = os.environ.get("CHANNEL_URL", "https://t.me/+HP-G74C1gRIxNGI0")

    # The text with your channel link
    caption = (
        "I WON’T POST AGAIN !!!!!\n\n"
        "I want to bless all active. Member today so you if you are active you are Lucky 🏆\n"
        "I will be dropping sure banker games Here.they ticket is 100% assure join here👇 👇 \n\n"
        f"{channel_url}\n"
        f"{channel_url}\n"
        "♐️👆🏻👆🏻\n"
        "Winning is sure and 💯 guarantee I want to break a record too request to join and participate"
    )

    try:
        # Send photo with caption (No reply_markup / No buttons)
        await update.message.reply_photo(
            photo=IMAGE_PATH,
            caption=caption,
        )
    except Exception as e:
        logger.warning(f"Could not send photo ({e}). Falling back to text message.")
        # Fallback: send text only if the image fails to load
        await update.message.reply_text(
            text=caption,
            disable_web_page_preview=False,
        )

def main() -> None:
    """Start the bot with long polling."""
    token = os.environ.get("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN environment variable is not set.")
        return

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("Starting Sure Betting Tips bot with long polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
