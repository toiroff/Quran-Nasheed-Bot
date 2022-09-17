from aiogram import types
from filters import Shaxsiy
from keyboards.default.yonalishlar import yonalishlar_button
from loader import dp,db

# Echo bot
@dp.message_handler(text='🔝 Asosiy Menyu')
async def bot_echo(message: types.Message):
    await message.answer(text=f"Assalomu alaykum, {message.from_user.full_name}! Inshaalloh bu botimiz sizga foyda beradi!😇",reply_markup=yonalishlar_button)
