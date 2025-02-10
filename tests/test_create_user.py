import allure
import pytest
import requests
from data.data import UserData, ErrorText
from data.helper import delete_user
from data.urls import Handlers


class TestCreateUser:
    @allure.title("Тест проверки успешного создания пользователя")
    @allure.description("Тест проверяет успешное создание пользователя при заполненных обязательных полях, код 200 и success:True, удаляем созданного пользователя")
    def test_create_user_required_fields_filled_user_created(self):
        payload = UserData.data_user_correct
        response = requests.post(Handlers.REGISTER_USER, data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True
        token = {'authorization': response.json().get('accessToken')}
        delete_user(token)

    @allure.title("Тест неудачного создания пользователя, который уже был создан")
    @allure.description("Тест проверяет неудачное создание пользователя, если он уже был создан, получение кода 403 и сообщения User already exists, удаляем созданного пользователя")
    def test_unsuccessful_creating_user_double_user_existing_user(self):
        payload = UserData.data_user_double
        response = requests.post(Handlers.REGISTER_USER, data=payload)
        token = {'Authorization': response.json().get('accessToken')}
        response_double = requests.post(Handlers.REGISTER_USER, data=payload)
        assert response_double.status_code == 403
        assert ErrorText.USER_EXISTS in response_double.text
        delete_user(token)

    @allure.title("Тест неудачного создания пользователя, без обязательного поля")
    @allure.description("Тест проверяет, что если не заполнить обязательное поле, пользователь не создаться, код 403 и сообщение что одно из полей не заполнено")
    @pytest.mark.parametrize('user_data',[UserData.data_user_not_email, UserData.data_user_not_password, UserData.data_user_not_name])
    def test_unsuccessful_creating_user_data_without_fields_required_fields(self, user_data):
        response = requests.post(Handlers.REGISTER_USER, data=user_data)
        assert response.status_code == 403
        assert ErrorText.FIELD_IS_EMPTY in response.text



