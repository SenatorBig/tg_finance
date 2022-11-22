from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def stores_keyboard(stores):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.insert("New store")
    if list(stores):
        for store in stores:
            keyboard.insert(str(store.title))
    return keyboard


def categories_keyboard(categories):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.insert("New category")
    if list(categories):
        for category in categories:
            keyboard.insert(str(category.title))
    return keyboard


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Cost analysis"),
            KeyboardButton(text="2. Purchases"),
            KeyboardButton(text="3. Balance"),
            KeyboardButton(text="4. Info")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


answer_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


currency_keyboard = ReplyKeyboardMarkup(
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
