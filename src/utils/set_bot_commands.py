from aiogram import types

# todo файл должен быть назван как существительное
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Starting bot"),
            types.BotCommand("help", "Help"),
            types.BotCommand("register", "Sign up")
        ]
    )