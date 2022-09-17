from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp

@dp.callback_query_handler(text='Dasturchi💻')
async def suralar(message:types.Message):
     await message.answer(text=f" Bu botni dasturchi @Harvard_Dev hech qanday manfaatsiz, xolis niyatda yaratdi\n"
                                       f"\n "
                                       f"Bot sizga foyda bersa, biz xursandmiz! 😊 \n "
                                       f"Barcha nashidalarni eshiting! Alloh o'zi qo'llasin🤲")


@dp.message_handler(text='Dasturchi💻')
async def suralar(message:types.Message):
     await message.answer(text=f" Bu botni dasturchi @UmarDeveloper hech qanday manfaatsiz, xolis niyatda yaratdi\n"
                                       f"\n "
                                       f"Bot sizga foyda bersa, biz xursandmiz! 😊 \n "
                                       f"Barcha nashidalarni eshiting! Alloh o'zi qo'llasin🤲")
