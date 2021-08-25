from aiogram import types

from data.peewee import Human
from keyboards.inline.inline_kb import mode_choice
from loader import dp


@dp.message_handler(text='🤩 Создать')
async def create_show(message: types.Message):
    human = Human.get(id=message.from_user.id)
    await message.answer(text=f'Окей, пришли мне фотку или поменяй режим.\nРежим Сейчас:\n<b>{human.mode}</b>',
                         reply_markup=mode_choice)