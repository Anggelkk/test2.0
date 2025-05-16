import pytest
import requests

API_URL = 'https://automationexercise.com/api/productsList'

def test_get_product_list():
    print(f'\n Проверяем адрес: {API_URL}')

    response = requests.get(API_URL)

    assert response.status_code == 200, f"Ожидался код ответа 200, получен: {response.status_code}"
    print(" Код ответа 200 получен, запрос на получение продуктов успешен.")


    data = response.json()
    assert isinstance(data, list), "Ответ должен быть списком продуктов."
    print(" Ответ имеет ожидаемую структуру (список продуктов).")

def test_post_product_list():
    print(f'\nПроверяем адрес: {API_URL}')

    response = requests.post(API_URL)

    assert response.status_code == 405, f"Ожидался код ответа 405, получен: {response.status_code}"
    print("Код ответа 405 получен, как и ожидалось.")

    response_message = response.text
    expected_message = "This request method is not supported."

    assert expected_message in response_message, f"Ожидаемое сообщение не найдено в ответе: {response_message}"
    print(" Сообщение об ошибке совпадает с ожидаемым.")
