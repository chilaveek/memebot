from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import admins
from data.demotivator_words import words
from data.peewee import Human
from keyboards.default.menu import menu_kb
from loader import dp
from states.list_append import ListAppend
from states.start_test import StartTest


@dp.message_handler(Command('menu'))
async def menu_show(message: types.Message):
    await message.answer('У вас что, меню закрылось? Жесть, ну тогда верну',reply_markup=menu_kb)

@dp.message_handler(Command('name'))
async def name_change(message: types.Message):
    await message.answer('Хотите сменить имя? Хорошо, тогда следующим предложением напишите мне, как вас называть')
    await StartTest.name_change.set()

@dp.message_handler(state=StartTest.name_change)
async def name_change_final(message: types.Message, state: FSMContext):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()
    await message.answer(text=f'Теперь буду называть вас {human.name}... Скрываетесь от кого-то?')
    await state.finish()

@dp.message_handler(Command('new'))
async def append(message: types.Message):
    human = Human.get(id=message.from_user.id)
    if human.id in admins:
        await message.answer(text='круто, админчик. Пришли одну (пока что) фразу для добавления в следующем сообщении')
        await ListAppend.msg.set()

@dp.message_handler(Command('words'))
async def append(message: types.Message):
    human = Human.get(id=message.from_user.id)
    if human.id in admins:
        dem_words = 'Список фраз. Всего фраз: ' + str(len(words))
        for i in range(len(words)):
            dem_words += '\n ' + ' ' + str(i+1) + '. ' + words[i]
        await message.answer(text=dem_words)

@dp.message_handler(Command('users'))
async def users(message: types.Message):
    admin = Human.get(id=message.from_user.id)
    if admin.id in admins:
        users_message = 'Статистика по юзерам!'
        i = 0
        for user in Human.select():
            i += 1
            human = Human.get(id=user.id)
            users_message += '\nid: ' + str(human.id) + ', username: ' + human.username + ', name: ' + human.name + ', age: ' \
            + str(human.age)

        users_message += '\n\n<b>ВСЕГО ЮЗЕРОВ: ' + str(i) + '</b>'
        await message.answer(text=users_message)


@dp.message_handler(state=ListAppend.msg)
async def list_append(message: types.Message, state: FSMContext):
    msg = message.text
    words.append(msg)
    await message.answer(text='Добавлено успешно!')
    await state.finish()
