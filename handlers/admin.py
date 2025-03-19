import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.crud import get_users

router = Router()


@router.message(Command('admin'))
async def cmd_admin(message: Message):
    users = get_users()
    await message.answer('\n'.join(str(user) for user in users))


