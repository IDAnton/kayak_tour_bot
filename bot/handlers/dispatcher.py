import telegram
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    InlineQueryHandler, CallbackQueryHandler,
    ChosenInlineResultHandler,
)
import os
from bot.handlers import commands
from bot.handlers.buttons import inline_buttons_handler


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CallbackQueryHandler(inline_buttons_handler))
    return dp


def run_pooling():
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    updater.start_polling()
    updater.idle()
