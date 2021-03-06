from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("menu", "Показать меню"),
        types.BotCommand("name", "Сменить имя"),
        types.BotCommand("new", "Добавить фразочку"),
        types.BotCommand("help_admins", "help для админчиков")
    ])
