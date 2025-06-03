import pytest
import requests

API_URL = 'https://automationexercise.com/api/searchProduct'

def test_post_search_negative():
    """
    Проверяет, что запрос POST без параметра search_product возвращает 400.
    """
    response = requests.post(API_URL) # Не передаем параметр search_product

    assert response.status_code == 200, f"Ожидался код 200, получен: {response.status_code}"

    expected_message = "Bad request, search_product parameter is missing in POST request."
    assert expected_message in response.text.strip(), f"Ожидаемое сообщение не найдено в ответе: {response.text}"

    response_to_json = response.json()
    assert response_to_json['responseCode'] == 400,\
    print(response_to_json['responseCode'])
    print(f'Тест успешно пройден: Получен код {response.status_code} и сообщение: "{response.text.strip()}"')