from django.conf import settings
from aiogram import Bot, Dispatcher

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


def setup_routers(dp: Dispatcher):
    from .handlers import user_private_router, student_private_router
    dp.include_routers(
        user_private_router,
        student_private_router
    )