from django.conf import settings
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from utils.aredis_service import get_async_redis_client


storage = RedisStorage(redis=get_async_redis_client(6))


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(storage=storage)


def setup_routers(dp: Dispatcher):
    from .handlers import user_private_router, student_private_router
    dp.include_routers(
        user_private_router,
        student_private_router
    )