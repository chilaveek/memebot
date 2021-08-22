from aiogram import types

from data.peewee import Human
from loader import dp


@dp.message_handler(text='Зачем нужен бот?')
async def bot_info(message: types.Message):
    human = Human.get(id=message.from_user.id)
    await message.answer(text=f'{human.name}, бот был сделан в целях повеселиться и быстро сделать мем ')