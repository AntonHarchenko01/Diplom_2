
class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'


class Handlers:
    REGISTER_USER = f'{Urls.BASE_URL}/api/auth/register'
    INFORMATION_USER = f'{Urls.BASE_URL}/api/auth/user'
    LOGIN_USER = f'{Urls.BASE_URL}/api/auth/login'
    CREATE_ORDER = f'{Urls.BASE_URL}/api/orders'
    GET_ORDER = f'{Urls.BASE_URL}/api/orders'

