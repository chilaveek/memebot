import asyncio
import os
import random
import string

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from PhotoEditor.demotivator import demotivator_create
from data.peewee import Human
from loader import dp


class DemotivatorText(StatesGroup):
    image = State()
    text1 = State()
    text2 = State()


@dp.message_handler(text='📝 Мой Текст')
async def your_text(message: types.Message):
    human = Human.get(id=message.from_user.id)
    await message.answer(text='Понял. Сделаем Демотиватор с твоим текстом. Сначала отправь фотку')
    await DemotivatorText.image.set()

@dp.message_handler(state=DemotivatorText.image, content_types=['photo'])
async def image(message: types.Message, state: FSMContext):
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(12)) + '.jpg'
    await message.photo[-1].download('PhotoEditor/sent_photos/' + file_name)
    await state.update_data(image=file_name)
    await message.answer('Отлично. Теперь пришли верхнюю надпись')
    await DemotivatorText.text1.set()

@dp.message_handler(state=DemotivatorText.text1)
async def image(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(text1=msg)
    await message.answer('Класс. Осталась нижняя надпись')
    await DemotivatorText.text2.set()

@dp.message_handler(state=DemotivatorText.text2)
async def image(message: types.Message, state: FSMContext):
    human = Human.get(id=message.from_user.id)
    msg = message.text

    await state.update_data(text2=msg)
    await asyncio.sleep(1)

    human.memes += 1
    human.save()

    await message.answer('Отлично. Процесс запущен, ожидай')

    data = await state.get_data()
    name = demotivator_create(data['image'], data['text1'], data['text2'])
    photo = open(name, 'rb')
    await message.answer_photo(photo=photo)
    os.remove('PhotoEditor/sent_photos/' + data['image'])
    os.remove(name)
    await state.finish()




