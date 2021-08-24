from aiogram import types, Bot
from aiogram.dispatcher import FSMContext

from data import config
from data.config import admins
from data.peewee import Human
from loader import dp
from states.message_for_admins import MessageForAdmins


@dp.message_handler(text='💬 Предложить фразу')
async def change(message: types.Message):
    await message.answer(text='Гуд, напиши фразу или фразы для добавления. Если фраз несколько раздели знаками '
                   'типа \|/ чтобы моему хозяину было легче читать твои сочинения. Если расхотелось, просто пиши Отмена '
                                  'и ничего не отправится')
    await MessageForAdmins.message.set()

@dp.message_handler(state=MessageForAdmins.message)
async def message_for_admins(message: types.Message, state: FSMContext):
    msg = message.text
    if msg.lower() == 'отмена':
        await message.answer('Понятненько, ничего не отправляем')
    else:
        for admin in Human.select():
            human = Human.get(id=admin.id)
            bot = Bot(config.BOT_TOKEN)
            if human.id in admins:
               await bot.send_message(text=msg, chat_id=human.id)

    await state.finish()