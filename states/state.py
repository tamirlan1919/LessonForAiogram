from aiogram.fsm.state import State, StatesGroup


class Booking(StatesGroup):
    date_booking = State()
    time_booking = State()
    guests_booking = State()
    requirements_booking = State()
