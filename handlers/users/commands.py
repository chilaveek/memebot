import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import admins
from data.peewee import Human, Words
from keyboards.default.menu import menu_kb
from loader import dp
from states.list_append import ListOperations
from states.start_test import StartTest


@dp.message_handler(Command('menu'))
async def menu_show(message: types.Message):
    await message.answer('У тебя что, меню закрылось? Жесть, ну тогда верну', reply_markup=menu_kb)


@dp.message_handler(Command('name'))
async def name_change(message: types.Message):
    await message.answer('Хочешь сменить имя? Хорошо, тогда следующим предложением напиши мне, как тебя называть')
    await StartTest.name_change.set()


@dp.message_handler(state=StartTest.name_change)
async def name_change_final(message: types.Message, state: FSMContext):
    name = message.text
    human = Human.get(id=message.from_user.id)
    human.name = name
    human.save()
    await message.answer(text=f'Теперь буду называть тебя {human.name}... Скрываешься от кого-то?')
    await state.finish()


@dp.message_handler(Command('new'))
async def append(message: types.Message):
    human = Human.get(id=message.from_user.id)
    if human.id in admins:
        await message.answer(text='круто, админчик. Пришли одну (пока что) фразу для добавления в следующем сообщении')
        await ListOperations.append.set()


@dp.message_handler(Command('words'))
async def append(message: types.Message):
    human = Human.get(id=message.from_user.id)

    if human.id in admins:
        open('base.txt', 'w').close()
        i = 0

        for word in Words.select():
            i += 1
            file_base = open('base.txt', 'a+')
            file_base.write('\n ' + ' ' + str(i) + '. ' + word.phrase)
            file_base.close()

        await message.answer_document(document=open('base.txt', 'rb'), caption='<b>ВСЕГО ФРАЗ: ' + str(i) + '</b>')


@dp.message_handler(Command('users'))
async def users(message: types.Message):
    admin = Human.get(id=message.from_user.id)
    if admin.id in admins:
        open('users.txt', 'w').close()
        i = 0
        for user in Human.select():
            i += 1
            human = Human.get(id=user.id)
            file_users = open('users.txt', 'a+')
            file_users.write('\n\nid: ' + str(
                human.id) + ', username: @' + human.username + ', name: ' + human.name + ', age: ' \
                             + str(human.age))

        await message.answer_document(document=open('users.txt', 'rb'), caption='<b>ВСЕГО ЮЗЕРОВ: ' + str(i) + '</b>')


@dp.message_handler(state=ListOperations.append)
async def list_append(message: types.Message, state: FSMContext):
    msg = message.text
    i = 0
    Words.create(phrase=msg)
    await message.answer(text='Добавлено успешно!')
    await state.finish()


@dp.message_handler(Command('help_admins'))
async def help_admins(message: types.Message):
    admin = Human.get(id=message.from_user.id)
    if admin.id in admins:
        await message.answer(text=f'Серьёзно? Ты, {admin.name}, админ и не знаешь свои команды наизусть??!'
                                  f'\n---\n'
                                  f'\n/words - Список фраз для демотиватора'
                                  f'\n/new - Добавить <b>одну</b> фразу'
                                  f'\n/users - Список Юзеров бота со статистикой'
                                  f'\n/delword - Удаление <b>одной</b> фразы. Следующим сообщением нужно указать '
                                  f'его номер в списке по команде /words'
                             )
    else:
        await message.answer(text='Вы прекрасны сами по себе, но админом бота не являетесь... Можете попробовать '
                                  'дописаться до владельца, если так хочется')


@dp.message_handler(Command('delword'))
async def users(message: types.Message):
    admin = Human.get(id=message.from_user.id)
    if admin.id in admins:
        await message.answer('Отлично, админчик, теперь укажи номер фразы из списка /words . '
                             '\n---\nЕсли команда введена случайно, напиши че нибудь текстом и всё, ок?')
        await ListOperations.delete.set()


@dp.message_handler(state=ListOperations.delete)
async def delete_word(message: types.Message, state: FSMContext):
    index = message.text
    q = 0
    for phrase in Words.select():
        q += 1

    if index.isdigit() is True:
        if int(index) <= q:
            delword = Words.get(id_primary=index)
            delword.delete_instance()
            await message.answer(text='Прекрасно, админчик, ты удалил слово под индексом ' + str(index))
        else:
            await message.answer(
                text='Ошибочка произшла в указании индекса (число больше размера списка), если так надо, введите команду /delword ещё раз')
    else:
        await message.answer(
            text='Ошибочка произшла в указании индекса, если нужно, введите команду /delword ещё раз и индекс укажите числом')

    await state.finish()
