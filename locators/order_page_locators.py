from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER = (By.XPATH, "//*[contains(@class, 'OrderHistory_link')]")
    COMPOUND = (By.XPATH, "//p[contains(text(),'Cостав')]")
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")
    COUNTER_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_WORKS = By.CSS_SELECTOR, "[class='OrderFeed_orderStatusBox__1d4q2 mb-15']"