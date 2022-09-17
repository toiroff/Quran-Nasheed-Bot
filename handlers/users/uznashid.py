from aiogram import types
from keyboards.default.uznashids import uznashids_button
from loader import dp,db

# Echo bot
@dp.message_handler(text="O'zbekcha Nashidalar🇺🇿")
async def bot_echo(message: types.Message):
    await message.answer(f"O'zbekcha Nashidalar🇺🇿",reply_markup=uznashids_button)