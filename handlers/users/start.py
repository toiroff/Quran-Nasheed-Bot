

import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.yonalishlar import yonalishlar_button
from loader import dp, db, bot
from filters import Shaxsiy

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.first_name
    try:
        db.qoshish(id=message.from_user.id, name=name)
    except Exception:
        pass

    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Inshaalloh bu botimiz sizga foyda beradi!😊")
    await message.answer(f" \n \nBotda xato-kamchiliklar bo'lsa, Avvalo Allohdan, so'ngra sizdan kechirim so'raymiz!☪️",reply_markup=yonalishlar_button)
