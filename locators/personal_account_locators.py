from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    AUTHORIZATION_MAIL = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    AUTHORIZATION_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    AUTHORIZATION_BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    INSCRIPTION_ENTRANCE = (By.XPATH, "//h2[contains(text(),'Вход')]")