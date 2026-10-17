from django.conf import settings
from redis.asyncio import Redis


def get_async_redis_client(db: int):
    return Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        db=db,
        decode_responses=True
    )