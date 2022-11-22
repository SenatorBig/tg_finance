from aiogram.dispatcher.filters.state import StatesGroup, State


class HandlersMessages(StatesGroup):
    """register states"""
    name_add = State()
    currency_add = State()
    overwrite = State()
    auto_redirect = State()
    """purchase_states"""
    new_buy = State()
    add_title = State()
    add_price = State()
    select_store = State()
    select_category = State()
    create_category = State()
    create_store = State()
    check_purchase_data = State()
    """menu_states"""
    menu_select = State()
    action = State()