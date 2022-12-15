from aiogram.dispatcher.filters.state import StatesGroup, State


class HandlersMessages(StatesGroup):
    # register states
    name_add = State()
    currency_add = State()
    overwrite = State()
    auto_redirect = State()

    # menu states
    menu_select = State()
    action = State()

    # purchase states
    new_buy = State()
    add_title = State()
    add_price = State()
    select_store = State()
    select_category = State()
    create_category = State()
    create_store = State()
    check_purchase_data = State()

    # categories states
    categories_menu = State()
    new_category = State()
    add_store_to_category = State()

