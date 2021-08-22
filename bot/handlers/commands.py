import telegram
import datetime
import re

from bot.utils import handler_logging
from bot.models import StaticText
from bot import keyboards


@handler_logging(action_name="/start")
def start(update, context):
    update.message.reply_text(text=StaticText.load_text("start"), reply_markup=keyboards.main_menu())
