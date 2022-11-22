from handlers.services.general_states import HandlersMessages
from loader import dp

from aiogram import types

@dp.message_handler(state=HandlersMessages.menu_select)
async def call_menu(message: types.Message):
    if message.text == "2. Purchases":
        await message.answer("Enter the product name")
        await HandlersMessages.add_title.set()


