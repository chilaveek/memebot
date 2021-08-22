from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Создать'),
            KeyboardButton(text='Поддержать'),
            KeyboardButton(text='Зачем нужен бот?'),
        ],
        [
            KeyboardButton(text='Предложить фразу')
        ],

    ],
    resize_keyboard=True,
)