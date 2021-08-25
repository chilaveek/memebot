import asyncio
import os
import random
import string

from aiogram import types
from aiogram.types import CallbackQuery

from PhotoEditor.demotivator import demotivator_create
from PhotoEditor.hybrid_shakal_demotivator import hybrid
from PhotoEditor.shakalizator import shakalizator
from data.peewee import Human, Words
from keyboards.inline.inline_kb import mode_choice
from loader import dp


@dp.callback_query_handler(text='demotivator')
async def demotivator_show(call: CallbackQuery):
    human = Human.get(id=call.from_user.id)
    human.mode = 'Демотиватор'
    human.save()

    await call.message.edit_text(text=f'Режим сменён на {human.mode}\nПросто пришлите фотку и ждите.',
                                 reply_markup=mode_choice)


@dp.callback_query_handler(text='shakalizator')
async def shakalizator_show(call: CallbackQuery):
    human = Human.get(id=call.from_user.id)
    human.mode = 'Шакализатор'
    human.save()

    await call.message.edit_text(text=f'Режим сменён на {human.mode}\nПросто пришлите фотку и ждите.',
                                 reply_markup=mode_choice)


@dp.callback_query_handler(text='hybrid_shakal_dem')
async def hybrid_show(call: CallbackQuery):
    human = Human.get(id=call.from_user.id)
    human.mode = 'УльтраШакал + Демотиватор'
    human.save()

    await call.message.edit_text(text=f'Режим сменён на {human.mode}\nПросто пришлите фотку и ждите.',
                                 reply_markup=mode_choice)


@dp.message_handler(content_types=['photo'], state=None)
async def photo_operation(message: types.Message):
    human = Human.get(id=message.from_user.id)
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(12)) + '.jpg'
    await message.photo[-1].download('PhotoEditor/sent_photos/' + file_name)

    if human.mode == 'Шакализатор':

        await message.answer(text='Процесс запущен, дождитесь окончания')
        await asyncio.sleep(1)
        human.memes += 1
        human.save()

        name = shakalizator(file_name, 5)
        photo = open('PhotoEditor/ready_photos/' + name + '.jpeg', 'rb')
        await message.answer_photo(photo=photo)
        os.remove('PhotoEditor/sent_photos/' + file_name)
        os.remove('PhotoEditor/ready_photos/' + name + '.jpeg')

    elif human.mode == 'Демотиватор':

        await message.answer(text='Процесс запущен, дождитесь окончания')
        await asyncio.sleep(1)
        human.memes += 1
        human.save()

        i = 0
        for phrase in Words.select():
            i += 1

        wrd1, wrd2 = Words.get(id_primary=random.randint(1, i)), Words.get(id_primary=random.randint(1, i))
        text1, text2 = wrd1.phrase, wrd2.phrase

        if text1 == text2:
            while text1 == text2:
                wrd2 = Words.get(id_primary=random.randint(1, i))
                text2 = wrd2.phrase

        name = demotivator_create(file_name, text1, text2)
        photo = open(name, 'rb')
        await message.answer_photo(photo=photo)
        os.remove('PhotoEditor/sent_photos/' + file_name)
        os.remove(name)

    elif human.mode == 'УльтраШакал + Демотиватор':

        await message.answer(text='Процесс запущен, дождитесь виртуализации')
        await asyncio.sleep(1)
        human.memes += 1
        human.save()

        i = 0
        for phrase in Words.select():
            i += 1

        wrd1, wrd2 = Words.get(id_primary=random.randint(1, i)), Words.get(id_primary=random.randint(1, i))
        text1, text2 = wrd1.phrase, wrd2.phrase

        if text1 == text2:
            while text1 == text2:
                wrd2 = Words.get(id_primary=random.randint(1, i))
                text2 = wrd2.phrase

        name = hybrid(file_name, text1, text2)
        photo = open(name, 'rb')
        await message.answer_photo(photo=photo)
        os.remove(name)

@dp.message_handler(text='📄 Мой Текст')
async def your_text(message: types.Message):
    human = Human.get(id=message.from_user.id)
    human.mode = 'Мой Текст'
    await message.answer(text='Понял. Сначала отправь первую строчку Демотиватора: ')
    await D
