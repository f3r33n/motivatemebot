import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

print("Everything is loading correctly...")

# Load environment variables
load_dotenv()

# Load Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print("Token loaded successfully:", bool(TELEGRAM_BOT_TOKEN))

# Some motivational quotes
QUOTES = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
]

class MotivationalBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        # Register command handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("motivate", self.send_quotes))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("👋 Hi! I am the *Motivate Me Bot*. Send /motivate to receive a motivational quote!", parse_mode="Markdown")

    async def send_quotes(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        quote = random.choice(QUOTES)
        await update.message.reply_text(f"💡 {quote}")

    def run(self):
        print("🚀 Bot is running...")
        self.application.run_polling()

# Start the bot
if __name__ == "__main__":
    bot = MotivationalBot(TELEGRAM_BOT_TOKEN)
    bot.run()
