import allure
import requests

from data.data import Ingredients
from data.urls import Handlers
from conftest import create_random_user_for_registration


class TestGetUserOrder:
    @allure.title("Тест получения заказов авторизованного пользователя")
    @allure.description("Тест проверяет, что можно получить список заказов авторизованного пользователя, код 200 и созданный заказ есть в списке полученных заказов")
    def test_get_order_user_create_new_order_order_is_in_order_list(self, create_random_user_for_registration):
        token = {"Authorization": create_random_user_for_registration[2]}
        response_create_order = requests.post(Handlers.CREATE_ORDER, headers=token, data=Ingredients.data_ingredients)
        response_get_order = requests.get(Handlers.GET_ORDER, headers= token)
        assert response_get_order.status_code == 200
        assert response_get_order.json()["orders"][0]["_id"] == response_create_order.json()["order"]["_id"]

    @allure.title("Тест получения заказов неавторизованного пользователя")
    @allure.description("Тест проверяет, что нельзя получить список заказов неавторизованного пользователя, код 401 и сообщение You should be authorised")
    def test_unsuccessful_get_order_not_login_order_unsuccessful_get(self):
        response = requests.get(Handlers.GET_ORDER)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"