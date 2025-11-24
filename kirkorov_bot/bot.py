import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Load environment variables from .env file
load_dotenv()

# Set up your bot token here. Replace 'YOUR_BOT_TOKEN' with your actual bot token.
# You can get a bot token from BotFather on Telegram.
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    await update.message.reply_text("Привет! Я Киркоров бот.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming messages and responds based on keywords."""
    text = update.message.text.lower()
    words = text.split()

    for word in words:
        if word == "да":
            await update.message.reply_text("Пизда")
            return # Отвечаем только один раз на первое совпадение
        elif word == "нет":
            await update.message.reply_text("Пидора ответ")
            return
        elif word == "триста" or word == "300":
            await update.message.reply_text("Отсоси у тракториста")
            return

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    aplikasi = Application.builder().token(BOT_TOKEN).build()

    # On different commands - answer in Telegram
    aplikasi.add_handler(CommandHandler("start", start))

    # On non command i.e message - echo the message on Telegram
    aplikasi.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    aplikasi.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

