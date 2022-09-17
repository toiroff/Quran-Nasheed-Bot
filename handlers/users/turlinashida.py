from aiogram import types
from keyboards.default.turlitildaginashids import turlitildagi_nasheed
from loader import dp,db

# Echo bot
@dp.message_handler(text="Turli tildagi Nashidalar🌐")
async def bot_echo(message: types.Message):
    await message.reply(f"Turli tildagi Nashidalar🌐",reply_markup=turlitildagi_nasheed)