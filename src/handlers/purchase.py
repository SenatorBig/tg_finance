from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from utils.database import Session, User, Purchase, Category, Store
from handlers.services.general_states import HandlersMessages
from handlers.services.keyboards import stores_keyboard, categories_keyboard, menu_keyboard


@dp.message_handler(state=HandlersMessages.new_buy)
async def create_new_purchase(message: types.Message):
    await message.answer("Enter the product name")
    await HandlersMessages.add_title.set()


@dp.message_handler(state=HandlersMessages.add_title)
async def enter_title_purchase(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchase = Purchase(title=message.text, user_id=user.id)
    session.add(purchase)
    session.commit()
    await message.answer("Enter the price. Example 99.99")
    await HandlersMessages.add_price.set()


@dp.message_handler(state=HandlersMessages.add_price)
async def enter_price(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchases = session.query(Purchase).filter_by(user_id=user.id).order_by(Purchase.created_at)
    if list(purchases):
        purchase = list(purchases)[-1]
    try:
        purchase.price = float(message.text)
    except ValueError:
        await message.answer("Enter valid price. Example 99.99")
        return
    session.add(purchase)
    session.commit()
    categories = session.query(Category).filter_by(user_id=user.id)
    await message.answer(
        "Select a product category or create a new one",
        reply_markup=categories_keyboard(categories)
    )
    await HandlersMessages.select_category.set()


@dp.message_handler(state=HandlersMessages.select_category)
async def select_category_purchase(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchases = session.query(Purchase).filter_by(user_id=user.id).order_by(Purchase.created_at)
    purchase = list(purchases)[-1]
    if message.text == "New category":
        await message.answer("Enter the title of new category")
        await HandlersMessages.create_category.set()
    category = session.query(Category).filter_by(user_id=user.id, title=message.text).first()
    purchase.category_id = category.id
    session.add(purchase)
    session.commit()
    stores = session.query(Store).filter_by(user_id=user.id)
    await message.answer(
        "Select a category or create a new one",
        reply_markup=stores_keyboard(stores)
    )
    await HandlersMessages.select_store.set()


@dp.message_handler(state=HandlersMessages.create_category)
async def create_new_category(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchases = session.query(Purchase).filter_by(user_id=user.id).order_by(Purchase.created_at)
    purchase = list(purchases)[-1]
    category = Category(title=message.text, user_id=user.id)
    purchase.category_id = category.id
    session.add(category, purchase)
    session.commit()
    stores = session.query(Store).filter_by(user_id=user.id)
    await message.answer(
        "Select a category or create a new one",
        reply_markup=stores_keyboard(stores)
    )
    await HandlersMessages.select_store.set()


@dp.message_handler(state=HandlersMessages.select_store)
async def add_store(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchases = session.query(Purchase).filter_by(user_id=user.id).order_by(Purchase.created_at)
    purchase = list(purchases)[-1]
    if message.text == "New store":
        await message.answer("Enter the title store")
        await HandlersMessages.create_store.set()
    store = session.query(Store).filter_by(user_id=user.id, title=message.text).first()
    purchase.store_id = store.id
    session.add(purchase)
    session.commit()
    category = session.query(Category).filter_by(user_id=user.id, id=purchase.category_id).first()
    text = f"Title: {purchase.title} \nPrice: {purchase.price} \nCategory: {category.title} \nStore: {store.title}"
    await message.answer(text)
    await message.answer("What do you want?", reply_markup=menu_keyboard)
    await HandlersMessages.menu_select.set()


@dp.message_handler(state=HandlersMessages.create_store)
async def create_new_store(message: types.Message):
    session = Session()
    user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
    purchases = session.query(Purchase).filter_by(user_id=user.id).order_by(Purchase.created_at)
    if list(purchases):
        purchase = list(purchases)[-1]
    store = Store(title=message.text, user_id=user.id)
    purchase.store_id = store.id
    session.add(store, purchase)
    category = session.query(Category).filter_by(user_id=user.id, id=purchase.category_id).first()
    session.commit()
    text = f"Title: {purchase.title} \nPrice: {purchase.price} \nCategory: {category.title} \nStore: {store.title}"
    await message.answer(text)
    await message.answer("What do you want?", reply_markup=menu_keyboard)
    await HandlersMessages.menu_select.set()
