import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.crud import get_user_by_id, insert_to_table_users

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    user = get_user_by_id(message.from_user.id)
    if user:
        await message.answer('Привет друг')
    else:
        await message.answer('Привет я тебя запомнил)')
        insert_to_table_users(message.from_user.id, datetime.datetime.now())
