import allure
import requests

from data.urls import Handlers


@allure.step('Удаляем пользователя')
def delete_user(token):
    response_del = requests.delete(Handlers.INFORMATION_USER, headers=token)
    assert response_del.status_code == 202