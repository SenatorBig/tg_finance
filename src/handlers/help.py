from aiogram import types
from loader import dp


@dp.message_handler(commands="help")
async def help_command(message: types.Message):
    await message.answer("Позже расписать")
