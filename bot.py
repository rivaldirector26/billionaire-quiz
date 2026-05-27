import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://rivaldirector26.github.io/billionaire-quiz")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            "Пройти тест 🏆",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Узнай с какой вероятностью ты стал бы миллиардером\n\n"
        "8 реальных кризисов из жизни Безоса, Шульца, Уолтона и других. "
        "Ты встаёшь на их место и принимаешь решение — потом узнаёшь чем это закончилось.\n\n"
        "Нажми кнопку ниже 👇",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
