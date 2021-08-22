import json

from bot.handlers import main_menu
from bot.handlers import rent_menu
from bot.utils import handler_logging


def inline_buttons_handler(update, context):
    query = update.callback_query
    query.answer()
    data = json.loads(query.data)
    print('query content', str(data))
    main_menu.main_menu(query=query, context=context, data=data)
    rent_menu.rent_menu(query=query, context=context, data=data)
