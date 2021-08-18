import telegram
import datetime
import re

from bot.utils import handler_logging
from bot.models import StaticText


@handler_logging(action_name="/start")
def start(update, context):
    update.message.reply_text(text=StaticText.load_text("start"))
