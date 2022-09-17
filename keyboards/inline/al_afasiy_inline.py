from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery

from keyboards.default.pora30 import pora30_button
from loader import dp, bot

al_afasiy=InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text='Fotiha😇',callback_data='pora1'),
            InlineKeyboardButton(text='Baqoro😇',callback_data='pora2'),
            InlineKeyboardButton(text='Oli imron😇',callback_data='pora3'),
        ],
        [
            InlineKeyboardButton(text='Nisa😇',callback_data='pora4'),
            InlineKeyboardButton(text="Ma'ida😇",callback_data='pora5'),
            InlineKeyboardButton(text="An'am😇",callback_data='pora6'),
            ],
        [
            InlineKeyboardButton(text="Ar'of😇",callback_data='pora7'),
            InlineKeyboardButton(text='Anfal😇',callback_data='pora8'),
            InlineKeyboardButton(text='Tavba😇',callback_data='pora9'),
        ],

        [
            InlineKeyboardButton(text='Yunus😇',callback_data='pora10'),
            InlineKeyboardButton(text='Hud😇',callback_data='pora11'),
            InlineKeyboardButton(text='Yusuf😇',callback_data='pora12')
        ],
        [
            InlineKeyboardButton(text="Ra'd😇",callback_data='pora13'),
            InlineKeyboardButton(text='Ibrohim😇',callback_data='pora14'),
            InlineKeyboardButton(text='Hijr😇',callback_data='pora15')
        ],
        [
            InlineKeyboardButton(text='Nahl😇',callback_data='pora16'),
            InlineKeyboardButton(text='Isro😇',callback_data='pora17'),
            InlineKeyboardButton(text='Kahf😇',callback_data='pora18')
        ],
        [
            InlineKeyboardButton(text='Maryam😇',callback_data='pora19'),
            InlineKeyboardButton(text='Toha😇',callback_data='pora20'),
            InlineKeyboardButton(text='Anbiya😇',callback_data='pora21')
        ],
        [
            InlineKeyboardButton(text='Haj😇',callback_data='pora22'),
            InlineKeyboardButton(text="Mu'minun😇",callback_data='pora23'),
            InlineKeyboardButton(text='Nur😇',callback_data='pora24')
        ],
        [
            InlineKeyboardButton(text='Furqon😇',callback_data='pora25'),
            InlineKeyboardButton(text='Shuaro😇',callback_data='pora26'),
            InlineKeyboardButton(text='Naml😇',callback_data='pora27')
        ],
        [
            InlineKeyboardButton(text='Qosos😇',callback_data='pora28'),
            InlineKeyboardButton(text='Ankabut😇',callback_data='pora29'),
            InlineKeyboardButton(text='Rum😇',callback_data='pora30')
        ],
        [
            InlineKeyboardButton(text='Luqman😇',callback_data='pora31'),
            InlineKeyboardButton(text='Sajda😇',callback_data='pora32'),
            InlineKeyboardButton(text='Axzab😇',callback_data='pora33')
        ],
        [
            InlineKeyboardButton(text='Saba😇',callback_data='pora34'),
            InlineKeyboardButton(text='Fatir😇',callback_data='pora35'),
            InlineKeyboardButton(text='Yasin😇',callback_data='pora36')
        ],
        [
            InlineKeyboardButton(text='Soffat😇',callback_data='pora37'),
            InlineKeyboardButton(text='Sod😇',callback_data='pora38'),
            InlineKeyboardButton(text='Zumar😇',callback_data='pora39')
        ],
        [
            InlineKeyboardButton(text="G'ofir😇",callback_data='pora40'),
            InlineKeyboardButton(text='Fussilat😇',callback_data='pora41'),
            InlineKeyboardButton(text='Shuro😇',callback_data='pora42')
        ],
        [
            InlineKeyboardButton(text='Zuxruf😇',callback_data='pora43'),
            InlineKeyboardButton(text='Duxon😇',callback_data='pora44'),
            InlineKeyboardButton(text='Jasiyah😇',callback_data='pora45')
        ],
[
            InlineKeyboardButton(text='Ahqof😇',callback_data='pora46'),
            InlineKeyboardButton(text='Muhammad😇',callback_data='pora47'),
            InlineKeyboardButton(text='Fath😇',callback_data='pora48'),
        ],
        [
            InlineKeyboardButton(text='Hujurot😇',callback_data='pora49'),
            InlineKeyboardButton(text="Qof😇",callback_data='pora50'),
            InlineKeyboardButton(text="Zariyat😇",callback_data='pora51'),
            ],
        [
            InlineKeyboardButton(text="Tur😇",callback_data='pora52'),
            InlineKeyboardButton(text='Najm😇',callback_data='pora53'),
            InlineKeyboardButton(text='Qomar😇',callback_data='pora54'),
        ],

        [
            InlineKeyboardButton(text='Ar Rohman😇',callback_data='pora55'),
            InlineKeyboardButton(text='Vaqia😇',callback_data='pora56'),
            InlineKeyboardButton(text='Hadid😇',callback_data='pora57')
        ],
        [
            InlineKeyboardButton(text='Mujodala😇',callback_data='pora58'),
            InlineKeyboardButton(text='Hashr😇',callback_data='pora59'),
            InlineKeyboardButton(text='Mumtahana😇',callback_data='pora60')
        ],
        [
            InlineKeyboardButton(text='Soff😇',callback_data='pora61'),
            InlineKeyboardButton(text="Jumu'a😇",callback_data='pora62'),
            InlineKeyboardButton(text='Munafiqun😇',callback_data='pora63')
        ],
        [
            InlineKeyboardButton(text="Tag'obun😇",callback_data='pora64'),
            InlineKeyboardButton(text='Tolaq😇',callback_data='pora65'),
            InlineKeyboardButton(text='Tahrim😇',callback_data='pora66')
        ],
        [
            InlineKeyboardButton(text='Mulk😇',callback_data='pora67'),
            InlineKeyboardButton(text="Qolam😇",callback_data='pora68'),
            InlineKeyboardButton(text='Haqqoh😇',callback_data='pora69')
        ],
        [
            InlineKeyboardButton(text="Ma'arij😇",callback_data='pora70'),
            InlineKeyboardButton(text='Nuh😇',callback_data='pora71'),
            InlineKeyboardButton(text='Jin😇',callback_data='pora72')
        ],
        [
            InlineKeyboardButton(text='Muzzammil😇',callback_data='pora73'),
            InlineKeyboardButton(text='Muddasir😇',callback_data='pora74'),
            InlineKeyboardButton(text='Qiyamah😇',callback_data='pora75')
        ],
        [
            InlineKeyboardButton(text='Insan😇',callback_data='pora76'),
            InlineKeyboardButton(text='Mursalat😇',callback_data='pora77'),
            InlineKeyboardButton(text='Naba😇',callback_data='pora78')
        ],
        [
            InlineKeyboardButton(text='Naziat😇',callback_data='pora79'),
            InlineKeyboardButton(text='Abasa😇',callback_data='pora80'),
            InlineKeyboardButton(text='Takvir😇',callback_data='pora81')
        ],
        [
            InlineKeyboardButton(text='Intifor😇',callback_data='pora82'),
            InlineKeyboardButton(text='Mutoffifun😇',callback_data='pora83'),
            InlineKeyboardButton(text='Inshiqoq😇',callback_data='pora84')
        ],
        [
            InlineKeyboardButton(text="Buruj😇",callback_data='pora85'),
            InlineKeyboardButton(text='Toriq😇',callback_data='pora86'),
            InlineKeyboardButton(text="A'la😇",callback_data='pora87')
        ],
        [
            InlineKeyboardButton(text="G'oshiyah😇",callback_data='pora88'),
            InlineKeyboardButton(text='Fajr😇',callback_data='pora89'),
            InlineKeyboardButton(text='Balad😇',callback_data='pora90')
        ],
[
            InlineKeyboardButton(text='Shams😇',callback_data='pora91'),
            InlineKeyboardButton(text='Layl😇',callback_data='pora92'),
            InlineKeyboardButton(text='Zuho😇',callback_data='pora93'),
        ],
        [
            InlineKeyboardButton(text='Sharh😇',callback_data='pora94'),
            InlineKeyboardButton(text="Tiyn😇",callback_data='pora95'),
            InlineKeyboardButton(text="Alaq😇",callback_data='pora96'),
            ],
        [
            InlineKeyboardButton(text="Qadr😇",callback_data='pora97'),
            InlineKeyboardButton(text='Bayyina😇',callback_data='pora98'),
            InlineKeyboardButton(text='Zalzala😇',callback_data='pora99'),
        ],


        [


        ],




    ],



)
al_afasiy2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Adiyat☪️', callback_data='pora100'),
            InlineKeyboardButton(text='Qoriya☪️', callback_data='pora101'),
            InlineKeyboardButton(text='Takasur☪️', callback_data='pora102')
        ],
        [
            InlineKeyboardButton(text='Asr☪️', callback_data='pora103'),
            InlineKeyboardButton(text='Humaza☪️', callback_data='pora104'),
            InlineKeyboardButton(text='Fil☪️', callback_data='pora105')
        ],
        [
            InlineKeyboardButton(text='Quraysh☪️', callback_data='pora106'),
            InlineKeyboardButton(text="Ma'un☪️", callback_data='pora107'),
            InlineKeyboardButton(text='Kavsar☪️', callback_data='pora108')
        ],
        [
            InlineKeyboardButton(text='Kafirun☪️ va Nasr☪️', callback_data='pora109'),
            InlineKeyboardButton(text='Masad☪️', callback_data='pora110'),


        ],
        [
            InlineKeyboardButton(text='Ixlos☪️ va Falaq☪️', callback_data='pora111'),
        ],
        [
            InlineKeyboardButton(text='Nas☪️', callback_data='pora112'),
            InlineKeyboardButton(text='Ulashish☪️', switch_inline_query='')
        ]
    ]
)
keying_sahifa =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Keyingi sahifa'),
            KeyboardButton(text="🔙 Orqaga")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(text='🎙Mishari Rashid Al Afasiy')
async def echo_bot(message  : types.Message):
    await bot.send_photo(chat_id=message.from_user.id,photo='https://cdns-images.dzcdn.net/images/artist/bad685cc810fc6a0333e72528ec228a4/500x500.jpg')
    await message.answer(f"Siz ushbu bo'limda mashxur qori Mishari Rashid Al Afasiyning qiroatlaridan baxramand bo'lasiz!\n \n"
"Quyidagi suralardan tinglamoqchi bo'lgan surangizni topishingiz mumkin!🕌",reply_markup=al_afasiy)
    await message.answer("Keyingi Suralarga o'tish uchun Keyingi sahifa tugmasini bosing☪️",reply_markup=keying_sahifa)

@dp.message_handler(text='Keyingi sahifa')
async def echo_bot(message: types.Message):
    await message.answer("Siz ushbu bo'limda mashxur qori Mishari Rashid Al Afasiyning qiroatlaridan baxramand bo'lasiz!😊",reply_markup=al_afasiy2)


@dp.message_handler(text="🔙 Orqaga4")
async def orqaga(message : types.Message):
    await message.answer(f"Ushbu bo'limda siz eng mashxur qorilarning barcha audio shakldagi 30 pora qiroatlarini topasiz In Sha Alloh!🕌",reply_markup=pora30_button)