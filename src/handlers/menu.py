from handlers.services.general_states import HandlersMessages
from loader import dp
from handlers.services import sting_vars
from handlers.services import keyboards as kb
from aiogram import types


@dp.message_handler(state=HandlersMessages.menu_select)
async def call_menu(message: types.Message):
    if message.text == sting_vars.menu_purchase:
        await message.answer("Enter the product name")
        await HandlersMessages.add_title.set()
    if message.text == sting_vars.menu_analysis:
        await message.answer("link to site")
        await message.answer("What do you want?", reply_markup=kb.menu_keyboard)
    if message.text == sting_vars.menu_categories:
        await message.answer("Categories settings", reply_markup=kb.categories_menu_keyboard)
