from aiogram.types import Message
from aiogram import Router

other_router = Router()

@other_router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо!{message.text}')