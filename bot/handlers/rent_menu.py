from bot.models import StaticText, RentObject
from bot import keyboards
from telegram.error import BadRequest


def rent_menu(query, context, data):
    if data["type"] == "rent_type":

        rent_types = [rent_type[0] for rent_type in RentObject._meta.get_field('rent_type').choices]
        if data["content"] in rent_types:
            query.edit_message_text(text=StaticText.load_text("rent_type"), reply_markup=keyboards.rent_object_keyboard(data["content"]))
            return

        # if data["content"] == 'back':
        #     query.edit_message_text(text=StaticText.load_text("rent"), reply_markup=keyboards.rent_type_keyboard())
        #     return

    elif data["type"] == 'rent_choice':
        if data["content"] == 'back':
            query.edit_message_text(text=StaticText.load_text("rent"), reply_markup=keyboards.rent_type_keyboard())
            return
        rent_obj = RentObject.get_by_id(obj_id=data["content"])
        text = f'{rent_obj.name}\n\n{rent_obj.description}'
        query.edit_message_text(text=text, reply_markup=keyboards.back_to_rent_choice(rent_obj.rent_type))
