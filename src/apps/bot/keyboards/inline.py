from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..callback import (
    UserCbData,
    UserAction
)


def get_role_ik() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="🧑🏼‍💻 Oqiwshi",
        callback_data=UserCbData(action=UserAction.role_student),
        style="primary"
    )
    builder.button(
        text="Ata-ana",
        callback_data=UserCbData(action=UserAction.role_parent),
        style="success"
    )
    builder.adjust(2)
    return builder.as_markup()
