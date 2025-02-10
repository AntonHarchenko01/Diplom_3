from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LINK_PASSWORD_RECOVERY = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    SET_EMAIL = (By.XPATH, "//label[text()='Email']/../input")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    SET_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'icon-action')]")
    INPUT_STATUS_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
