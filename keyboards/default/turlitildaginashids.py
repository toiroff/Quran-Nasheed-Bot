from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.turlitildagi_buttons import *

from loader import dp

turlitildagi_nasheed=ReplyKeyboardMarkup(
       keyboard=[
        [
            KeyboardButton(text="Arabcha Nashidalar🇸🇦"),
            KeyboardButton(text="Turkcha Nashidalar🇹🇷")
        ],
        [
            KeyboardButton(text="Chechencha Nashidalar🇧🇾"),
            KeyboardButton(text="Falastin Nashidalar🇵🇸")
        ],
        [
            KeyboardButton(text="Tojikcha Nashidalar🇹🇯"),
            KeyboardButton(text="Pokiston Nashidalar🇵🇰")
        ],
        [
            KeyboardButton(text="Dasturchi💻"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],resize_keyboard=True
)
@dp.message_handler(text='Arabcha Nashidalar🇸🇦')
async def turkcha(message : types.Message):
    await message.answer(f'🎵Arabcha Nasheed',reply_markup=arabcha_buttons)

@dp.message_handler(text='Turkcha Nashidalar🇹🇷')
async def turkcha(message : types.Message):
    await message.answer(f'🎵Turkcha Nasheed',reply_markup=turkcha_buttons)

@dp.message_handler(text='Chechencha Nashidalar🇧🇾')
async def turkcha(message: types.Message):
    await message.answer(f'🎵Chechen Nasheed', reply_markup=chechencha_buttons)

@dp.message_handler(text='Falastin Nashidalar🇵🇸')
async def turkcha(message: types.Message):
    await message.answer(f'🎵Chechen Nasheed', reply_markup=falastin_buttons)
