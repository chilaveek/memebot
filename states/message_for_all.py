from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import Unauthorized

from data import config
from data.config import admins
from data.peewee import Human
from loader import dp


class MessageForAll(StatesGroup):
    message = State()

@dp.message_handler(Command('msg'), state=None)
async def msg_for_all(message: types.Message):
    human = Human.get(id=message.from_user.id)
    if human.id in admins:
        await message.answer(text='Приветствую, пришли сообщение для отправки всем юзерам бота')
        await message.answer_sticker(sticker='CAACAgIAAxkBAAECxjFhHfrG3chMiIpBl6GjdIm47OcCxAACmgADObZ9OR3fkdWjbQ9fIAQ')

    await MessageForAll.message.set()

@dp.message_handler(state=MessageForAll.message)
async def message_send(message: types.Message, state: FSMContext):
    send_message = message.text
    bot = Bot(config.BOT_TOKEN)
    for gamer in Human.select():
        try:
            human = Human.get(id=gamer.id)
            await bot.send_message(chat_id=gamer.id, text=send_message)
        except Unauthorized:
            pass

    await state.finish()


