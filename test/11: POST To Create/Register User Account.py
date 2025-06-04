import pytest
import requests
import json
from faker import Faker

BASE_URL = 'https://automationexercise.com/api/createAccount'
fake = Faker()

def test_post_create_user_acc():
   print(BASE_URL)

   name = fake.first_name() + ' ' + fake.last_name()
   email = fake.email()
   password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
   title = fake.random_element(elements=('Mr', 'Mrs', 'Miss'))
   birth_date = fake.random_int(min=1, max=28)  # День месяца
   birth_month = fake.month_name()
   birth_year = fake.random_int(min=1950, max=2003)

   firstname = fake.first_name()
   lastname = fake.last_name()
   company = fake.company()
   address1 = fake.address()
   address2 = fake.secondary_address()
   country = 'Russia'  
   zipcode = fake.postcode()
   state = fake.state()
   city = fake.city()  
   mobile_number = fake.phone_number()

   payload = {
      'name': name,
      'email': email,
      'password': password,
      'title': title,  # Теперь это строка, а не список
      'birth_date': birth_date,
      'birth_month': birth_month,
      'birth_year': birth_year,
      'firstname': firstname,
      'lastname': lastname,
      'company': company,
      'address1': address1,
      'address2': address2,
      'country': country,
      'zipcode': zipcode,
      'state': state,
      'city': city,
      'mobile_number': mobile_number
      }

   response = requests.post(BASE_URL, data=payload)
   assert response.status_code == 200, f'Ожидали 200, получили {response.status_code}'

   expectid_message = 'User created!'
   assert expectid_message in response.text.strip(), f'Ожидали сообщение: {response.text}'

   response_to_json = response.json()
   assert response_to_json['responseCode'] == 201,\
   print(response_to_json['responseCode'])
   print(f'Тест успешно пройден: Получен код {response.status_code} и сообщение: "{response.text.strip()}"')


