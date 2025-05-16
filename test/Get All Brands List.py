import pytest
import requests


API_URL1 = "https://automationexercise.com/api/brandsList"


def test_get_brands_list():
    print(f'\nПроверяем адрес: {API_URL1}')

    response = requests.get(API_URL1)

    assert response.status_code == 200, f"Должны получить 200, получили {response.status_code}"
    print("Получили 200")

    try:
        data = response.json()
        print("Ответ успешно прочитан как JSON.")
    except requests.exceptions.JSONDecodeError:
        pytest.fail("Ответ не является валидным JSON")

    assert "brands" in data, 'В JSON ответе нет "brands"'
    assert isinstance(data['brands'], list), "Значение 'brands' не список."
    print("В JSON есть 'brands', и это список.")

