from aiogram.dispatcher.filters.state import StatesGroup, State

class ListAppend(StatesGroup):
    msg = State()