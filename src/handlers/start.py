from aiogram import types

from handlers.services.keyboards import menu_keyboard
from loader import dp
from utils.database import Session, User
from handlers.services.general_states import HandlersMessages


@dp.message_handler(commands="start")
@dp.message_handler(state=HandlersMessages.action)
async def start_command(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    if not user:
        await message.answer("Please, sign up!\nEnter your name")
        await HandlersMessages.name_add.set()
    else:
        await message.answer("What do you want?", reply_markup=menu_keyboard)
        await HandlersMessages.menu_select.set()
