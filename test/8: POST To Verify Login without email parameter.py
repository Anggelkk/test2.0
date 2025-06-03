from logging import exception

import pytest
import requests

BASE_URL = 'https://automationexercise.com/api/verifyLogin'
password = "123456"  # Установите ваш пароль

def test_verify_post_negative():
    print(f'Отправка запроса на: {BASE_URL}')

    payload = {
        'password': password
    }

    response = requests.post(BASE_URL, data=payload)

    assert response.status_code == 200, f'Ожидали 200, получили {response.status_code} с сообщением: {response.text}'

    expected_message = 'Bad request, email or password parameter is missing in POST request'
    assert expected_message in response.text,\
    f"Ожидаемое сообщение '{expected_message}' не найдено в ответе: {response.text}"

    response_to_json = response.json()
    assert response_to_json['responseCode'] == 400
    print(response_to_json['responseCode'])
    print(f'Тест успешно пройден: Получен код {response.status_code} и сообщение: "{response.text.strip()}"')

