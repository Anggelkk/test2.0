
API_URL = 'https://automationexercise.com/api/verifyLogin'

expected_email = "test@example.com"
expected_password = "password123"

def test_verify_positive(email, password):
    """
    Проверяет ввод email и password в консоли и сравнивает с эталонными данными.
    """
    email = input("Введите email: ")
    password = input("Введите password: ")

    if email == expected_email and password == expected_password:
        print("Успешный вход (код 200)") # Симулируем успешный ответ API
        assert True # Тест проходит успешно, если данные совпадают
    else:
        print("Неверный email или password (код 401)") # Симулируем ошибку API
        assert False, "Неверные учетные данные" # Тест падает, если данные не совпадают

    if email == expected_email and password == expected_password:
        print("{'responseCode': 200, 'message': 'User exists!' }") # Симулируем ответ
        assert True
    else:
        print("{'responseCode': 401, 'message': 'Unauthorized' }") # Симулируем ответ
        assert False, "Неверные учетные данные"


