from aiogram import types

from loader import dp, bot


@dp.message_handler(text="👨‍👩‍👧‍👦 Biz haqimizda")
async def bot_echo(message: types.Message):
    await message.reply(text=f" Bu botni dasturchi @UmarDeveloper hech qanday manfaatsiz, xolis niyatda yaratdi\n"
                              f"\n "
                              f"Bot sizga foyda bersa, biz xursandmiz! 😊 \n "
                              "‼️Ushbu botda reklama hizmati mavjud emas\n\n"
                              f" 🌐Rasmiy kanalimiz: @UmarDeveloper \n")