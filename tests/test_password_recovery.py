import allure
from data.data import UserData
from data.urls import Urls
from pages.password_recovery_page import PasswordRecoveryPage
from conftest import get_driver

class TestPasswordRecovery:
    @allure.title("Тест проверки перехода на страницу /forgot-password")
    @allure.description("Тест проверяет переход со страницы входа на страницу восстановления пароля, проверка на верный URL")
    def test_transition_forgot_recovery_open_correct_url(self, get_driver):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        password_recovery_page.click_button_personal_account()
        password_recovery_page.click_recovery_password()
        current_url = password_recovery_page.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD

    @allure.title("Тест проверки перехода на страницу /reset-password")
    @allure.description("Тест проверяет переход со страницы /forgot-password на /reset-password, после ввода почты, проверка на верный URL")
    def test_transition_rest_password_open_correct_url(self, get_driver):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        password_recovery_page.click_button_personal_account()
        password_recovery_page.click_recovery_password()
        password_recovery_page.set_email(UserData.email)
        password_recovery_page.click_restore_button()
        password_recovery_page.visible_save_button()
        current_url = password_recovery_page.get_current_url()
        assert current_url == Urls.RESET_PASSWORD

    @allure.title("Тест проверки клика по кнопке 'показать/скрыть' делает поле активным")
    @allure.description("Тест проверяет, что при нажатии на кнопку 'показать/скрыть', пароль становится видимым, проверка поля на input_status_active")
    def test_click_button_show_hide_input_status_active(self, get_driver):
        password_recovery_page = PasswordRecoveryPage(get_driver)
        password_recovery_page.click_button_personal_account()
        password_recovery_page.click_recovery_password()
        password_recovery_page.set_email(UserData.email)
        password_recovery_page.click_restore_button()
        password_recovery_page.visible_save_button()
        password_recovery_page.set_new_password(UserData.new_password)
        password_recovery_page.click_button_show_hide_password()
        assert password_recovery_page.input_password_status_active()