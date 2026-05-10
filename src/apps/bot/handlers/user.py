from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import Message

from ..keyboards import (
    get_student_reg_ik
)

from apps.students.services import has_active_groups_exists


user_private_router = Router()

@user_private_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()

    has_groups = await has_active_groups_exists()
    
    if has_groups:
        text = (
            "<b>Assalawma aleykum!</b>\n\n"
            "Baqla botqa xosh keldińiz. ✨"
        )
        await message.answer(text, reply_markup=get_student_reg_ik(), parse_mode="HTML")
    else:
        await message.answer("Hello.")
