from handlers.services.general_states import HandlersMessages
from loader import dp
from handlers.services import sting_vars
from handlers.services import keyboards as kb
from aiogram import types


@dp.message_handler(state=HandlersMessages.menu_select)
async def call_menu(message: types.Message):
    if message.text == sting_vars.category_menu_create:
        await message.answer("Enter the category name")
        await HandlersMessages.add_title.set()
    if message.text == sting_vars.menu_analysis:
        await message.answer("Select category to delete")
    if message.text == sting_vars.category_menu_store:
        await message.answer("Select category to add store")
