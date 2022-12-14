from utils.set_bot_commands import set_default_commands
from aiogram import executor
import handlers
from loader import dp


async def on_startup(dp):
    await set_default_commands(dp)
    print("Bot started")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    