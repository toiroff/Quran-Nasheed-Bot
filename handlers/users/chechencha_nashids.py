from aiogram.types import CallbackQuery

from loader import dp, bot


@dp.callback_query_handler(text='ch1')
async def turkcha(message : CallbackQuery):
    await message.answer(f'🎙 Абдурахмон Гаджев Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/627?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/628?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/629?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/630?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/631?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/632?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/633?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/634?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/635?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/636?single')

@dp.callback_query_handler(text='ch2')
async def turkcha(message : CallbackQuery):
    await message.answer(f'🎙Xadicha Muhammedova Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/638?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/639?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/640?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/641?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/642?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/643?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/644?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/645?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/646?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/647?single')