from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.database import Purchase, Category, Store
from handlers.services.general_states import HandlersMessages
from handlers.services.keyboards import stores_keyboard, categories_keyboard, menu_keyboard
from handlers.services.decorators import inject_user_and_session


@dp.message_handler(state=HandlersMessages.new_buy)
async def create_new_purchase(message: types.Message):
    await message.answer("Enter the product name")
    await HandlersMessages.add_title.set()


@dp.message_handler(state=HandlersMessages.add_title)
@inject_user_and_session
async def enter_title_purchase(message: types.Message, session, user, state: FSMContext):
    await state.update_data(user_id=user.id, title=message.text)
    await message.answer("Enter the price. Example 99.99")
    await HandlersMessages.add_price.set()


@dp.message_handler(state=HandlersMessages.add_price)
@inject_user_and_session
async def enter_price(message: types.Message, session, user, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("Enter valid price. Example 99.99")
        return
    categories = session.query(Category).filter_by(user_id=user.id)
    await state.update_data(price=price)
    await message.answer(
        "Select a product category or create a new one",
        reply_markup=categories_keyboard(categories)
    )
    await HandlersMessages.select_category.set()


@dp.message_handler(state=HandlersMessages.select_category)
@inject_user_and_session
async def select_category_purchase(message: types.Message, session, user, state: FSMContext):
    if message.text == "New category":
        await message.answer("Enter the title of new category")
        await HandlersMessages.create_category.set()
    else:
        stores = session.query(Store).filter_by(user_id=user.id)
        categories = session.query(Category).filter_by(user_id=user.id)
        if message.text not in [category.title for category in categories]:
            await message.answer("Please, select category from keyboard")
            return
        await message.answer(
            "Select a store or create a new one",
            reply_markup=stores_keyboard(stores)
        )
        await state.update_data(category=message.text, new_category=False)
        await HandlersMessages.select_store.set()


@dp.message_handler(state=HandlersMessages.create_category)
@inject_user_and_session
async def create_new_category(message: types.Message, session, user, state: FSMContext):
    category = Category(title=message.text, user_id=user.id)
    session.add(category)
    stores = session.query(Store).filter_by(user_id=user.id)
    await message.answer(
        "Select a store or create a new one",
        reply_markup=stores_keyboard(stores)
    )
    await state.update_data(category=message.text)
    await HandlersMessages.select_store.set()


@dp.message_handler(state=HandlersMessages.select_store)
@inject_user_and_session
async def add_store(message: types.Message, session, user, state: FSMContext):
    if message.text == "New store":
        await message.answer("Enter the title store")
        await HandlersMessages.create_store.set()
    else:
        stores = session.query(Store).filter_by(user_id=user.id)
        if message.text not in [store.title for store in stores]:
            await message.answer("Please, select store from keyboard")
            return
        await state.update_data(store=message.text, new_store=False)
        data = await state.get_data()
        store = session.query(Store).filter_by(user_id=user.id, title=data["store"]).first()
        category = session.query(Category).filter_by(user_id=user.id, title=data["category"]).first()
        purchase = Purchase(
            title=data["title"], user_id=user.id, price=data["price"], category_id=category.id, store_id=store.id
        )
        session.add(purchase)
        text = f"Title: {data['title']} \nPrice: {data['price']} \nCategory: {data['category']} \nStore: {data['store']}"
        await message.answer(text)
        await message.answer("What do you want?", reply_markup=menu_keyboard)
        await HandlersMessages.menu_select.set()


@dp.message_handler(state=HandlersMessages.create_store)
@inject_user_and_session
async def create_new_store(message: types.Message, session, user, state: FSMContext):
    await state.update_data(store=message.text, new_store=True)
    data = await state.get_data()
    store = Store(title=message.text, user_id=user.id)
    session.add(store)
    session.commit()
    store_id = store.id
    category = session.query(Category).filter_by(user_id=user.id, title=data["category"]).first()
    purchase = Purchase(title=data["title"], price=data["price"], category_id=category.id, store_id=store_id)
    session.add(purchase)
    session.commit()
    text = f"Title: {data['title']} \nPrice: {data['price']} \nCategory: {data['category']} \nStore: {data['store']}"
    await message.answer(text)
    await message.answer("What do you want?", reply_markup=menu_keyboard)
    await HandlersMessages.menu_select.set()
