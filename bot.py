import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz

openai.api_key = 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
BOT_TOKEN = 8232914386: AAG7B09Z4YE8ku8-
GWQAa7spw5lJjOSvUgY

logging.basicConfig(level=logging.INFO)

def get_candle_time():
    now = datetime.now(pytz.timezone("UTC"))
    return now.strftime("This signal is for %H:%M UTC candle.")

async def get_signal():
    prompt = "Give a high-quality binary trading signal (only UP or DOWN) for EURUSD 1-minute candle. Don't explain."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip().upper()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot started! Type /signal to get latest EURUSD 1-min signal.")

async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signal = await get_signal()
    candle_time = get_candle_time()
    await update.message.reply_text(f"📉 EURUSD Signal: {signal}\n🕐 {candle_time}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", send_signal))
    app.run_polling()

if __name__ == "__main__":
    main()
