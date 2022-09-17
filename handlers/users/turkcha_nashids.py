from aiogram import types
from aiogram.types import CallbackQuery


from loader import dp, bot



@dp.message_handler(text="Tojikcha Nashidalar🇹🇯")
async def turkcha(message : types.Message):
    await message.answer(f'Tojikcha  Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/670?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/671?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/672?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/673?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/674?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/675?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/676?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/678?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/679?single')
