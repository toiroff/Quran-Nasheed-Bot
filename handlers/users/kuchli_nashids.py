from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default.turlixilnashids import kuchli2
from loader import dp, bot


@dp.message_handler(text='Kuchli Nashidalar 🦁⚔️')
async def turkcha(message : types.Message):
    await message.answer(f'🎙Kuchli  Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/709?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/710?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/711?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/712?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/713?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/714?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/715?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/716?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/717?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/718?single',reply_markup=kuchli2)




@dp.callback_query_handler(text='kk1')
async def turkcha(message :CallbackQuery):
    await message.answer(f'🎙Kuchli  Nasheeds')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/719?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/720?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/721?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/722?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/723?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/724?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/725?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/726?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/727?single')
    await bot.send_audio(chat_id=message.from_user.id,audio='https://t.me/nashidsmedia/728?single')