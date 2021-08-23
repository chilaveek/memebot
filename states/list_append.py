from aiogram.dispatcher.filters.state import StatesGroup, State

class ListOperations(StatesGroup):
    append = State()
    delete = State()