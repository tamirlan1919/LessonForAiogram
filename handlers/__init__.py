from aiogram import Router
from .start import router as start_router
from .book import router as booking_router

router = Router()

router.include_routers(start_router,booking_router)