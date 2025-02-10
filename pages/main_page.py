import allure

from locators.main_page_locators import MainPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажимаем на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.wait_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.wait_element_visible(MainPageLocators.ASSEMBLE_BURGER_TITLE)

    @allure.step("Нажимаем на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.wait_element_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_element_visible(MainPageLocators.ORDER_FEED_TITLE)

    @allure.step("Нажимаем на ингредиент")
    def click_ingredient(self):
        self.wait_element_clickable(MainPageLocators.INGREDIENT)
        self.click_element(MainPageLocators.INGREDIENT)
        self.wait_element_visible(MainPageLocators.DITAIL_INGREDIENT)

    @allure.step("Берем текст 'Детали заказа'")
    def get_text_ditail_ingredient(self):
        return self.find_element(MainPageLocators.DITAIL_INGREDIENT).text

    @allure.step("Закрываем детали ингредиента")
    def close_ditail_ingredient(self):
        self.wait_element_clickable(MainPageLocators.CLOSE_BUTTON)
        self.click_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step("Проверяем скрытость деталей ингредиентов")
    def check_close_ditail_ingredient(self):
        self.check_invisibility_element(MainPageLocators.DITAIL_INGREDIENT)

    @allure.step("Проверяем 'Детали ингредиента' на экране")
    def check_displayed_ingredient_detail(self) -> bool:
        return self.check_presence(MainPageLocators.DITAIL_INGREDIENT).is_displayed()

    @allure.step("Получаем значение счетчика ингредиента")
    def get_count_value(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Добавим ингредиент в заказ")
    def add_ingredient_to_order(self):
        self.wait_element_clickable(MainPageLocators.INGREDIENT)
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BASKET_ORDER)

    @allure.step("Нажимаем кнопку личный кабинет")
    def click_button_personal_account(self):
        self.wait_element_clickable(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Нажимаем кнопку оформить заказ")
    def click_order_button(self):
        self.wait_element_clickable(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_element_visible(MainPageLocators.YOU_ORDER_STARTED)

    @allure.step("Проверяем что заказ взяли в работу")
    def check_order_started(self):
        return self.get_text(MainPageLocators.YOU_ORDER_STARTED)