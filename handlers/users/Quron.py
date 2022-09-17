from aiogram import types

from keyboards.inline.inline_buttons import inline_tugmalar
from keyboards.default.yonalishlar import keying_bolim
from loader import dp

@dp.message_handler(text="Qur'oni Karim tarjimalari😇")
async def suralar(sura: types.Message):
    await sura.answer(text="Botimizdagi ma'lumotlarning barchasi www.ziyouz.com saytidan olingan bo'lib, Alouddin Mansur tarjimasi😊Qur'oni Karim suralarini tanlang😇",reply_markup=inline_tugmalar)
    await sura.answer(text="Keyingi sahifaga o'tish uchun Keyingi Sahifa😇 tugmasini bosing",reply_markup=keying_bolim)