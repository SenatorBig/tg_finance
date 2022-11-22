from utils.set_bot_commands import set_default_commands
from aiogram import executor


async def on_startup(dp):
    await set_default_commands(dp)
    print("Bot started")


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)