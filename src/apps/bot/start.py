from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    text = (
        "<b>Assalawma aleykum!</b>\n\n"
        "Tómendegi <b>Baqla</b> túymesi arqali kiriwińiz múmkin.")
    
    await message.answer(text=text, parse_mode="HTML")