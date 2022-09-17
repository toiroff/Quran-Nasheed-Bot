from aiogram import types
from aiogram.types import CallbackQuery


from loader import dp, bot



@dp.message_handler(text="Pokiston Nashidalar🇵🇰")
async def turkcha(message : types.Message):
    await message.answer(f'Pokiston 🇵🇰 Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/681?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/682?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/683?single')

