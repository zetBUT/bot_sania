from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8719329023:AAH_86AJxxHRE-m7uuGtcwpQ-T-d5FKUmF4"

WEB_APP_URL = "https://zetbut.github.io/bot_sania/"


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    button = KeyboardButton(

        text="💰 Finance App",

        web_app=WebAppInfo(
            url=WEB_APP_URL
        )
    )

    keyboard = [[button]]

    reply_markup = ReplyKeyboardMarkup(

        keyboard,

        resize_keyboard=True
    )

    await update.message.reply_text(

        "📒 Фінансовий щоденник",

        reply_markup=reply_markup
    )


async def web_app_data(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = update.effective_message.web_app_data.data

    await update.message.reply_text(

        f"{data}"

    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(

    MessageHandler(
        filters.StatusUpdate.WEB_APP_DATA,
        web_app_data
    )

)

print("BOT STARTED")

app.run_polling()