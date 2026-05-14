from enum import Enum
from aiogram.filters.callback_data import CallbackData


class UserAction(Enum):
    SELECT = "select"


class RoleCbData(CallbackData, prefix="role"):
    action: UserAction
    role: str


class GroupCbData(CallbackData, prefix="group"):
    action: UserAction
    id: int