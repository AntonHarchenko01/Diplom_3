import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import get_driver, create_user
from pages.personal_account_page import PersonalAccountPage


class TestOrder:
    @allure.title("Тест проверки открытия деталей о заказе")
    @allure.description("Тест проверяет, что при нажатии на заказ в ленте заказов, открываются детали заказа, проверка что есть 'Состав'")
    def test_open_ditail_order_open_compound_order(self, get_driver):
        main_page = MainPage(get_driver)
        order_page = OrderPage(get_driver)
        main_page.click_order_feed_button()
        order_page.click_order()
        result = "Cостав"
        assert result in order_page.get_text_compound()

    @allure.title("Тест проверки, что заказ пользователя отображается в ленте заказов")
    @allure.description("Тест проверяет, что созданный заказ отображается в ленте заказов, проверка номер заказа есть в ленте заказов")
    def test_create_order_in_order_feed_create_order_number_order_in_order_feed(self, get_driver, create_user):
        main_page = MainPage(get_driver)
        order_page = OrderPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        main_page.click_button_personal_account()
        number = personal_account_page.authorization_and_create_order(create_user)
        number = "#0" + number
        main_page.click_order_feed_button()
        all_orders = order_page.all_orders_text()
        assert number in all_orders

    @allure.title("Тест проверки, что при созданном заказе счетчик за все время увеличивается")
    @allure.description("Тест проверяет, что при создании заказа, счетчик за все время увеличивается, проверка актуальный счетчик больше предыдущего")
    def test_counter_all_time_orders_increases_create_order_counter_orders_increases_successful(self, get_driver, create_user):
        main_page = MainPage(get_driver)
        order_page = OrderPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        main_page.click_order_feed_button()
        previous_counter = order_page.counter_orders_all_time()
        main_page.click_button_personal_account()
        personal_account_page.authorization_and_create_order(create_user)
        main_page.click_order_feed_button()
        actual_counter = order_page.counter_orders_all_time()
        assert actual_counter > previous_counter

    @allure.title("Тест проверка, что при созданном заказе счетчик за сегодня увеличивается")
    @allure.description("Тест проверяет, что при создании заказа, счетчик за сегодня увеличивается, проверка актуальный счетчик больше предыдущего")
    def test_counter_today_orders_increases_create_order_counter_orders_increases_successful(self, get_driver, create_user):
        main_page = MainPage(get_driver)
        order_page = OrderPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        main_page.click_order_feed_button()
        previous_counter = order_page.counter_orders_today()
        main_page.click_button_personal_account()
        personal_account_page.authorization_and_create_order(create_user)
        main_page.click_order_feed_button()
        actual_counter = order_page.counter_orders_today()
        assert actual_counter > previous_counter

    @allure.title("Тест проверка, что при созданном заказе он попадает в работу")
    @allure.description("Тест проверяет, что при создании заказа, он попадает в работу на ленте заказов, проверка номер созданного заказа есть в работе")
    def test_order_in_work_create_order_number_order_in_work(self, get_driver, create_user):
        main_page = MainPage(get_driver)
        order_page = OrderPage(get_driver)
        personal_account_page = PersonalAccountPage(get_driver)
        main_page.click_button_personal_account()
        number = personal_account_page.authorization_and_create_order(create_user)
        number = "0" + number
        main_page.click_order_feed_button()
        in_work = order_page.get_user_order(number)
        assert number in in_work