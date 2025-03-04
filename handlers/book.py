from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import PRICE
from states.state import Booking
from database.crud import insert_to_booking

router = Router()


@router.message(Command('book'))
async def cmd_book(message: Message, state: FSMContext):
    await message.answer('Привет начинается процесс бронирования столика, введите дату: ')
    await state.set_state(Booking.date_booking)


@router.message(Booking.date_booking)
async def cmd_booking_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer('Отлично теперь введите время бронирования')
    await state.set_state(Booking.time_booking)


@router.message(Booking.time_booking)
async def cmd_booking_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer('Отлично теперь введите кол-во гостей')
    await state.set_state(Booking.guests_booking)


@router.message(Booking.guests_booking)
async def cmd_booking_guests(message: Message, state: FSMContext):
    await state.update_data(guests=message.text)
    await message.answer('Отлично теперь введите ваши предпочтения')
    await state.set_state(Booking.requirements_booking)


@router.message(Booking.requirements_booking)
async def cmd_booking_requirements(message: Message, state: FSMContext):
    await state.update_data(requirements=message.text)
    await message.answer('Отлично осталось оплатить депозит 100 руб')
    data = await state.get_data()
    date_time = data['date'] + ' ' + data['time']
    guest = data['guests']
    requirements = data['requirements']
    status = 'Не оплачено'
    insert_to_booking(message.from_user.id, date_time, guest, requirements, status)
    await state.clear()
    await message.answer_invoice(
        title='Депозит на бронирование',
        description='Оплата за бронь столика в Ресторане Тбилиссо',
        payload='success-payment',
        provider_token='1744374395:TEST:0e11fb6d26df9a555a05',
        prices=PRICE,
        currency='RUB'
    )



