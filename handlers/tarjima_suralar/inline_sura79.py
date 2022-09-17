from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura79')
async def suralar(message:CallbackQuery):
     await message.message.answer(text="Noziot Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio='for_send/Noziot.docx')

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
