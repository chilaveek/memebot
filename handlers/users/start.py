from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.peewee import Human
from keyboards.default.menu import menu_kb
from keyboards.inline.inline_kb import start_kb, start_btn_yes
from loader import dp


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    Human.get_or_create(id=message.from_user.id, username=message.from_user.username, name=message.from_user.first_name)
    human = Human.get(id=message.from_user.id)
    await message.answer(f'Приветствую, {human.name}!', reply_markup=menu_kb)



