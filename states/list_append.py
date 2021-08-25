from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import admins
from data.peewee import Human, Words
from loader import dp
from states.message_for_admins import MessageForAdmins


class ListOperations(StatesGroup):
    append = State()
    delete = State()

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


@dp.message_handler(Command('new'))
async def append(message: types.Message):
    human = Human.get(id=message.from_user.id)
    if human.id in admins:
        await message.answer(text='круто, админчик. Пришли одну (пока что) фразу для добавления в следующем сообщении')
        await ListOperations.append.set()
    else:
        await message.answer(text='У тебя конечно нет прав админчика, но можешь предложить фразу (или фразы), '
                                  'просто напиши их в след. сообщении. Если расхотелось, просто пиши Отмена '
                                  'и ничего не отправится')
        await MessageForAdmins.message.set()


@dp.message_handler(state=ListOperations.append)
async def list_append(message: types.Message, state: FSMContext):
    msg = message.text
    i = 0
    Words.create(phrase=msg)
    await message.answer(text='Добавлено успешно!')
    await state.finish()