from enum import Enum
from aiogram.filters.callback_data import CallbackData


class UserAction(Enum):
    role_student = "role_student"
    role_parent = "role_parent"


class UserCbData(CallbackData, prefix = "user"):
    action: UserAction
