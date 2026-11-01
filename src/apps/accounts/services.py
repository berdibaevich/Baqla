from django.utils import timezone

# from .models import TelegramGroup



def get_or_create_user(tg_user: dict) -> tuple:
    from src.apps.accounts.models import UserBase

    tg_id = tg_user["telegram_id"]

    user, is_new = UserBase.objects.get_or_create(
        telegram_id = tg_id,
        defaults={
            "full_name": tg_user["full_name"],
            "last_login": timezone.now()
        }
    )

    return user, is_new





# async def has_active_groups_exists() -> bool:
#     exists = await TelegramGroup.objects.filter(is_active_group=False).aexists()
#     return exists


# async def get_groups():
#     return [group async for group in TelegramGroup.objects.filter(is_active_group=False, is_full=False).values("id", "days", "time")]