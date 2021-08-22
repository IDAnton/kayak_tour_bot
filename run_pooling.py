import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kayak_tour.settings')
django.setup()

from bot.handlers.dispatcher import run_pooling
from bot.db_init import standart_gen


if __name__ == "__main__":
    standart_gen.generate_standard_texts()
    run_pooling()

