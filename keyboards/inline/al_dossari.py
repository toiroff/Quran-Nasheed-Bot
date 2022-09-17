from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery

from keyboards.default.pora30 import pora30_button
from loader import dp, bot

al_dossari=InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text='Fotiha😇',callback_data='dossari1'),
            InlineKeyboardButton(text='Baqoro😇',callback_data='dossari2'),
            InlineKeyboardButton(text='Oli imron😇',callback_data='dossari3'),
        ],
        [
            InlineKeyboardButton(text='Nisa😇',callback_data='dossari4'),
            InlineKeyboardButton(text="Ma'ida😇",callback_data='dossari5'),
            InlineKeyboardButton(text="An'am😇",callback_data='dossari6'),
            ],
        [
            InlineKeyboardButton(text="Ar'of😇",callback_data='dossari7'),
            InlineKeyboardButton(text='Anfal😇',callback_data='dossari8'),
            InlineKeyboardButton(text='Tavba😇',callback_data='dossari9'),
        ],

        [
            InlineKeyboardButton(text='Yunus😇',callback_data='dossari10'),
            InlineKeyboardButton(text='Hud😇',callback_data='dossari11'),
            InlineKeyboardButton(text='Yusuf😇',callback_data='dossari12')
        ],
        [
            InlineKeyboardButton(text="Ra'd😇",callback_data='dossari13'),
            InlineKeyboardButton(text='Ibrohim😇',callback_data='dossari14'),
            InlineKeyboardButton(text='Hijr😇',callback_data='dossari15')
        ],
        [
            InlineKeyboardButton(text='Nahl😇',callback_data='dossari16'),
            InlineKeyboardButton(text='Isro😇',callback_data='dossari17'),
            InlineKeyboardButton(text='Kahf😇',callback_data='dossari18')
        ],
        [
            InlineKeyboardButton(text='Maryam😇',callback_data='dossari19'),
            InlineKeyboardButton(text='Toha😇',callback_data='dossari20'),
            InlineKeyboardButton(text='Anbiya😇',callback_data='dossari21')
        ],
        [
            InlineKeyboardButton(text='Haj😇',callback_data='dossari22'),
            InlineKeyboardButton(text="Mu'minun😇",callback_data='dossari23'),
            InlineKeyboardButton(text='Nur😇',callback_data='dossari24')
        ],
        [
            InlineKeyboardButton(text='Furqon😇',callback_data='dossari25'),
            InlineKeyboardButton(text='Shuaro😇',callback_data='dossari26'),
            InlineKeyboardButton(text='Naml😇',callback_data='dossari27')
        ],
        [
            InlineKeyboardButton(text='Qosos😇',callback_data='dossari28'),
            InlineKeyboardButton(text='Ankabut😇',callback_data='dossari29'),
            InlineKeyboardButton(text='Rum😇',callback_data='dossari30')
        ],
        [
            InlineKeyboardButton(text='Luqman😇',callback_data='dossari31'),
            InlineKeyboardButton(text='Sajda😇',callback_data='dossari32'),
            InlineKeyboardButton(text='Axzab😇',callback_data='dossari33')
        ],
        [
            InlineKeyboardButton(text='Saba😇',callback_data='dossari34'),
            InlineKeyboardButton(text='Fatir😇',callback_data='dossari35'),
            InlineKeyboardButton(text='Yasin😇',callback_data='dossari36')
        ],
        [
            InlineKeyboardButton(text='Soffat😇',callback_data='dossari37'),
            InlineKeyboardButton(text='Sod😇',callback_data='dossari38'),
            InlineKeyboardButton(text='Zumar😇',callback_data='dossari39')
        ],
        [
            InlineKeyboardButton(text="G'ofir😇",callback_data='dossari40'),
            InlineKeyboardButton(text='Fussilat😇',callback_data='dossari41'),
            InlineKeyboardButton(text='Shuro😇',callback_data='dossari42')
        ],
        [
            InlineKeyboardButton(text='Zuxruf😇',callback_data='dossari43'),
            InlineKeyboardButton(text='Duxon😇',callback_data='dossari44'),
            InlineKeyboardButton(text='Jasiyah😇',callback_data='dossari45')
        ],
[
            InlineKeyboardButton(text='Ahqof😇',callback_data='dossari46'),
            InlineKeyboardButton(text='Muhammad😇',callback_data='dossari47'),
            InlineKeyboardButton(text='Fath😇',callback_data='dossari48'),
        ],
        [
            InlineKeyboardButton(text='Hujurot😇',callback_data='dossari49'),
            InlineKeyboardButton(text="Qof😇",callback_data='dossari50'),
            InlineKeyboardButton(text="Zariyat😇",callback_data='dossari51'),
            ],
        [
            InlineKeyboardButton(text="Tur😇",callback_data='dossari52'),
            InlineKeyboardButton(text='Najm😇',callback_data='dossari53'),
            InlineKeyboardButton(text='Qomar😇',callback_data='dossari54'),
        ],

        [
            InlineKeyboardButton(text='Ar Rohman😇',callback_data='dossari55'),
            InlineKeyboardButton(text='Vaqia😇',callback_data='dossari56'),
            InlineKeyboardButton(text='Hadid😇',callback_data='dossari57')
        ],
        [
            InlineKeyboardButton(text='Mujodala😇',callback_data='dossari58'),
            InlineKeyboardButton(text='Hashr😇',callback_data='dossari59'),
            InlineKeyboardButton(text='Mumtahana😇',callback_data='dossari60')
        ],
        [
            InlineKeyboardButton(text='Soff😇',callback_data='dossari61'),
            InlineKeyboardButton(text="Jumu'a😇",callback_data='dossari62'),
            InlineKeyboardButton(text='Munafiqun😇',callback_data='dossari63')
        ],
        [
            InlineKeyboardButton(text="Tag'obun😇",callback_data='dossari64'),
            InlineKeyboardButton(text='Tolaq😇',callback_data='dossari65'),
            InlineKeyboardButton(text='Tahrim😇',callback_data='dossari66')
        ],
        [
            InlineKeyboardButton(text='Mulk😇',callback_data='dossari67'),
            InlineKeyboardButton(text="Qolam😇",callback_data='dossari68'),
            InlineKeyboardButton(text='Haqqoh😇',callback_data='dossari69')
        ],
        [
            InlineKeyboardButton(text="Ma'arij😇",callback_data='dossari70'),
            InlineKeyboardButton(text='Nuh😇',callback_data='dossari71'),
            InlineKeyboardButton(text='Jin😇',callback_data='dossari72')
        ],
        [
            InlineKeyboardButton(text='Muzzammil😇',callback_data='dossari73'),
            InlineKeyboardButton(text='Muddasir😇',callback_data='dossari74'),
            InlineKeyboardButton(text='Qiyamah😇',callback_data='dossari75')
        ],
        [
            InlineKeyboardButton(text='Insan😇',callback_data='dossari76'),
            InlineKeyboardButton(text='Mursalat😇',callback_data='dossari77'),
            InlineKeyboardButton(text='Naba😇',callback_data='dossari78')
        ],
        [
            InlineKeyboardButton(text='Naziat😇',callback_data='dossari79'),
            InlineKeyboardButton(text='Abasa😇',callback_data='dossari80'),
            InlineKeyboardButton(text='Takvir😇',callback_data='dossari81')
        ],
        [
            InlineKeyboardButton(text='Intifor😇',callback_data='dossari82'),
            InlineKeyboardButton(text='Mutoffifun😇',callback_data='dossari83'),
            InlineKeyboardButton(text='Inshiqoq😇',callback_data='dossari84')
        ],
        [
            InlineKeyboardButton(text="Buruj😇",callback_data='dossari85'),
            InlineKeyboardButton(text='Toriq😇',callback_data='dossari86'),
            InlineKeyboardButton(text="A'la😇",callback_data='dossari87')
        ],
        [
            InlineKeyboardButton(text="G'oshiyah😇",callback_data='dossari88'),
            InlineKeyboardButton(text='Fajr😇',callback_data='dossari89'),
            InlineKeyboardButton(text='Balad😇',callback_data='dossari90')
        ],
[
            InlineKeyboardButton(text='Shams😇',callback_data='dossari91'),
            InlineKeyboardButton(text='Layl😇',callback_data='dossari92'),
            InlineKeyboardButton(text='Zuho😇',callback_data='dossari93'),
        ],
        [
            InlineKeyboardButton(text='Sharh😇',callback_data='dossari94'),
            InlineKeyboardButton(text="Tiyn😇",callback_data='dossari95'),
            InlineKeyboardButton(text="Alaq😇",callback_data='dossari96'),
            ],
        [
            InlineKeyboardButton(text="Qadr😇",callback_data='dossari97'),
            InlineKeyboardButton(text='Bayyina😇',callback_data='dossari98'),
            InlineKeyboardButton(text='Zalzala😇',callback_data='dossari99'),
        ],


        [


        ],




    ],



)
al_d2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Adiyat☪️', callback_data='dossari100'),
            InlineKeyboardButton(text='Qoriya☪️', callback_data='dossari101'),
            InlineKeyboardButton(text='Takasur☪️', callback_data='dossari102')
        ],
        [
            InlineKeyboardButton(text='Asr☪️', callback_data='dossari103'),
            InlineKeyboardButton(text='Humaza☪️', callback_data='dossari104'),
            InlineKeyboardButton(text='Fil☪️', callback_data='dossari105')
        ],
        [
            InlineKeyboardButton(text='Quraysh☪️', callback_data='dossari106'),
            InlineKeyboardButton(text="Ma'un☪️", callback_data='dossari107'),
            InlineKeyboardButton(text='Kavsar☪️', callback_data='dossari108')
        ],
        [
            InlineKeyboardButton(text='Kafirun☪️ va Nasr☪️', callback_data='dossari109'),
            InlineKeyboardButton(text='Masad☪️', callback_data='dossari110'),


        ],
        [
            InlineKeyboardButton(text='Ixlos☪️ va Falaq☪️', callback_data='dossari111'),
        ],
        [
            InlineKeyboardButton(text='Nas☪️', callback_data='dossari112'),
            InlineKeyboardButton(text='Ulashish☪️', switch_inline_query='')
        ]
    ]
)
keying_sahifa =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Keyingi sahifa🕌'),
            KeyboardButton(text="🔙 Orqaga")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(text='🎙Yasser Al Dossari')
async def echo_bot(message  : types.Message):
    await bot.send_photo(chat_id=message.from_user.id,photo='https://i1.sndcdn.com/artworks-000396828012-1emi2k-t500x500.jpg')
    await message.answer(f"Siz ushbu bo'limda mashxur qori Yasser Al Dossarining qiroatlaridan baxramand bo'lasiz!\n \n"
"Quyidagi suralardan tinglamoqchi bo'lgan surangizni topishingiz mumkin!🕌",reply_markup=al_dossari)
    await message.answer("Keyingi Suralarga o'tish uchun Keyingi sahifa tugmasini bosing☪️",reply_markup=keying_sahifa)
@dp.message_handler(text='Keyingi sahifa🕌')
async def echo_bot(message: types.Message):
    await message.answer("Siz ushbu bo'limda mashxur qori Yasser Al Dossarining qiroatlaridan baxramand bo'lasiz!😊",reply_markup=al_d2)

@dp.message_handler(text='🔙 Orqaga')
async def echo_bot(message: types.Message):
    await message.answer(f"Ushbu bo'limda siz eng mashxur qorilarning barcha audio shakldagi 30 pora qiroatlarini topasiz In Sha Alloh!🕌",reply_markup=pora30_button)
