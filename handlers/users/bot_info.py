from aiogram import types

from data.peewee import Human
from loader import dp


@dp.message_handler(text='❓ Зачем?')
async def bot_info(message: types.Message):
    human = Human.get(id=message.from_user.id)
    await message.answer(text=f'{human.name}, бот был сделан в целях повеселиться и быстро сделать мем'
                              f'\nВ создании фраз в боте я старался сохранить достаточный уровень абсурдоности, чтобы'
                              f'мемы получались достаточно смешными. Фразы бота достаточно разные, 1ая и 2ая генерируются'
                              f'случайно, всего вариантов взаимодействия свыше 80К и это число может стать ещё '
                              f'больше благодаря вам и вашей активности. Сделайте вклад в бота - предложите фразу')