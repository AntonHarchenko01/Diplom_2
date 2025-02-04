from http.client import responses

import allure
import requests

from conftest import create_random_user_for_registration
from data.data import UserData
from data.urls import Urls


class TestChangeUserData:
    @allure.title("Тест проверки успешного изменения email у авторизированного пользователя")
    @allure.description("Тест проверяет, что можно успешно изменить email у авторизированного пользователя, код 200 и сравнение емайлов")
    def test_changing_user_email_faker_email_changing_email_success(self, create_random_user_for_registration):
        payload = {"email": UserData.create_random_user_data()["email"]}
        token = {"Authorization": create_random_user_for_registration[2]}
        response = requests.patch(Urls.INFORMATION_USER, headers=token, data=payload)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == payload["email"]

    @allure.title("Тест проверки успешного изменения password у авторизованного пользователя")
    @allure.description("Тест проверяет, что можно изменить password у авторизованного пользователя, код 200")
    def test_changing_user_password_faker_password_changing_password_success(self, create_random_user_for_registration):
        payload = {"password": UserData.create_random_user_data()["password"]}
        token = {"Authorization": create_random_user_for_registration[2]}
        response = requests.patch(Urls.INFORMATION_USER, headers=token, data=payload)
        assert response.status_code == 200

    @allure.title("Тест проверки успешного изменения name у авторизованного пользователя")
    @allure.description("Тест проверят, что можно изменить name у авторизованного пользователя, код 200 и сравнение полей name")
    def test_changing_user_name_faker_name_changing_name_success(self, create_random_user_for_registration):
        payload = {"name": UserData.create_random_user_data()["name"]}
        token = {"Authorization": create_random_user_for_registration[2]}
        response = requests.patch(Urls.INFORMATION_USER, headers=token, data=payload)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == payload["name"]

    @allure.title("Тест проверки получения сообщения, при изменении данных неавторизованного пользователя")
    @allure.description("Тест проверяет, что нельзя изменить данные неавторизованному пользователя, код 401 и сообщение You should be authorized")
    def test_changing_user_data_faker_user_data_error_message(self):
        payload = UserData.create_random_user_data()
        response = requests.patch(Urls.INFORMATION_USER, data= payload)
        assert response.status_code ==401
        assert response.json()["message"] == "You should be authorised"

