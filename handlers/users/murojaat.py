from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.tas_bek import tas_bek
from loader import dp,bot
from states.holatlar import Forma


# Echo bot
@dp.message_handler(text="Adminga murojaat✍️")
async def bot_echo(message: types.Message):
    await message.answer(text="ILTIMOS TAKLIFINGIZNI QISQA VA TUSHUNARLI QILIB YOZING..✓")
    await Forma.murojat.set()

@dp.message_handler(state=Forma.murojat)
async def bot_echo(message: types.Message,state:FSMContext):
    text = message.text
    user_id = message.from_user.id
    await state.update_data({"matn": text})
    user_malumotlari = await state.get_data()
    murojat= user_malumotlari.get("matn")
    id = user_id
    b =  f"Murojaatingiz Agar Tog'ri bo'lsa Tasdiqlashni bosing👌\n" \
         f"Aks holda Bekor qilishni bosing\n\n  {murojat} "
    await bot.send_message(chat_id=user_id,text=b,reply_markup=tas_bek)
    await Forma.tasdiqlash.set()

@dp.callback_query_handler(state=Forma.tasdiqlash,text="tasdiqlash")
async def bot_echo(message: CallbackQuery, state: FSMContext):
    user_malumotlari = await state.get_data()
    user_id = message.from_user.id
    username = message.from_user.username
    murojat = user_malumotlari.get("matn")
    b =  f"👉 Murojaat  :{murojat} \n" \
         f" id : {user_id}\n" \
         f"username : @{username}"
    await bot.send_message(chat_id=f"917782961",text=b)
    await bot.send_message(text="Adminga yuborildi",chat_id=message.from_user.id)
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash,text="Bekor qilish")
async def bot_echo(message: types.message, state: FSMContext):
    await message.answer(text="Bekor qilindi ",reply_markup=yonalishlar_button)
    await state.finish()
