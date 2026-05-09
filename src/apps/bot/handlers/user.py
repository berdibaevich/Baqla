from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from ..keyboards import (
    get_role_ik
)

from apps.students.services import has_active_groups_exists


user_private_router = Router()

@user_private_router.message(Command("start"))
async def cmd_start(message: Message):
    has_groups = await has_active_groups_exists()
    
    if has_groups:
        text = (
            "<b>Assalawma aleykum!</b>\n\n"
            "Baqla botqa xosh keldińiz. ✨"
            "\nTanlań:"
        )
        await message.answer(text, reply_markup=get_role_ik(), parse_mode="HTML")
    else:
        await message.answer("Hello.")
