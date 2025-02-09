import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Нажимаем на заказ в ленте заказов")
    def click_order(self):
        self.wait_element_clickable(OrderPageLocators.ORDER)
        self.click_element(OrderPageLocators.ORDER)

    @allure.step("Берем текст 'Состав' из Деталей заказа")
    def get_text_compound(self):
        return self.find_element(OrderPageLocators.COMPOUND).text

    @allure.step("Берем текст всех заказов в ленте заказов")
    def all_orders_text(self):
        self.wait_element_visible(OrderPageLocators.ALL_ORDERS)
        return self.get_text(OrderPageLocators.ALL_ORDERS)

    @allure.step("Берем число заказов за все время")
    def counter_orders_all_time(self):
        self.wait_element_visible(OrderPageLocators.COUNTER_ORDERS_ALL_TIME)
        return self.get_text(OrderPageLocators.COUNTER_ORDERS_ALL_TIME)

    @allure.title("Берем число заказов за сегодня")
    def counter_orders_today(self):
        self.wait_element_visible(OrderPageLocators.COUNTER_ORDERS_TODAY)
        return self.get_text(OrderPageLocators.COUNTER_ORDERS_TODAY)

    @allure.title("Ожидаем когда наш заказ появится в работе")
    def get_user_order(self, number):
        self.wait_text_in_element(OrderPageLocators.ORDERS_IN_WORKS, number)
        return self.get_text(OrderPageLocators.ORDERS_IN_WORKS)
