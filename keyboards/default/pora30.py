from aiogram import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import dp

pora30_button= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎙Mishari Rashid Al Afasiy"),
        ],
        [
            KeyboardButton(text="🎙️Hazza Al Balushi"),
            KeyboardButton(text="🎙Yasser Al Dossari")
        ],
        [
            KeyboardButton(text="🎙Abu-Bakr Ash-Shatri")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Qur'oni Karim 30pora!📖")
async def echo_bot(message : types.Message):
    await message.answer(f"Ushbu bo'limda siz eng mashxur qorilarning barcha audio shakldagi 30 pora qiroatlarini topasiz In Sha Alloh!🕌",reply_markup=pora30_button)