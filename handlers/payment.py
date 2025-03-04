from aiogram import Router, F
from aiogram.types import PreCheckoutQuery, Message
from database.crud import update_booking

router = Router()


@router.pre_checkout_query()
async def cmd_checkout_pay(query: PreCheckoutQuery):
    await query.answer(ok=True)


@router.message(F.successful_payment)
async def success_payment(message: Message):
    await message.answer('Оплата успешно прошла, вы зарезервировали ваш столик')
    status = 'Оплачено'
    update_booking(message.from_user.id, status)