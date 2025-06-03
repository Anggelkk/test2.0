# import requests
#
# API_URL =  'https://automationexercise.com/api/verifyLogin'
#

# def test_delete_request():
#     print(API_URL)
#     response = requests.delete(API_URL)
#
#     if response.status_code == 200:
#         print('Получили код 200, тест не пройден')
#     elif response.status_code == 405:
#         print ('Получили код 405, тест пройден')
#     else:
#         print('Неизвестная ошибка')

import pytest
import requests

API_URL = 'https://automationexercise.com/api/verifyLogin'

def test_delete_request_method_not_supported():

    response = requests.delete(API_URL)
    assert response.status_code == 200,\
    f"Ожидался код 405, но получен {response.status_code}. Ответ: {response.text}"

    expected_message = "This request method is not supported."
    assert expected_message in response.text, \
        f"Ожидаемое сообщение '{expected_message}' не найдено в ответе: {response.text}"

    response_to_json = response.json()
    assert response_to_json['responseCode'] == 405
    print(response_to_json['responseCode'])
    print(f'Тест успешно пройден: Получен код {response.status_code} и сообщение: "{response.text.strip()}"')