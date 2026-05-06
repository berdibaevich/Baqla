from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


user_private_router = Router()

@user_private_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello Bro.")
