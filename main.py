from config import bot
from keybord import markup, markup_inline, markup_chang, markup_weather
from api_lingvoli import get_translite
from openexchang import get_usd_cheng
from openweathermap import get_pop_weather, get_weather, city_popular


@bot.message_handler(commands=['start'])
def welcome_fun(message):
    """Основное меню"""
    bot.send_message(
        message.chat.id,
        f'Привет {message.chat.first_name}, '
        f'это бот показывает работу с различными API',
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def get_text(messange):
    if messange.text == 'Переводчик':
        bot.send_message(
            messange.chat.id,
            'Выберите язык для перевода', reply_markup=markup_inline)
    if messange.text == 'Курс валют':
        bot.send_message(
            messange.chat.id,
            'Выберите список валют, доступных в настоящее время',
            reply_markup=markup_chang)
    if messange.text == 'Погода':
        bot.send_message(
            messange.chat.id,
            'Узнате погоду.Выберите город или введите свой',
            reply_markup=markup_weather)


@bot.callback_query_handler(func=lambda call: True)
def call_fun(call):
    """Переводчик"""
    if call.data == 'RU':
        msg = bot.send_message(call.message.chat.id,
                               'Введите одно слово на русском языке '
                               'Бот переводит только по одному слову!')
        bot.register_next_step_handler(msg, trans_ru_en)
    if call.data == 'EN':
        msg = bot.send_message(call.message.chat.id,
                               'Введите одно слово на английском языке '
                               'Бот переводит только по одному слову!')
        bot.register_next_step_handler(msg, trans_en_ru)
    """Курс валют"""
    if call.data in ('RUB', 'EUR', 'GBP', 'THB'):
        bot.send_message(call.message.chat.id,
                         f'Курс {call.data} к USD '
                         f'равен {get_usd_cheng(call.data)}')

    """Погода"""
    if call.data == 'msk':
        bot.send_message(
            call.message.chat.id,
            get_pop_weather(city_popular['msk']))
    if call.data == 'spb':
        bot.send_message(
            call.message.chat.id,
            get_pop_weather(city_popular['spb']))
    if call.data == 'ekb':
        bot.send_message(
            call.message.chat.id,
            get_pop_weather(city_popular['ekb']))
    if call.data == 'next':
        msg = bot.send_message(
            call.message.chat.id,
            'Введите свой город')
        bot.register_next_step_handler(msg, fun_wather)

    bot.answer_callback_query(call.id)


def trans_ru_en(message):
    bot.reply_to(message, get_translite(message.text, 1049, 1033))


def trans_en_ru(message):
    bot.reply_to(message, get_translite(message.text, 1033, 1049))


def fun_wather(message):
    bot.send_message(message.chat.id, get_weather(message.text))


bot.polling(non_stop=True, skip_pending=True)
