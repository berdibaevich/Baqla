import re
from django.conf import settings
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest


def format_group_name(days: str, time: str) -> str:
    translations = {
        "ODD": "Taq kúnler",
        "EVEN": "Jup kúnler"
    }
    day_name = translations.get(days.upper(), days)
    return f"{day_name} | 🕒 {time}"



async def delete_old_messages(bot: Bot, chat_id: int, message_ids: list[int]):
    """
        Delete old messages from spesific user's chat by IDs.
    """
    for msg_id in message_ids:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except TelegramBadRequest as e:
            await bot.send_message(
                chat_id=settings.SUPERUSER_TELEGRAM_ID,
                text=f"Xabardi óshiriwde qátelik (ID: {msg_id}): \n\n{e}"
            )
        except Exception as e:
            await bot.send_message(
                chat_id=settings.SUPERUSER_TELEGRAM_ID,
                text=f"Kútilmegen qátelik: {e}"
            )



def is_valid_full_name(text: str) -> bool:
    if not re.match(r"^[A-Za-z\s'‘“áóǵńíúÁÓǴŃÍÚ]+$", text):
        return False

    words = text.strip().split()

    if len(words) < 2:
        return False
    
    for word in words:
        clean_word = word.replace("'", "")
        if len(clean_word) < 4:
            return False

    return True
