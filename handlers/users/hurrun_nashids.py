from aiogram import types
from aiogram.types import CallbackQuery


from loader import dp, bot



@dp.message_handler(text="Axi Anta Hurrun")
async def turkcha(message : types.Message):
    await message.answer(f'Axi Anta Hurrun 🇵🇰 Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/704?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/705?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/706?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/707?single')