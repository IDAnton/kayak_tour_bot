import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kayak_tour.settings')
django.setup()

from bot.handlers.dispatcher import run_pooling

if __name__ == "__main__":
    run_pooling()
