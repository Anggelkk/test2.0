import requests
import pytest


API_URL = "https://automationexercise.com/api/productsList"

def test_get_all_products_list():
    print(f"\nПроверяем адрес: {API_URL}")

    # 4. Отправляем "заказ" официанту (GET запрос к API).
    #    Мы используем requests.get() для этого.
    response = requests.get(API_URL)
    print(f"Получили ответ с кодом: {response.status_code}")

    # 5. Проверяем первый пункт нашего списка: код ответа должен быть 200.
    #    Если он не 200, тест провалится и скажет об этом.
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
    print("Код ответа 200 получен.")

    # 6. Проверяем второй пункт: ответ должен быть в формате JSON.
    #    requests.json() пытается прочитать ответ как JSON.
    #    Если не получилось, произойдет ошибка, и тест провалится.
    try:
        data = response.json()
        print("Ответ успешно прочитан как JSON.")
    except requests.exceptions.JSONDecodeError:
        # Если не JSON, говорим, что тест провалился.
        pytest.fail(" Ответ не является валидным JSON.")

    # 7. Проверяем третий пункт: в JSON должен быть ключ 'products',
    #    и его значение должно быть списком.
    assert "products" in data, " В JSON ответе нет 'products'."
    assert isinstance(data["products"], list), " Значение 'products' не список."
    print("В JSON есть 'products', и это список.")

    # 8. (Дополнительно) Проверяем, что список не пустой, там действительно что-то есть.
    assert len(data["products"]) > 0, " Список продуктов пуст."
    print(f"Список продуктов не пуст, товаров: {len(data['products'])}.")

    # 9. (Дополнительно) Проверяем, что первый товар в списке содержит ожидаемые данные (например, id, name, price).
    if len(data["products"]) > 0:
         first_product = data["products"][0] # Берем первый товар из списка
         assert "id" in first_product, " У первого товара нет id."
         assert "name" in first_product, " У первого товара нет name."
         assert "price" in first_product, " У первого товара нет price."
         print("Первый товар в списке имеет ожидаемую структуру.")

    print("Тест успешно завершен!")