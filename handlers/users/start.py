from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.peewee import Human
from keyboards.default.menu import menu_kb
from keyboards.inline.inline_kb import start_kb, start_btn_yes
from loader import dp
from states.start_test import StartTest


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    Human.get_or_create(id=message.from_user.id, username=message.from_user.username)
    await message.answer(f'Приветствую! Как я могу к тебе обращаться?')

    await StartTest.name.set()

@dp.message_handler(state=StartTest.name)
async def name_save(message: types.Message):

    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()

    await message.answer(text=f'Приятно, познакомиться, {human.name}! Смена имени кстати возможна по команде /name \n'
                                 f'Теперь разберёмся с твоим возрастом, сколько тебе лет?', reply_markup=menu_kb)
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
                            reply_markup=start_kb)
        await state.finish()

    else:
        await message.answer('Похоже, вы прислали символы или число, содержащее символы. Напишите ещё раз свой возраст')
        await StartTest.age.set()





@dp.callback_query_handler(text='no_start')
async def no_start(call: CallbackQuery):
    await call.message.edit_text(text='Уууоууу, меня кажется вырубило как раз, когда ты нажал на кнопку. '
                                      'Так тебе не терпится создать свой первый мэм?',
                                 reply_markup=start_btn_yes)

@dp.callback_query_handler(text='yes_start')
async def yes_start(call: CallbackQuery):
    await call.message.edit_text(text='Ура! Тогда начнём!')