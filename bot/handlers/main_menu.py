from bot.models import StaticText
from bot import keyboards
from telegram.error import BadRequest


def main_menu(query, context, data):
    if data["type"] != "main_menu":
        return

    if data["content"] == "rent":
        query.edit_message_text(text=StaticText.load_text("rent"), reply_markup=keyboards.rent_type_keyboard())
        return

    if data["content"] == "safety":
        query.edit_message_text(text=StaticText.load_text("safety"), reply_markup=keyboards.back_to_main())
        return

    if data["content"] == "take":
        query.edit_message_text(text=StaticText.load_text("take"), reply_markup=keyboards.back_to_main())
        return

    if data["content"] == "location":
        query.delete_message()
        query.message.reply_venue(title="Прокат каяков", address='Бердск, пляж "Дюны"', latitude=54.78185318062615, longitude=83.05472909804102, google_place_id='ChIJATy5nPLF30IRMJ9tsB2W3Lo', reply_markup=keyboards.back_to_main())
        return

    if data["content"] == "back":
        try:
            query.edit_message_text(text=StaticText.load_text("start"), reply_markup=keyboards.main_menu())
        except BadRequest:
            query.delete_message()
            query.message.reply_text(text=StaticText.load_text("start"), reply_markup=keyboards.main_menu())
        return
