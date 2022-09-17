from aiogram import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

from loader import dp

turlixil_button= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Aralash Nashidalar 🎧"),

        ],
        [
            KeyboardButton(text='«Ramazon» Haqida'),
            KeyboardButton(text="Axi Anta Hurrun")
        ],
        [
            KeyboardButton(text="Kuchli Nashidalar 🦁⚔️"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Turli Hil Nashidalar😇")
async def echo_bot(message : types.Message):
    await message.answer(f'Assalomu alaykum va Rahmatullohi va Barakatuh Hurmatli Obunachi👤 siz bu yerda Turli xil Nashidalarni topishingiz mumkun 😊',reply_markup=turlixil_button)

kuchli2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Keyingi Bo'lim",callback_data="kk1")
        ]
    ]
)