import os
import random
import string

from aiogram import types
from aiogram.types import CallbackQuery

from PhotoEditor.demotivator import demotivator_create
from PhotoEditor.shakalizator import shakalizator
from data.peewee import Human, Words
from keyboards.inline.inline_kb import mode_choice
from loader import dp


@dp.callback_query_handler(text='demotivator')
async def demotivator(call: CallbackQuery):

    human = Human.get(id=call.from_user.id)
    human.mode = 'Демотиватор'
    human.save()

    await call.message.edit_text(text=f'Режим сменён на {human.mode}\nПросто пришлите фотку и ждите.', reply_markup=mode_choice)

@dp.callback_query_handler(text='shakalizator')
async def shakalizator_show(call: CallbackQuery):

    human = Human.get(id=call.from_user.id)
    human.mode = 'Шакализатор'
    human.save()

    await call.message.edit_text(text=f'Режим сменён на {human.mode}\nПросто пришлите фотку и ждите.', reply_markup=mode_choice)

@dp.message_handler(content_types=['photo'])
async def photo_operation(message: types.Message):
    human = Human.get(id=message.from_user.id)
    letters = string.ascii_lowercase
    file_name = ''.join(random.choice(letters) for i in range(12)) + '.jpg'
    await message.photo[-1].download('PhotoEditor/sent_photos/' + file_name)

    if human.mode == 'Шакализатор':
        name = shakalizator(file_name, 5)
        photo = open('PhotoEditor/ready_photos/' + name + '.jpeg', 'rb')
        await message.answer_photo(photo=photo)
        os.remove('PhotoEditor/sent_photos/' + file_name)
        os.remove('PhotoEditor/ready_photos/' + name + '.jpeg')

    elif human.mode == 'Демотиватор':
        # await DemotivatorText.text1.set()
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

# @dp.message_handler(state=DemotivatorText.text1)
# async def demtext1(message: types.Message, state: FSMContext):
#     human = Human.get(id=message.from_user.id)
#     text1 = message.text
#
#     await state.update_data(text1=text1)
#
#     await message.answer(text=f'Отлично, {human.name}, следующим предложением пришлите вторую строчку. Если второй '
#                               'строчки вообще быть не должно, отправьте none')
#     await DemotivatorText.text2.set()

