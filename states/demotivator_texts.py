from aiogram.dispatcher.filters.state import StatesGroup, State


class DemotivatorText(StatesGroup):
    text1 = State()
    text2 = State()
