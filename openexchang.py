"""Сервис курса валют API openexchangerates.org"""
import requests
from config import YOUR_APP_ID

URL = "https://openexchangerates.org/api/latest.json"
hedars = {"Authorization": "Token " + YOUR_APP_ID}


def get_usd_cheng(symbols):
    param = {'base': 'USD',
             'symbols': symbols}
    rez = requests.get(URL, headers=hedars, params=param)
    if rez.status_code == 200:
        try:
            rez = rez.json()
            return rez['rates'][symbols]
        except Exception as error:
            print(error)
            return 'Нет данных'
    else:
        print(f'Error {rez.status_code}')
