import allure
from conftest import get_driver, create_user
from data.urls import Urls
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title("Тест перехода на страницу личный кабинет")
    @allure.description("Тест проверяет переход на страницу личного кабинета, без авторизации, проверка на верный URL")
    def test_transition_personal_account_unauthorized_open_page_personal_account(self, get_driver):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        password_recovery_page.click_button_personal_account()
        current_url = password_recovery_page.get_current_url()
        assert current_url == Urls.LOGIN_PAGE

    # После авторизации не срабатывает переход в личный кабинет в браузере firefox, в chrome все отрабатывает правильно
    @allure.title("Тест перехода в 'историю заказов'")
    @allure.description("Тест проверяет переход на страницу истории заказов у авторизованного пользователя, проверка на верный URL")
    def test_transition_history_order_authorized_user_open_page_order_history(self, get_driver,create_user):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        password_recovery_page.click_button_personal_account()
        personal_account_page.authorization_user(create_user)
        password_recovery_page.click_button_personal_account()
        personal_account_page.click_history_order_button()
        current_url = personal_account_page.get_current_url()
        assert current_url == Urls.HISTORY_ORDER_PAGE

    # После авторизации не срабатывает переход в личный кабинет в браузере firefox, в chrome все отрабатывает правильно
    @allure.title("Тест выхода из аккаунта")
    @allure.description("Тест проверяет возможность выхода из аккаунта, проверка на видимость элемента 'Вход' после выхода из аккаунта")
    def test_logout_authorized_user_inscription_entrance(self, get_driver, create_user):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        password_recovery_page.click_button_personal_account()
        personal_account_page.authorization_user(create_user)
        password_recovery_page.click_button_personal_account()
        assert personal_account_page.click_logout_button()

