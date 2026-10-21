from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    text = (
        "<b>Assalawma aleykum!</b>\n\n"
        "Baqla botqa xosh keldińiz. ✨")
    
    await message.answer(text=text, parse_mode="HTML")