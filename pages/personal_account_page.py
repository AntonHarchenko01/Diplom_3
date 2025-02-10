import allure
from conftest import create_user
from helpers import create_order
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step("Авторизация пользователя")
    def authorization_user(self, create_user):
        payload, answer = create_user
        self.set_text_to_element(PersonalAccountLocators.AUTHORIZATION_MAIL, payload["email"])
        self.set_text_to_element(PersonalAccountLocators.AUTHORIZATION_PASSWORD, payload["password"])
        self.click_element(PersonalAccountLocators.AUTHORIZATION_BUTTON_LOGIN)
        self.wait_element_visible(MainPageLocators.CREATE_ORDER_BUTTON)
        return payload["email"], payload["password"]

    @allure.step("Нажимаем кнопку 'История заказов'")
    def click_history_order_button(self):
        self.wait_element_clickable(PersonalAccountLocators.HISTORY_ORDER_BUTTON)
        self.click_element(PersonalAccountLocators.HISTORY_ORDER_BUTTON)

    @allure.step("Нажимаем кнопку 'Выход' из аккаунта")
    def click_logout_button(self):
        self.wait_element_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)
        return self.wait_element_visible(PersonalAccountLocators.INSCRIPTION_ENTRANCE)

    @allure.step("Авторизуемся и сделаем заказ")
    def authorization_and_create_order(self, create_user):
        payload, answer = create_user
        number = create_order(answer)
        number = str(number.json()['order']['number'])
        return number
