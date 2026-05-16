from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

DELETE_REPLY_KEYBOARD = ReplyKeyboardRemove()


def share_phone_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="☎️ Jónetiw",
        request_contact=True
    )
    return builder.as_markup()