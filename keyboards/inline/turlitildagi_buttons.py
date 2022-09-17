from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
turkcha_buttons=InlineKeyboardMarkup(
inline_keyboard=[
        [
             InlineKeyboardButton(text="© Maher zain",callback_data='t1'),
        ],
        [
             InlineKeyboardButton(text="©Sami Yusuf",callback_data='t3'),
             InlineKeyboardButton(text="©Mohamed Tarek",callback_data='t4')
        ]
    ],

)
arabcha_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="© Muhammad Al Muqit",callback_data='a1')
        ],
        [
            InlineKeyboardButton(text="Ahmed Bukhatir",callback_data='a2'),
            InlineKeyboardButton(text="Abu Yasser",callback_data='a3')
        ],
        [
            InlineKeyboardButton(text="Mishari Rashid Al Afasiy",callback_data='a4'),

        ],

    ]
)
chechencha_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🎙 Абдурахмон Гаджев',callback_data='ch1'),

        ],
        [
            InlineKeyboardButton(text="Xadicha Muhammedova🎙",callback_data='ch2')
        ]
    ]
)
falastin_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Falastin Nashidalari 1-10',callback_data='f1')
        ],
        [
            InlineKeyboardButton(text='Falastin Nashidalari 11-20',callback_data='f2')
        ]
    ]
)
keyingiz_arabcha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Keyingi Bo'lim",callback_data='ka1')
        ]
    ]
)
keyingi_arabcha2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Keyingiz Bo'lim",callback_data='ka2')
        ]
    ]
)