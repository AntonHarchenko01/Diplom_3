import random
import string

import allure
import requests

from data.data import Ingredients
from data.handles import Handles


@allure.step("Генерируем данные пользователя")
def generate_data_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_random_string(10) + '@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@allure.step("Создадим заказ")
def create_order(answer):
    token = answer.json().get("accessToken")
    ingredients = {"ingredients": [Ingredients.CRATOR_BURGER]}
    headers = {"Content-type": "application/json", "Authorization": f"{token}"}
    response = requests.post(Handles.CREATE_ORDER, headers=headers, json=ingredients)
    return response