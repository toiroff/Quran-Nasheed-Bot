from aiogram.types import CallbackQuery

from loader import dp, bot


@dp.callback_query_handler(text='f1')
async def turkcha(message : CallbackQuery):
    await message.answer(f'🎙 Абдурахмон Гаджев Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/649?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/650?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/651?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/652?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/653?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/654?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/655?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/656?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/657?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/658?single')

@dp.callback_query_handler(text='f2')
async def turkcha(message : CallbackQuery):
    await message.answer(f'🎙Xadicha Muhammedova Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/659?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/660?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/661?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/662?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/663?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/664?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/665?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/666?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/667?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/668?single')