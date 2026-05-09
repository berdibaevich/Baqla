from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery

from ..callback import (
    UserAction,
    UserCbData
)


student_private_router = Router()


@student_private_router.callback_query(
    UserCbData.filter(F.action == UserAction.role_student)
)
async def handle_student_group(query: CallbackQuery, callback_data: UserCbData):
    await query.message.answer("Hello Student")
    await query.answer()
