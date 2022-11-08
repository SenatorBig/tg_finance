from aiogram import Bot, Dispatcher, executor, types
import logging
from tg_backend.models import Session
from aiogram.dispatcher import FSMContext

from settings import API_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from tg_backend.models import User

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

new_user = User()
@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    if user:
        await message.answer(f"Hi, {user.name}")
    else:
        name = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=f"{message.from_user.first_name}")
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await message.answer("Hi!\nI'm FinanceBot!\n Enter your name!", reply_markup=name)


@dp.message_handler()
async def get_name(message: types.Message, state: FSMContext):
    session = Session()
    user = User(name=message.text, chat_id=message.from_user.id)
    session.add(user)
    session.commit()
    currency = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="USD"),
                KeyboardButton(text="RUB"),
                KeyboardButton(text="GEL")
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f"{message.text}, enter your currency:", reply_markup=currency)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)