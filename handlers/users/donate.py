from aiogram import types

from loader import dp


@dp.message_handler(text='💳 Задонатить')
async def donate_show(message: types.Message):
    await message.answer(text='✋ Добро Пожаловать!\n\n💰 Этот раздел создан для тех, кто хочет финансово поддержать проект.'
                              '\nЭтот проект лично мой и делался на собственной инициативе. Можешь пожертвовать любую '
                              'сумму мне для продолжения работы бота, дальнейшего развития, еды, кофе или энергетиков. Спасибо.'
                              '\n\n--\n\n😋 В сообщении к донату укажи свой юзернейм, чтобы я мог отблагодарить тебя лично хехе'
                              '\n\n--\n\nhttps://www.donationalerts.com/r/chilaveek',)
