from django.conf import settings
from aiogram import Bot, Dispatcher

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()