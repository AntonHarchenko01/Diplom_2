from faker import Faker


class UserData:
    data_user_correct = {
        "email": "harchenko@yandex.ru",
        "password": "12345678",
        "name": "HarchenkoA"
    }
    data_user_double = {
        "email": "userdouble1@yandex.ru",
        "password": "12345678",
        "name": "UserDouble1"
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
    def create_random_user_data():
        faker = Faker()
        user_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }
        return user_data


