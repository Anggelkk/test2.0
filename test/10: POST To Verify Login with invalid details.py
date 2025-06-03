import pytest
import requests
import json

BASE_URL = 'https://automationexercise.com/api/verifyLogin'

def test_post_verify_login_negative():
    print(BASE_URL)

    invalid_email = "nonexistent_user@example.com"
    invalid_password = "wrong_password123"

    payload = {
        'email': invalid_email,
        'password': invalid_password
    }

    response = requests.post(BASE_URL, data=payload)

    assert response.status_code == 200, f'Ожидали 200, получили {response.status_code}'

    expected_message = "User not found!"
    assert expected_message in response.text.strip(), f"Ожидаемое сообщение не найдено в ответе: {response.text}"

    response_to_json = response.json()
    assert response_to_json['responseCode'] == 404,\
    print(response_to_json['responseCode'])
    print(f'Тест успешно пройден: Получен код {response.status_code} и сообщение: "{response.text.strip()}"')


