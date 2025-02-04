import allure
import requests

from data.data import Ingredients
from data.urls import Handlers
from conftest import create_random_user_for_registration


class TestCreateOrder:
    @allure.title("Тест создание заказа с авторизацией и ингредиентами")
    @allure.description("Тест проверяет успешно созданный заказ, авторизованным пользователем с ингредиентами, код 200 и success: True")
    def test_create_order_login_user_create_order_success(self, create_random_user_for_registration):
        token = {"Authorization": create_random_user_for_registration[2]}
        response = requests.post(Handlers.CREATE_ORDER, headers=token, data=Ingredients.data_ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Тест создания заказа неавторизованным пользователем с ингредиентами")
    @allure.description("Тест проверяет созданный заказ без авторизации пользователя с ингредиентами, код 200 и success: True")
    def test_create_order_not_login_user_create_order_success(self):
        response = requests.post(Handlers.CREATE_ORDER, data= Ingredients.data_ingredients)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Тест создания заказа без авторизации и без ингредиентов")
    @allure.description("Тест проверяет, что нельзя создать заказ без ингредиентов и авторизации, код 400 и сообщение Ingredient ids must be provided")
    def test_unsuccessful_creating_order_without_ingredients_unsuccessful_creating(self):
        response = requests.post(Handlers.CREATE_ORDER)
        assert response.status_code ==400
        assert response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Тест создания заказа с неверным хешем ингредиентов, с авторизацией")
    @allure.description("Тест проверят, что нельзя создать заказ с неверными хешами ингредиентов, с авторизацией, код = 500 и сообщение Internal Server Error")
    def test_unsuccessful_creating_order_invalid_hash_unsuccessful_creating(self, create_random_user_for_registration):
        token = {"Authorization": create_random_user_for_registration[2]}
        response = requests.post(Handlers.CREATE_ORDER, data= Ingredients.data_ingredients_incorrect, headers= token)
        assert response.status_code == 500
        assert 'Internal Server Error' in response.text
