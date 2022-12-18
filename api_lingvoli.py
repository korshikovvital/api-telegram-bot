"""Переводчик API lingvolive.com"""

import requests
from config import KEY

URl_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANS = 'https://developers.lingvolive.com/api/v1/Minicard'


def get_token(key: str, url_auth) -> str:
    headers_auth = {'Authorization': 'Basic ' + key}
    response = requests.post(url_auth, headers=headers_auth)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Ошибка {response.status_code}')


token = get_token(KEY, URl_AUTH)


def get_translite(word: str, x, y) -> str:
    headers = {'Authorization': 'Bearer ' + token}
    param = {'text': word,
             'srcLang': x,
             'dstLang': y}
    response = requests.get(URL_TRANS, headers=headers, params=param)
    if response.status_code == 200:
        rez = response.json()
        try:
            return rez['Translation']['Translation']
        except Exception as error:
            print(error)
            return 'нет перевода'
    else:
        print(f'Error  {response.status_code}')
        return 'нет перевода, убедитесь что выбрали нужный словарь'
