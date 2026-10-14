from .models import TelegramGroup


async def has_active_groups_exists() -> bool:
    exists = await TelegramGroup.objects.filter(is_active_group=False).aexists()
    return exists


async def get_groups():
    return [group async for group in TelegramGroup.objects.filter(is_active_group=False, is_full=False).values("id", "days", "time")]