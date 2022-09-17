from aiogram import types


from loader import dp, bot


@dp.message_handler(text='Aralash Nashidalar 🎧')
async def turkcha(message : types):
    await message.answer(f'🎙Aralash Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/693?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/694?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/695?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/696?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/697?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/698?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/699?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/670?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/671?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/672?single')