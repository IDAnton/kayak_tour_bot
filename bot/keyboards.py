from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.models import StaticText, RentObject

import json


def pack(content, type):
    return json.dumps({'content': content, 'type': type})


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(StaticText.load_text("rent button"), callback_data=pack("rent", "main_menu"))],
        [InlineKeyboardButton(StaticText.load_text("location button"), callback_data=pack("location", "main_menu"))],
        [InlineKeyboardButton(StaticText.load_text("take button"), callback_data=pack("take", "main_menu"))],
        [InlineKeyboardButton(StaticText.load_text("safety button"), callback_data=pack("safety", "main_menu"))]
    ])


def back_to_main():
    return InlineKeyboardMarkup([[InlineKeyboardButton(StaticText.load_text("back button"), callback_data=pack("back", "main_menu"))]])


def rent_type_keyboard():
    rent_types = RentObject._meta.get_field('rent_type').choices
    buttons = [[InlineKeyboardButton(rent_type[1], callback_data=pack(rent_type[0], "rent_type"))] for rent_type in rent_types]
    buttons.append([InlineKeyboardButton(StaticText.load_text("back button"), callback_data=pack("back", "main_menu"))])
    return InlineKeyboardMarkup(buttons)


def rent_object_keyboard(rent_type):
    rent_objects = RentObject.get_all_type_available(rent_type=rent_type)
    buttons = [[InlineKeyboardButton(rent_obj.name, callback_data=pack(rent_obj.id, "rent_choice"))] for rent_obj in
               rent_objects]
    buttons.append([InlineKeyboardButton(StaticText.load_text("back button"), callback_data=pack("back", "rent_choice"))])
    return InlineKeyboardMarkup(buttons)


def back_to_rent_choice(rent_type):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(StaticText.load_text("back button"), callback_data=pack(rent_type, "rent_type"))]])

