import allure
import requests

from data.data import UserData
from data.urls import Handlers


class TestLoginUser:
    @allure.title("Тест проверки успешного входа пользователя")
    @allure.description("Тест проверяет успешный вход зарегистрированного пользователя, код 200 и success: True")
    def test_login_user_registered_user_login_success(self):
        payload =UserData.data_user_registered
        response = requests.post(Handlers.LOGIN_USER, data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Тест проверки неуспешного входа пользователя")
    @allure.description("Тест проверяет, что невозможно войти c неверными данными, код 401 и success: False")
    def test_not_login_user_unregistered_user_login_not_success(self):
        payload = UserData.data_user_unregistered
        response = requests.post(Handlers.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.json().get("success") is False
