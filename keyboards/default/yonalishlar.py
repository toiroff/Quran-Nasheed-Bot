from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

yonalishlar_button= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qur'oni Karim tarjimalari😇"),
        ],
        [
            KeyboardButton(text="Qur'oni Karim 30pora!📖")
        ],
        [
            KeyboardButton(text="O'zbekcha Nashidalar🇺🇿"),
            KeyboardButton(text="Turli tildagi Nashidalar🌐")
        ],
        [
            KeyboardButton(text="Turli Xil Nashidalar😇"),
            KeyboardButton(text="Yangi Nashidalar🎧")
        ],
        [
            KeyboardButton(text="Go'zal Azonlar 🎧"),
            KeyboardButton(text="👨‍👩‍👧‍👦 Biz haqimizda")
        ],
        [
            KeyboardButton(text="Adminga murojaat✍️")
        ]

    ],resize_keyboard=True

)
keying_bolim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Keyingi sahifa😇"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
asosiym = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
