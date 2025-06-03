import pytest
import requests

BASE_URL = 'https://automationexercise.com/api/searchProduct'

def test_post_search_product():
    print(BASE_URL)

    search_term = "top"
    payload = {"search_product": search_term}

        # Отправляем POST запрос на URL с данными
    response = requests.post(BASE_URL, data=payload)

    assert response.status_code == 200
    data = response.json()

    assert 'products' in data

    assert isinstance(data['products'], list)




