from aiogram import types


from loader import dp, bot


@dp.message_handler(text='«Ramazon» Haqida')
async def turkcha(message : types):
    await message.answer(f'🎙 Ramazon Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/685?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/686?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/687?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/688?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/689?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/690?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/691?single')

