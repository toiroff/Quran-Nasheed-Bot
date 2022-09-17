from aiogram import types
from aiogram.types import CallbackQuery


from loader import dp, bot



@dp.message_handler(text="Go'zal Azonlar 🎧")
async def turkcha(message : types.Message):
    await message.answer(f'Tojikcha  Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/739?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/740?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/741?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/742?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/743?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/744?single')

