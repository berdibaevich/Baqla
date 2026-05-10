from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery

from ..callback import (
    RoleCbData
)


student_private_router = Router()


@student_private_router.callback_query(
    RoleCbData.filter(F.role == "student")
)
async def show_groups(query: CallbackQuery, callback_data: RoleCbData, state: FSMContext):
    await query.message.answer("Hello Student")
    await query.answer()
