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
    await StartTest.age.set()


@dp.message_handler(state=StartTest.age)
async def age_save(message: types.Message, state=FSMContext):
    age = message.text
    human = Human.get(id=message.from_user.id)

    if age.isdigit() is True:
        human.age = age
        human.save()
        await message.answer(text=f'Благодарю за искренность, {human.name}! '
                                  f'Тебе наверное уже не терпится создать свой первый мэм?',
                             reply_markup=menu_kb)
        await state.finish()

    else:
        await message.answer('Похоже, ты прислал символы или число, содержащее символы. Напиши-ка ещё раз свой возраст')
        await StartTest.age.set()


@dp.message_handler(state=StartTest.name_change)
async def name_change_final(message: types.Message, state: FSMContext):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()
    await message.answer(text=f'Теперь буду называть тебя {human.name}... Скрываешься от кого-то?')
    await state.finish()