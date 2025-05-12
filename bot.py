import json
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

class PersianBot:
    def __init__(self):
        with open('data/phrases.json') as f:
            self.phrases = json.load(f)
        
        with open('data/events.json') as f:
            self.events = json.load(f)

    async def send_morning_message(self, context: ContextTypes.DEFAULT_TYPE):
        phrase = random.choice(self.phrases["morning"])
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text=phrase
        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "ربات فعال شد!\n"
            "هر صبح یک پیام تصادفی دریافت خواهید کرد."
        )
        context.job_queue.run_daily(
            self.send_morning_message,
            time=datetime.time(hour=8),
            chat_id=update.effective_chat.id
        )

def main():
    bot = PersianBot()
    app = Application.builder().token("TOKEN").build()
    app.add_handler(CommandHandler("start", bot.start))
    app.run_polling()

if __name__ == "__main__":
    main()
