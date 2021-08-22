from bot.models import StaticText


def generate_standard_texts():
    # start text
    StaticText.create("start", "Текст при старте бота", "Хаю хай")

    # main_menu buttons
    StaticText.create("rent button", "Текст на кнопке главного меню для брони", "Забронировать лодку")
    StaticText.create("location button", "Текст на кнопке главного меню как добраться", "Как добраться")
    StaticText.create("take button", "Текст на кнопке главного меню что взять с собой", "Что взять с собой")
    StaticText.create("safety button", "Текст на кнопке главного меню ТБ", "Техника безопасности")
    StaticText.create("back button", "Текст на кнопке назад", "Назад")

    # take text
    StaticText.create("take", "Текст в разделе что взять с собой", "Ну чет там возьмите хз")

    print("Standard texts inited")
