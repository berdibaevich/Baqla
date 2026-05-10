from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..callback import (
    UserAction,
    RoleCbData
)


def get_role_ik() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="Oqiwshi",
        callback_data=RoleCbData(action=UserAction.SELECT, role="student"),
        style="primary"
    )
    builder.button(
        text="Ata-ana",
        callback_data=RoleCbData(action=UserAction.SELECT, role="parent"),
        style="success"
    )
    builder.adjust(2)
    return builder.as_markup()
