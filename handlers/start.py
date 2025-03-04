from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from text import START_MESSAGE

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE)