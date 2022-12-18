"""API сервиса OpenWeatherMap"""

import requests
from config import KEY_WEATHER

URL = 'https://api.openweathermap.org/data/2.5/weather'
URL_GEO = 'http://api.openweathermap.org/geo/1.0/direct'


def get_geocoding(city):
    """Получаем координаты"""
    param = {'q': city,
             'appid': KEY_WEATHER}
    response = requests.get(URL_GEO, params=param)
    if response.status_code == 200:
        try:
            data = response.json()
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
        except Exception as error:
            print(error)
            return 'Нет данных'

    else:
        print('Не получилось получить гео')


def get_weather(city):
    """Погода по полученному гео"""
    try:
        lat, lon = get_geocoding(city)
        param = {'lat': lat, 'lon': lon,
                 'appid': KEY_WEATHER, 'units': 'metric'}
        response = requests.get(URL, params=param)
        if response.status_code == 200:
            rez = response.json()
            temp = rez['main']['temp']
            wind = rez['wind']['speed']
            humidity = rez['main']['humidity']

            return (f'Температура {temp}\nСкорость ветра {wind}\n'
                    f'Влажность {humidity}')
    except Exception as error:
        print(error)
        return 'Нет данных по этому городу'


city_popular = {'msk': (55.7504461, 37.6174943),
                'spb': (59.938732, 30.316229),
                'ekb': (56.839104, 60.60825)}


def get_pop_weather(city):
    try:
        lat, lon = city
        param = {'lat': lat, 'lon': lon,
                 'appid': KEY_WEATHER, 'units': 'metric'}
        response = requests.get(URL, params=param)
        if response.status_code == 200:
            rez = response.json()
            temp = rez['main']['temp']
            wind = rez['wind']['speed']
            humidity = rez['main']['humidity']

            return (f'Температура {temp}\nСкорость ветра {wind}\n'
                    f'Влажность {humidity}')
    except Exception as error:
        print(error)
        return 'Нет данных по этому городу'
