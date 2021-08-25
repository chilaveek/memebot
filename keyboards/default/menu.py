from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🤩 Создать'),
            KeyboardButton(text='📝 Мой Текст')
        ],
        [
            KeyboardButton(text='💬 Предложить фразу')
        ],
        [
            KeyboardButton(text='💳 Задонатить'),
            KeyboardButton(text='❓ Зачем?'),
        ],

    ],
    resize_keyboard=True,
)