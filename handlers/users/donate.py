from aiogram import types

from loader import dp


@dp.message_handler(text='Поддержать')
async def donate_show(message: types.Message):
    await message.answer(text='✋Добро Пожаловать!\nЭтот раздел создан для тех, кто хочет поддержать проект.'
                              '\nЭтот проект лично мой и делался на собственной инициативе. Можете пожертвовать любую '
                                 'сумму вашему покорному слуге для дальнейшего развития. Спасибо.'
                                 '\nhttps://www.donationalerts.com/r/chilaveek',)
