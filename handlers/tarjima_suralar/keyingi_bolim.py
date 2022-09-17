from aiogram import types
from handlers.tarjima_suralar.keyingi_inline_buttons import keyingi_inline_tugmalar
from loader import dp

@dp.message_handler(text="Keyingi sahifa😇")
async def suralar(sura: types.Message):
    await sura.answer(text="Keyingi sahifadagi suralarni tanlang😇",reply_markup=keyingi_inline_tugmalar)
