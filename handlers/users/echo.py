from aiogram import types
from filters import Shaxsiy
from loader import dp,db

# Echo bot
@dp.message_handler(Shaxsiy(),commands='Baza')
async def bot_echo(message: types.Message):
    db.create_table_users()
    await message.answer(text='Baza yaratildi')

# @dp.message_handler(Shaxsiy(),state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
