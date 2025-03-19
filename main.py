from aiogram import Bot, Dispatcher
from config import TOKEN
import logging
import asyncio
from handlers import router
from database.models import make_table_users


async def main():
    logging.basicConfig(level=logging.INFO)
    make_table_users()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())