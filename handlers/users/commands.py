import os

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import Unauthorized

from data import config
from data.config import admins
from data.peewee import Human, Words
from keyboards.default.menu import menu_kb
from loader import dp
from states.list_append import ListOperations
from states.message_for_admins import MessageForAdmins
from states.message_for_all import MessageForAll
from states.start_test import StartTest


@dp.message_handler(Command('menu'))
async def menu_show(message: types.Message):
    await message.answer('У тебя что, меню закрылось? Жесть, ну тогда верну', reply_markup=menu_kb)


@dp.message_handler(Command('name'))
async def name_change(message: types.Message):
    await message.answer('Хочешь сменить имя? Хорошо, тогда следующим предложением напиши мне, как тебя называть')
    await StartTest.name_change.set()


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
        i = 0
        all_memes = 0
        for user in Human.select():
            i += 1

            human = Human.get(id=user.id)
            all_memes += human.memes

            if i == 1:
                file_users = open('users.txt', 'w')
                file_users.write('id: ' + str(
                human.id) + ', username: @' + human.username + ', name: ' + human.name + ', age: ' \
                             + str(human.age) + ', memes: ' + str(human.memes))

            file_users = open('users.txt', 'a+')
            file_users.write('\n\nid: ' + str(
                human.id) + ', username: @' + human.username + ', name: ' + human.name + ', age: ' \
                             + str(human.age) + ', memes: ' + str(human.memes))

        await message.answer_document(document=open('users.txt', 'rb'),
                                      caption='<b>ВСЕГО ЮЗЕРОВ: ' + str(i) + '</b>'
                                              '\n<b>ВСЕГО СДЕЛАННЫХ МЕМОВ\n(с 24.08.21, 19:30): ' + str(all_memes) + '</b>')



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



