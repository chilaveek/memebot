from aiogram.dispatcher.filters.state import StatesGroup, State


class StartTest(StatesGroup):
    name = State()
    age = State()
    name_change = State()
