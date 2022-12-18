from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   row_width=1)
markup.add(
    types.KeyboardButton('Переводчик'),
    types.KeyboardButton('Курс валют'),
    types.KeyboardButton('Погода'),
)
markup_inline = types.InlineKeyboardMarkup()
markup_inline.add(
    types.InlineKeyboardButton('RU - EN', callback_data='RU'),
    types.InlineKeyboardButton('EN - RU', callback_data='EN'),
)

markup_chang = types.InlineKeyboardMarkup(row_width=2)
markup_chang.add(
    types.InlineKeyboardButton('USD - RUB', callback_data='RUB'),
    types.InlineKeyboardButton('USD - EUR', callback_data='EUR'),
    types.InlineKeyboardButton('USD - GBP', callback_data='GBP'),
    types.InlineKeyboardButton('USD - THB', callback_data='THB')
)

markup_weather = types.InlineKeyboardMarkup(row_width=2)
markup_weather.add(
    types.InlineKeyboardButton('Москва', callback_data='msk'),
    types.InlineKeyboardButton('Санкт-Петербург', callback_data='spb'),
    types.InlineKeyboardButton('Екатеринбург', callback_data='ekb'),
    types.InlineKeyboardButton('Другой город', callback_data='next')
)
