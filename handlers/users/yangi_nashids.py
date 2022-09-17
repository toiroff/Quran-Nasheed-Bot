from aiogram import types
from aiogram.types import CallbackQuery


from loader import dp, bot



@dp.message_handler(text="Yangi Nashidalar🎧")
async def turkcha(message : types.Message):
    await message.answer(f'Tojikcha  Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/730?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/731?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/732?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/733?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/734?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/735?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/736?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/737?single')