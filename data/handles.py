from data.urls import Urls


class Handles:
    CREATE_USER = f"{Urls.MAIN_PAGE}/api/auth/register"
    DELETE_USER = f"{Urls.MAIN_PAGE}/api/auth/user"
    CREATE_ORDER = f"{Urls.MAIN_PAGE}/api/orders"