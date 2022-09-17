from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


tas_bek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Tasdiqlash',callback_data='tasdiqlash')
        ],
        [
            InlineKeyboardButton(text='Bekor qilish',callback_data='bekor')
        ]
    ]
)