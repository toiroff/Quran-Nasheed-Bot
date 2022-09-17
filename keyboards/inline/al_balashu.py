from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery

from keyboards.default.pora30 import pora30_button
from loader import dp, bot

al_balashu=InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text='Fotiha😇',callback_data='g1'),
            InlineKeyboardButton(text='Baqoro😇',callback_data='g2'),
            InlineKeyboardButton(text='Oli imron😇',callback_data='g3'),
        ],
        [
            InlineKeyboardButton(text='Nisa😇',callback_data='g4'),
            InlineKeyboardButton(text="Ma'ida😇",callback_data='g5'),
            InlineKeyboardButton(text="An'am😇",callback_data='g6'),
            ],
        [
            InlineKeyboardButton(text="Ar'of😇",callback_data='g7'),
            InlineKeyboardButton(text='Anfal😇',callback_data='g8'),
            InlineKeyboardButton(text='Tavba😇',callback_data='g9'),
        ],

        [
            InlineKeyboardButton(text='Yunus😇',callback_data='g10'),
            InlineKeyboardButton(text='Hud😇',callback_data='g11'),
            InlineKeyboardButton(text='Yusuf😇',callback_data='g12')
        ],
        [
            InlineKeyboardButton(text="Ra'd😇",callback_data='g13'),
            InlineKeyboardButton(text='Ibrohim😇',callback_data='g14'),
            InlineKeyboardButton(text='Hijr😇',callback_data='g15')
        ],
        [
            InlineKeyboardButton(text='Nahl😇',callback_data='g16'),
            InlineKeyboardButton(text='Isro😇',callback_data='g17'),
            InlineKeyboardButton(text='Kahf😇',callback_data='g18')
        ],
        [
            InlineKeyboardButton(text='Maryam😇',callback_data='g19'),
            InlineKeyboardButton(text='Toha😇',callback_data='g20'),
            InlineKeyboardButton(text='Anbiya😇',callback_data='g21')
        ],
        [
            InlineKeyboardButton(text='Haj😇',callback_data='g22'),
            InlineKeyboardButton(text="Mu'minun😇",callback_data='g23'),
            InlineKeyboardButton(text='Nur😇',callback_data='g24')
        ],
        [
            InlineKeyboardButton(text='Furqon😇',callback_data='g25'),
            InlineKeyboardButton(text='Shuaro😇',callback_data='g26'),
            InlineKeyboardButton(text='Naml😇',callback_data='g27')
        ],
        [
            InlineKeyboardButton(text='Qosos😇',callback_data='g28'),
            InlineKeyboardButton(text='Ankabut😇',callback_data='g29'),
            InlineKeyboardButton(text='Rum😇',callback_data='g30')
        ],
        [
            InlineKeyboardButton(text='Luqman😇',callback_data='g31'),
            InlineKeyboardButton(text='Sajda😇',callback_data='g32'),
            InlineKeyboardButton(text='Axzab😇',callback_data='g33')
        ],
        [
            InlineKeyboardButton(text='Saba😇',callback_data='g34'),
            InlineKeyboardButton(text='Fatir😇',callback_data='g35'),
            InlineKeyboardButton(text='Yasin😇',callback_data='g36')
        ],
        [
            InlineKeyboardButton(text='Soffat😇',callback_data='g37'),
            InlineKeyboardButton(text='Sod😇',callback_data='g38'),
            InlineKeyboardButton(text='Zumar😇',callback_data='g39')
        ],
        [
            InlineKeyboardButton(text="G'ofir😇",callback_data='g40'),
            InlineKeyboardButton(text='Fussilat😇',callback_data='g41'),
            InlineKeyboardButton(text='Shuro😇',callback_data='g42')
        ],
        [
            InlineKeyboardButton(text='Zuxruf😇',callback_data='g43'),
            InlineKeyboardButton(text='Duxon😇',callback_data='g44'),
            InlineKeyboardButton(text='Jasiyah😇',callback_data='g45')
        ],
[
            InlineKeyboardButton(text='Ahqof😇',callback_data='g46'),
            InlineKeyboardButton(text='Muhammad😇',callback_data='g47'),
            InlineKeyboardButton(text='Fath😇',callback_data='g48'),
        ],
        [
            InlineKeyboardButton(text='Hujurot😇',callback_data='g49'),
            InlineKeyboardButton(text="Qof😇",callback_data='g50'),
            InlineKeyboardButton(text="Zariyat😇",callback_data='g51'),
            ],
        [
            InlineKeyboardButton(text="Tur😇",callback_data='g52'),
            InlineKeyboardButton(text='Najm😇',callback_data='g53'),
            InlineKeyboardButton(text='Qomar😇',callback_data='g54'),
        ],

        [
            InlineKeyboardButton(text='Ar Rohman😇',callback_data='g55'),
            InlineKeyboardButton(text='Vaqia😇',callback_data='g56'),
            InlineKeyboardButton(text='Hadid😇',callback_data='g57')
        ],
        [
            InlineKeyboardButton(text='Mujodala😇',callback_data='g58'),
            InlineKeyboardButton(text='Hashr😇',callback_data='g59'),
            InlineKeyboardButton(text='Mumtahana😇',callback_data='g60')
        ],
        [
            InlineKeyboardButton(text='Soff😇',callback_data='g61'),
            InlineKeyboardButton(text="Jumu'a😇",callback_data='g62'),
            InlineKeyboardButton(text='Munafiqun😇',callback_data='g63')
        ],
        [
            InlineKeyboardButton(text="Tag'obun😇",callback_data='g64'),
            InlineKeyboardButton(text='Tolaq😇',callback_data='g65'),
            InlineKeyboardButton(text='Tahrim😇',callback_data='g66')
        ],
        [
            InlineKeyboardButton(text='Mulk😇',callback_data='g67'),
            InlineKeyboardButton(text="Qolam😇",callback_data='g68'),
            InlineKeyboardButton(text='Haqqoh😇',callback_data='g69')
        ],
        [
            InlineKeyboardButton(text="Ma'arij😇",callback_data='g70'),
            InlineKeyboardButton(text='Nuh😇',callback_data='g71'),
            InlineKeyboardButton(text='Jin😇',callback_data='g72')
        ],
        [
            InlineKeyboardButton(text='Muzzammil😇',callback_data='g73'),
            InlineKeyboardButton(text='Muddasir😇',callback_data='g74'),
            InlineKeyboardButton(text='Qiyamah😇',callback_data='g75')
        ],
        [
            InlineKeyboardButton(text='Insan😇',callback_data='g76'),
            InlineKeyboardButton(text='Mursalat😇',callback_data='g77'),
            InlineKeyboardButton(text='Naba😇',callback_data='g78')
        ],
        [
            InlineKeyboardButton(text='Naziat😇',callback_data='g79'),
            InlineKeyboardButton(text='Abasa😇',callback_data='g80'),
            InlineKeyboardButton(text='Takvir😇',callback_data='g81')
        ],
        [
            InlineKeyboardButton(text='Intifor😇',callback_data='g82'),
            InlineKeyboardButton(text='Mutoffifun😇',callback_data='g83'),
            InlineKeyboardButton(text='Inshiqoq😇',callback_data='g84')
        ],
        [
            InlineKeyboardButton(text="Buruj😇",callback_data='g85'),
            InlineKeyboardButton(text='Toriq😇',callback_data='g86'),
            InlineKeyboardButton(text="A'la😇",callback_data='g87')
        ],
        [
            InlineKeyboardButton(text="G'oshiyah😇",callback_data='g88'),
            InlineKeyboardButton(text='Fajr😇',callback_data='g89'),
            InlineKeyboardButton(text='Balad😇',callback_data='g90')
        ],
[
            InlineKeyboardButton(text='Shams😇',callback_data='g91'),
            InlineKeyboardButton(text='Layl😇',callback_data='g92'),
            InlineKeyboardButton(text='Zuho😇',callback_data='g93'),
        ],
        [
            InlineKeyboardButton(text='Sharh😇',callback_data='g94'),
            InlineKeyboardButton(text="Tiyn😇",callback_data='g95'),
            InlineKeyboardButton(text="Alaq😇",callback_data='g96'),
            ],
        [
            InlineKeyboardButton(text="Qadr😇",callback_data='g97'),
            InlineKeyboardButton(text='Bayyina😇',callback_data='g98'),
            InlineKeyboardButton(text='Zalzala😇',callback_data='g99'),
        ],


        [


        ],




    ],



)
al_balashu2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Adiyat☪️', callback_data='g100'),
            InlineKeyboardButton(text='Qoriya☪️', callback_data='g101'),
            InlineKeyboardButton(text='Takasur☪️', callback_data='g102')
        ],
        [
            InlineKeyboardButton(text='Asr☪️', callback_data='g103'),
            InlineKeyboardButton(text='Humaza☪️', callback_data='g104'),
            InlineKeyboardButton(text='Fil☪️', callback_data='g105')
        ],
        [
            InlineKeyboardButton(text='Quraysh☪️', callback_data='g106'),
            InlineKeyboardButton(text="Ma'un☪️", callback_data='g107'),
            InlineKeyboardButton(text='Kavsar☪️', callback_data='g108')
        ],
        [
            InlineKeyboardButton(text='Kafirun☪️ va Nasr☪️', callback_data='g109'),
            InlineKeyboardButton(text='Masad☪️', callback_data='g110'),


        ],
        [
            InlineKeyboardButton(text='Ixlos☪️ va Falaq☪️', callback_data='g111'),
        ],
        [
            InlineKeyboardButton(text='Nas☪️', callback_data='g112'),
            InlineKeyboardButton(text='Ulashish☪️', switch_inline_query='')
        ]
    ]
)
keying_sahifa =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Keyingi sahifa☪️'),
            KeyboardButton(text="🔙 Orqaga")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(text='🎙️Hazza Al Balushi')
async def echo_bot(message  : types.Message):
    await bot.send_photo(chat_id=message.from_user.id,photo='https://i.scdn.co/image/ab6761610000e5ebe08dc8ea5cf98a8a96db795c')
    await message.answer(f"Siz ushbu bo'limda mashxur qori Hazza Al Balushining qiroatlaridan baxramand bo'lasiz!\n \n"
"Quyidagi suralardan tinglamoqchi bo'lgan surangizni topishingiz mumkin!🕌",reply_markup=al_balashu)
    await message.answer("Keyingi Suralarga o'tish uchun Keyingi sahifa tugmasini bosing☪️",reply_markup=keying_sahifa)
@dp.message_handler(text='Keyingi sahifa☪️')
async def echo_bot(message: types.Message):
    await message.answer("Siz ushbu bo'limda mashxur qori Mishari Rashid Al Afasiyning qiroatlaridan baxramand bo'lasiz!😊",reply_markup=al_balashu2)

@dp.message_handler(text='🔙 Orqaga')
async def echo_bot(message: types.Message):
    await message.answer(f"Ushbu bo'limda siz eng mashxur qorilarning barcha audio shakldagi 30 pora qiroatlarini topasiz In Sha Alloh!🕌",reply_markup=pora30_button)

