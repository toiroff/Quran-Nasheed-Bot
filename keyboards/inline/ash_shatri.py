from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery

from keyboards.default.pora30 import pora30_button
from loader import dp, bot

al_dossari=InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text='Fotiha😇',callback_data='ash1'),
            InlineKeyboardButton(text='Baqoro😇',callback_data='ash2'),
            InlineKeyboardButton(text='Oli imron😇',callback_data='ash3'),
        ],
        [
            InlineKeyboardButton(text='Nisa😇',callback_data='ash4'),
            InlineKeyboardButton(text="Ma'ida😇",callback_data='ash5'),
            InlineKeyboardButton(text="An'am😇",callback_data='ash6'),
            ],
        [
            InlineKeyboardButton(text="Ar'of😇",callback_data='ash7'),
            InlineKeyboardButton(text='Anfal😇',callback_data='ash8'),
            InlineKeyboardButton(text='Tavba😇',callback_data='ash9'),
        ],

        [
            InlineKeyboardButton(text='Yunus😇',callback_data='ash10'),
            InlineKeyboardButton(text='Hud😇',callback_data='ash11'),
            InlineKeyboardButton(text='Yusuf😇',callback_data='ash12')
        ],
        [
            InlineKeyboardButton(text="Ra'd😇",callback_data='ash13'),
            InlineKeyboardButton(text='Ibrohim😇',callback_data='ash14'),
            InlineKeyboardButton(text='Hijr😇',callback_data='ash15')
        ],
        [
            InlineKeyboardButton(text='Nahl😇',callback_data='ash16'),
            InlineKeyboardButton(text='Isro😇',callback_data='ash17'),
            InlineKeyboardButton(text='Kahf😇',callback_data='ash18')
        ],
        [
            InlineKeyboardButton(text='Maryam😇',callback_data='ash19'),
            InlineKeyboardButton(text='Toha😇',callback_data='ash20'),
            InlineKeyboardButton(text='Anbiya😇',callback_data='ash21')
        ],
        [
            InlineKeyboardButton(text='Haj😇',callback_data='ash22'),
            InlineKeyboardButton(text="Mu'minun😇",callback_data='ash23'),
            InlineKeyboardButton(text='Nur😇',callback_data='ash24')
        ],
        [
            InlineKeyboardButton(text='Furqon😇',callback_data='ash25'),
            InlineKeyboardButton(text='Shuaro😇',callback_data='ash26'),
            InlineKeyboardButton(text='Naml😇',callback_data='ash27')
        ],
        [
            InlineKeyboardButton(text='Qosos😇',callback_data='ash28'),
            InlineKeyboardButton(text='Ankabut😇',callback_data='ash29'),
            InlineKeyboardButton(text='Rum😇',callback_data='ash30')
        ],
        [
            InlineKeyboardButton(text='Luqman😇',callback_data='ash31'),
            InlineKeyboardButton(text='Sajda😇',callback_data='ash32'),
            InlineKeyboardButton(text='Axzab😇',callback_data='ash33')
        ],
        [
            InlineKeyboardButton(text='Saba😇',callback_data='ash34'),
            InlineKeyboardButton(text='Fatir😇',callback_data='ash35'),
            InlineKeyboardButton(text='Yasin😇',callback_data='ash36')
        ],
        [
            InlineKeyboardButton(text='Soffat😇',callback_data='ash37'),
            InlineKeyboardButton(text='Sod😇',callback_data='ash38'),
            InlineKeyboardButton(text='Zumar😇',callback_data='ash39')
        ],
        [
            InlineKeyboardButton(text="G'ofir😇",callback_data='ash40'),
            InlineKeyboardButton(text='Fussilat😇',callback_data='ash41'),
            InlineKeyboardButton(text='Shuro😇',callback_data='ash42')
        ],
        [
            InlineKeyboardButton(text='Zuxruf😇',callback_data='ash43'),
            InlineKeyboardButton(text='Duxon😇',callback_data='ash44'),
            InlineKeyboardButton(text='Jasiyah😇',callback_data='ash45')
        ],
[
            InlineKeyboardButton(text='Ahqof😇',callback_data='ash46'),
            InlineKeyboardButton(text='Muhammad😇',callback_data='ash47'),
            InlineKeyboardButton(text='Fath😇',callback_data='ash48'),
        ],
        [
            InlineKeyboardButton(text='Hujurot😇',callback_data='ash49'),
            InlineKeyboardButton(text="Qof😇",callback_data='ash50'),
            InlineKeyboardButton(text="Zariyat😇",callback_data='ash51'),
            ],
        [
            InlineKeyboardButton(text="Tur😇",callback_data='ash52'),
            InlineKeyboardButton(text='Najm😇',callback_data='ash53'),
            InlineKeyboardButton(text='Qomar😇',callback_data='ash54'),
        ],

        [
            InlineKeyboardButton(text='Ar Rohman😇',callback_data='ash55'),
            InlineKeyboardButton(text='Vaqia😇',callback_data='ash56'),
            InlineKeyboardButton(text='Hadid😇',callback_data='ash57')
        ],
        [
            InlineKeyboardButton(text='Mujodala😇',callback_data='ash58'),
            InlineKeyboardButton(text='Hashr😇',callback_data='ash59'),
            InlineKeyboardButton(text='Mumtahana😇',callback_data='ash60')
        ],
        [
            InlineKeyboardButton(text='Soff😇',callback_data='ash61'),
            InlineKeyboardButton(text="Jumu'a😇",callback_data='ash62'),
            InlineKeyboardButton(text='Munafiqun😇',callback_data='ash63')
        ],
        [
            InlineKeyboardButton(text="Tag'obun😇",callback_data='ash64'),
            InlineKeyboardButton(text='Tolaq😇',callback_data='ash65'),
            InlineKeyboardButton(text='Tahrim😇',callback_data='ash66')
        ],
        [
            InlineKeyboardButton(text='Mulk😇',callback_data='ash67'),
            InlineKeyboardButton(text="Qolam😇",callback_data='ash68'),
            InlineKeyboardButton(text='Haqqoh😇',callback_data='ash69')
        ],
        [
            InlineKeyboardButton(text="Ma'arij😇",callback_data='ash70'),
            InlineKeyboardButton(text='Nuh😇',callback_data='ash71'),
            InlineKeyboardButton(text='Jin😇',callback_data='ash72')
        ],
        [
            InlineKeyboardButton(text='Muzzammil😇',callback_data='ash73'),
            InlineKeyboardButton(text='Muddasir😇',callback_data='ash74'),
            InlineKeyboardButton(text='Qiyamah😇',callback_data='ash75')
        ],
        [
            InlineKeyboardButton(text='Insan😇',callback_data='ash76'),
            InlineKeyboardButton(text='Mursalat😇',callback_data='ash77'),
            InlineKeyboardButton(text='Naba😇',callback_data='ash78')
        ],
        [
            InlineKeyboardButton(text='Naziat😇',callback_data='ash79'),
            InlineKeyboardButton(text='Abasa😇',callback_data='ash80'),
            InlineKeyboardButton(text='Takvir😇',callback_data='ash81')
        ],
        [
            InlineKeyboardButton(text='Intifor😇',callback_data='ash82'),
            InlineKeyboardButton(text='Mutoffifun😇',callback_data='ash83'),
            InlineKeyboardButton(text='Inshiqoq😇',callback_data='ash84')
        ],
        [
            InlineKeyboardButton(text="Buruj😇",callback_data='ash85'),
            InlineKeyboardButton(text='Toriq😇',callback_data='ash86'),
            InlineKeyboardButton(text="A'la😇",callback_data='ash87')
        ],
        [
            InlineKeyboardButton(text="G'oshiyah😇",callback_data='ash88'),
            InlineKeyboardButton(text='Fajr😇',callback_data='ash89'),
            InlineKeyboardButton(text='Balad😇',callback_data='ash90')
        ],
[
            InlineKeyboardButton(text='Shams😇',callback_data='ash91'),
            InlineKeyboardButton(text='Layl😇',callback_data='ash92'),
            InlineKeyboardButton(text='Zuho😇',callback_data='ash93'),
        ],
        [
            InlineKeyboardButton(text='Sharh😇',callback_data='ash94'),
            InlineKeyboardButton(text="Tiyn😇",callback_data='ash95'),
            InlineKeyboardButton(text="Alaq😇",callback_data='ash96'),
            ],
        [
            InlineKeyboardButton(text="Qadr😇",callback_data='ash97'),
            InlineKeyboardButton(text='Bayyina😇',callback_data='ash98'),
            InlineKeyboardButton(text='Zalzala😇',callback_data='ash99'),
        ],


        [


        ],




    ],



)
al_d2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Adiyat☪️', callback_data='ash100'),
            InlineKeyboardButton(text='Qoriya☪️', callback_data='ash101'),
            InlineKeyboardButton(text='Takasur☪️', callback_data='ash102')
        ],
        [
            InlineKeyboardButton(text='Asr☪️', callback_data='ash103'),
            InlineKeyboardButton(text='Humaza☪️', callback_data='ash104'),
            InlineKeyboardButton(text='Fil☪️', callback_data='ash105')
        ],
        [
            InlineKeyboardButton(text='Quraysh☪️', callback_data='ash106'),
            InlineKeyboardButton(text="Ma'un☪️", callback_data='ash107'),
            InlineKeyboardButton(text='Kavsar☪️', callback_data='ash108')
        ],
        [
            InlineKeyboardButton(text='Kafirun☪️ va Nasr☪️', callback_data='ash109'),
            InlineKeyboardButton(text='Masad☪️', callback_data='ash110'),


        ],
        [
            InlineKeyboardButton(text='Ixlos☪️ va Falaq☪️', callback_data='ash111'),
        ],
        [
            InlineKeyboardButton(text='Nas☪️', callback_data='ash112'),
            InlineKeyboardButton(text='Ulashish☪️', switch_inline_query='')
        ]
    ]
)
keying_sahifa =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Keyingi sahifa😇'),
            KeyboardButton(text="🔙 Orqaga")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(text='🎙Abu-Bakr Ash-Shatri')
async def echo_bot(message  : types.Message):
    await bot.send_photo(chat_id=message.from_user.id,photo='https://static.qurancdn.com/images/reciters/3/abu-bakr-al-shatri-pofile.jpeg?v=1')
    await message.answer(f"Siz ushbu bo'limda mashxur qori 🎙Abu-Bakr Ash-Shatrining qiroatlaridan baxramand bo'lasiz!\n \n"
"Quyidagi suralardan tinglamoqchi bo'lgan surangizni topishingiz mumkin!🕌",reply_markup=al_dossari)
    await message.answer("Keyingi Suralarga o'tish uchun Keyingi sahifa tugmasini bosing☪️",reply_markup=keying_sahifa)
@dp.message_handler(text='Keyingi sahifa😇')
async def echo_bot(message: types.Message):
    await message.answer("Siz ushbu bo'limda mashxur qori 🎙Abu-Bakr Ash-Shatrining qiroatlaridan baxramand bo'lasiz!😊",reply_markup=al_d2)

@dp.message_handler(text='🔙 Orqaga')
async def echo_bot(message: types.Message):
    await message.answer(f"Ushbu bo'limda siz eng mashxur qorilarning barcha audio shakldagi 30 pora qiroatlarini topasiz In Sha Alloh!🕌",reply_markup=pora30_button)
