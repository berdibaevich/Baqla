from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..callback import (
    UserAction,
    RoleCbData,
    GroupCbData,
    ProfileCbData
)

from ..utils import format_group_name


def get_student_reg_ik() -> InlineKeyboardMarkup:
    """Student Registration Inline Keyboard"""
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="Oqiwshi bolip dizimnen ótiw",
        callback_data=RoleCbData(action=UserAction.SELECT, role="student"),
        style="success"
    )
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



def confirm_profile_ik() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="✅ Jiberiw",
        callback_data=ProfileCbData(action=UserAction.CONFIRM),
    )
    builder.button(
        text="🔄 Qayta toltiriw",
        callback_data=ProfileCbData(action=UserAction.REFILL),
    )

    builder.adjust(2)
    return builder.as_markup()
