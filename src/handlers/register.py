from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from handlers.services.keyboards import currency_keyboard, menu_keyboard, answer_keyboard
from loader import dp
from utils.database import Session, User, Category
from handlers.services.general_states import HandlersMessages


@dp.message_handler(commands="register")
async def register(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    if user:
        await message.answer(
            f"{user.name}, do you want to recreate your profile?",
            reply_markup=answer_keyboard
        )
        await HandlersMessages.overwrite.set()
    else:
        await message.answer("Enter your name!")
        await HandlersMessages.name_add.set()


@dp.message_handler(state=HandlersMessages.overwrite)
async def overwrite_user(message: types.Message, state: FSMContext):
    session = Session()
    if message.text == "Yes":
        user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
        session.delete(user)
        session.commit()
        await message.answer("Enter your name!")
        await HandlersMessages.name_add.set()
    else:
        await message.answer("Registration canceled")
        await state.finish()


@dp.message_handler(state=HandlersMessages.name_add)
async def get_name(message: types.Message, state: FSMContext):
    session = Session()
    state.proxy()
    user = User(name=message.text, chat_id=message.from_user.id)
    session.add(user)
    session.commit()
    await state.update_data(name_add=message.text)
    await message.answer(f"{message.text}, enter your currency:", reply_markup=currency_keyboard)
    await HandlersMessages.currency_add.set()


@dp.message_handler(state=HandlersMessages.currency_add)
async def get_currency(message: types.Message, state: FSMContext):
    if message.text not in ["USD", "RUB", "GEL"]:
        await message.answer("Choose from the proposed options")
        return
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    categories = ["groceries", "medicines", "transport"]
    for category in categories:
        new_category = Category(title=category, user_id=user.id)
        session.add(new_category)
    user.currency = message.text
    user.is_active = True
    session.add(user)
    session.commit()
    await state.update_data(currency_add=message.text)
    await message.answer("Success!")
    await message.answer("What do you want?", reply_markup=menu_keyboard)
    await HandlersMessages.menu_select.set()
