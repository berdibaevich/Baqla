from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..callback import (
    UserAction,
    RoleCbData,
    GroupCbData
)

from utils import format_group_name


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



def get_select_groups_ik(list_groups: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for group in list_groups:
        text = format_group_name(group['days'], group['time'])

        builder.button(
            text=text,
            callback_data=GroupCbData(action=UserAction.SELECT, id=group['id'])
        )

    builder.adjust(1)
    return builder.as_markup()

