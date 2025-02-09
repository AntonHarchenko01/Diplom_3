from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER = (By.XPATH, "//*[contains(@class, 'OrderHistory_link')]")
    COMPOUND = (By.XPATH, "//p[contains(text(),'Cостав')]")
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")
    COUNTER_ORDERS_ALL_TIME = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/p[2]")
    COUNTER_ORDERS_TODAY = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[3]/p[2]")
    ORDERS_IN_WORKS = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[1]")