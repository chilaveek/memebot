from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.peewee import Human
from keyboards.default.menu import menu_kb
from loader import dp


class StartTest(StatesGroup):
    name = State()
    age = State()
    name_change = State()

@dp.message_handler(state=StartTest.name)
async def name_save(message: types.Message):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()

    await message.answer(
        text=f'Какое красивое имя, <b>{human.name}</b>! Смена имени кстати возможна по команде /name \n'
             f'Теперь разберёмся с твоим возрастом, сколько тебе лет?')



@dp.message_handler(state=StartTest.name_change)
async def name_change_final(message: types.Message, state: FSMContext):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()
    await message.answer(text=f'Теперь буду называть тебя {human.name}... Скрываешься от кого-то?')
    await state.finish()