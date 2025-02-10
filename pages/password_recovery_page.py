import allure
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step("Нажимаем кнопку личный кабинет")
    def click_button_personal_account(self):
        self.wait_element_clickable(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Нажимаем 'Восстановить пароль'")
    def click_recovery_password(self):
        self.wait_element_clickable(PasswordRecoveryLocators.LINK_PASSWORD_RECOVERY)
        self.click_element(PasswordRecoveryLocators.LINK_PASSWORD_RECOVERY)

    @allure.step("Вводим email")
    def set_email(self, email):
        self.wait_element_clickable(PasswordRecoveryLocators.SET_EMAIL)
        self.click_element(PasswordRecoveryLocators.SET_EMAIL)
        self.set_text_to_element(PasswordRecoveryLocators.SET_EMAIL, email)

    @allure.step("Нажимаем кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element(PasswordRecoveryLocators.RESTORE_BUTTON)

    @allure.step("Ожидаем пока появится кнопка сохранить")
    def visible_save_button(self):
        self.wait_element_visible(PasswordRecoveryLocators.SAVE_BUTTON)

    @allure.step("Вводим новый пароль")
    def set_new_password(self, new_password):
        self.wait_element_clickable(PasswordRecoveryLocators.SET_NEW_PASSWORD)
        self.click_element(PasswordRecoveryLocators.SET_NEW_PASSWORD)
        self.set_text_to_element(PasswordRecoveryLocators.SET_NEW_PASSWORD, new_password)

    @allure.step("Нажимаем кнопку показать/скрыть пароль")
    def click_button_show_hide_password(self):
        self.click_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BUTTON)


    @allure.step("Ожидаем активности поля новый пароль")
    def input_password_status_active(self):
        return self.wait_element_visible(PasswordRecoveryLocators.INPUT_STATUS_ACTIVE)