from aiogram import types

from loader import dp


@dp.message_handler(text='Поддержать')
async def donate_show(message: types.Message):
    await message.answer(text='✋Добро Пожаловать!\nЭтот раздел создан для тех, кто хочет поддержать проект.'
                              '\nЭтот проект лично мой и делался на собственной инициативе. Можешь пожертвовать любую '
                              'сумму мине для дальнейшего развития, еды, кофе или энергетиков. Спасибо.'
                              '\n\n--\n\nВ сообщении к донату укажи свой юзернейм, чтобы я мог отблагодарить тебя лично хехе'
                              '\nhttps://www.donationalerts.com/r/chilaveek',)
