from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.peewee import Human
from keyboards.default.menu import menu_kb
from loader import dp
from states.start_test import StartTest


@dp.message_handler(Command('menu'))
async def menu_show(message: types.Message):
    await message.answer('У вас что, меню закрылось? Жесть, ну тогда верну',reply_markup=menu_kb)

@dp.message_handler(Command('name'))
async def name_change(message: types.Message):
    await message.answer('Хотите сменить имя? Хорошо, тогда следующим предложением напишите мне, как вас называть')
    StartTest.name_change.set()

@dp.message_handler(state=StartTest.name_change)
async def name_change_final(message: types.Message, state: FSMContext):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()
    await message.answer(text=f'Теперь буду называть вас {human.name}... Скрываетесь от кого-то?')
    await state.finish()

