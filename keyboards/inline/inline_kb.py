from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_button(text, cb_data):
    button = [
        InlineKeyboardButton(text=text, callback_data=cb_data)
    ]
    kb = InlineKeyboardMarkup(row_width=1).add(*button)

    return kb


start_btn_yes = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton(text='Да', callback_data='yes_start'),
    )


start_kb = InlineKeyboardMarkup(row_width=2).row(
    InlineKeyboardButton(text='Да', callback_data='yes_start'),
    InlineKeyboardButton(text='Нет', callback_data='no_start'),
    )

mode_choice = InlineKeyboardMarkup(row_width=1).add(
InlineKeyboardButton(text='Шакализатор', callback_data='shakalizator'),
    InlineKeyboardButton(text='Демотиватор', callback_data='demotivator'),

)

share_kb = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton(text='Поделиться со всеми!', callback_data='share'),
    )
