import allure
import pytest
import requests

from data.data import UserData
from data.urls import Handlers


@allure.step("Регистрируем рандомного пользователя")
@pytest.fixture(scope='function')
def create_random_user_for_registration():
    random_user_data = UserData.create_faker_user_data()
    response = requests.post(Handlers.REGISTER_USER, data=random_user_data)
    if response.status_code != 200:
        pytest.fail(f'Не удалось создать пользователя: {response.text}')
    token = response.json().get('accessToken')
    yield random_user_data, response, token
    requests.delete(Handlers.INFORMATION_USER, headers={'Authorization': f'{token}'})
