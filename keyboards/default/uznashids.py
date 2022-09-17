from aiogram import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from loader import dp, bot

uznashids_button= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbekcha Nashidalar"),
            KeyboardButton(text="Muhammadjon Qori😇")
        ],
        [
            KeyboardButton(text="Nilufar bintu Ulug'bek🌹"),
            KeyboardButton(text="Izzat Shukurov")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]

    ],resize_keyboard=True

)
nilufar_bintu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nilufar bintu Ulug'bek-1"),
        ],
        [
            KeyboardButton(text="Nilufar bintu Ulug'bek-2")
        ],
        [
            KeyboardButton(text="Nilufar bintu Ulug'bek-3")
        ],
        [
            KeyboardButton(text="Nilufar bintu Ulug'bek Nashidalar To'plami")
        ],
        [
            KeyboardButton(text="Orqaga🔙")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Orqaga🔙")
async def echo_bot(messsage : types.Message):
    await messsage.answer(f"O'zbekcha Nashidalar🇺🇿",reply_markup=uznashids_button)
@dp.message_handler(text="O'zbekcha Nashidalar")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli bo'limni tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/492?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/493?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/494?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/495?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/496?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/497?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/498?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/499?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/500?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/501?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Muhammadjon Qori😇")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/503?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/504?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/505?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/506?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Nilufar bintu Ulug'bek🌹")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli sahifani tanlang ⤵️",reply_markup=nilufar_bintu)

@dp.message_handler(text="Nilufar bintu Ulug'bek-1")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/508?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/509?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/510?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/511?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/512?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/513?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/514?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/515?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Nilufar bintu Ulug'bek-2")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/516?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/517?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/518?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/519?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/520?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/521?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/522?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/523?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/524?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/525?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Nilufar bintu Ulug'bek-3")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/527?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Nilufar bintu Ulug'bek Nashidalar To'plami")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/529?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)

@dp.message_handler(text="Izzat Shukurov")
async def echo_bot(message : types.Message):
    await message.answer(f"O'zingizga kerakli nashidani tanlang ⤵️")
    audio_manzil = 'https://t.me/nashidsmedia/531?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/532?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/533?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)
    audio_manzil = 'https://t.me/nashidsmedia/534?single'
    await bot.send_audio(chat_id=message.from_user.id,audio=audio_manzil)