from enum import Enum
from aiogram.filters.callback_data import CallbackData


class UserAction(Enum):
    SELECT = "select"
    CONFIRM = "confirm"
    REFILL = "refill"



class RoleCbData(CallbackData, prefix="role"):
    action: UserAction
    role: str


class GroupCbData(CallbackData, prefix="group"):
    action: UserAction
    id: int


class ProfileCbData(CallbackData, prefix="profile"):
    action: UserAction