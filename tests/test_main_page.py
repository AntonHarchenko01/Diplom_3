import allure
from conftest import get_driver, create_user
from data.data import MessageText
from data.urls import Urls
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage


class TestMainPage:
    @allure.title("Тест проверки перехода на конструктор")
    @allure.description("Тест проверяет перехода на конструктор из личного кабинета, проверка на нажатие кнопки, после чего появляется надпись 'Соберите бургер'")
    def test_transition_constructor_personal_account_page_transition_constructor(self, get_driver):
        main_page = MainPage(get_driver)
        password_recovery_page = PasswordRecoveryPage(get_driver)
        password_recovery_page.click_button_personal_account()
        assert main_page.click_constructor_button()

    @allure.title("Тест проверки перехода в ленту заказов")
    @allure.description("Тест проверяет переход на ленту заказов, проверка верный url")
    def test_transition_order_feed_open_page_order_feed(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.click_order_feed_button()
        current_url = main_page.get_current_url()
        assert current_url == Urls.ORDER_FEED

    @allure.title("Тест проверки нажатия на ингредиент")
    @allure.description("Тест проверяет что после нажатия на ингредиент открываются детали, проверка что есть надпись 'Детали ингредиента'")
    def test_click_ingredient_visible_detail_ingredient(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.click_ingredient()
        result = MessageText.DITAIL_INGREDIENT
        assert result in main_page.get_text_ditail_ingredient()

    @allure.title("Тест проверяет закрытие деталей ингредиента")
    @allure.description("Тест проверяет закрытие деталей об ингредиенте через крестик, проверка что 'Детали ингредиента' исчезли ")
    def test_close_detail_ingredient_detail_ingredient_not_displayed(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.click_ingredient()
        main_page.close_ditail_ingredient()
        main_page.check_close_ditail_ingredient()
        assert main_page.check_displayed_ingredient_detail() == False

    # Не срабатывает на firefox, в chrome все срабатывает правильно
    @allure.title("Тест проверки что при добавлении ингредиента счетчик увеличивается")
    @allure.description("Тест проверяет, если добавить ингредиент в заказ, счетчик ингредиента увеличится, проверка счетчик ингредиента увеличился")
    def test_increase_counter_add_ingredient_increase_counter_successful(self, get_driver):
        main_page = MainPage(get_driver)
        previous_counter = main_page.get_count_value()
        main_page.add_ingredient_to_order()
        actual_counter = main_page.get_count_value()
        assert actual_counter > previous_counter

    @allure.title("Тест проверки авторизованный пользователь может оформить заказ")
    @allure.description("Тест проверяет, что авторизованный пользователь может оформить заказ, проверка есть надпись 'Ваш заказ начали готовить'")
    def test_order_created_authorized_user_order_created_successful(self, get_driver, create_user):
        main_page = MainPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        main_page.click_button_personal_account()
        personal_account_page.authorization_user(create_user)
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        result = MessageText.ORDER_STARTED
        assert result == main_page.check_order_started()
