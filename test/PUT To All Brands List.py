import pytest
import requests

BASE_URL = 'https://automationexercise.com/api/brandsList'

def test_get_products_list():
    print(f'Проверяем урл: {BASE_URL}')

    response = requests.get(BASE_URL)

    assert response.status_code == 200, f'Ожидали 200, получили: {response.status_code}'
    print(" Код ответа 200 получен, запрос на получение продуктов успешен.")

    try:
        data = response.json()
        print(" Ответ успешно прочитан как JSON.")
    except requests.exceptions.JSONDecodeError:
        pytest.fail(" Ответ не является валидным JSON.")

    assert isinstance(data, dict), " Ответ должен быть словарем."

def test_put_products_list():
    print(f'Проверяем урл: {BASE_URL}')

    response = requests.put(BASE_URL)

    assert response.status_code == 405, f'Ожидали 405, получили: {response.status_code}'
    print(" Код ответа 405 получен, метод PUT не поддерживается, как и ожидалось.")

    response_text = response.text.strip()
    expected_message = "This request method is not supported."

    assert expected_message in response_text, f" Ожидаемое сообщение не найдено в ответе: {response_text}"
    print("✅ Сообщение об ошибке 'This request method is not supported.' найдено в ответе.")


