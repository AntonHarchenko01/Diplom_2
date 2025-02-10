from faker import Faker


class UserData:
    data_user_correct = {
        "email": "harchenko24@yandex.ru",
        "password": "12345678",
        "name": "HarchenkoA24"
    }
    data_user_double = {
        "email": "userdouble24@yandex.ru",
        "password": "12345678",
        "name": "UserDouble24"
    }
    data_user_not_email = {
        "email": "",
        "password": "12345678",
        "name": "NoEmail"
    }
    data_user_not_password = {
        "email": "notpassword@yandex.ru",
        "password": "",
        "name": "NotPassword"
    }
    data_user_not_name = {
        "email": "notname@yandex.ru",
        "password": "12345678",
        "name": ""
    }

    data_user_registered = {
        "email": "test-data@yandex.ru",
        "password": "password",
    }

    data_user_unregistered = {
        "email": "harchenko012@yandex.ru",
        "password": "12345678"
    }

    @staticmethod
    def create_faker_user_data():
        faker = Faker()
        user_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }
        return user_data

class Ingredients:
    data_ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa74"]}
    data_ingredients_incorrect = {"ingredients": ["0", "1"]}

class ErrorText:
    UNAUTHORIZED = "You should be authorised"
    NOT_INGREDIENTS = "Ingredient ids must be provided"
    SERVER_ERROR = "Internal Server Error"
    USER_EXISTS = 'User already exists'
    FIELD_IS_EMPTY = "Email, password and name are required fields"

