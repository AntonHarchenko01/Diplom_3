import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем когда элемент станет кликабельным")
    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Нажимаем на элемент")
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Получаем текущий url")
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Вставить текст")
    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Ожидаем пока появится элемент")
    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Находим элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step("Проверяем невидимость элемента")
    def check_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step("Проверяем присутствие элемента на экране")
    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return  self.driver.find_element(*locator)

    @allure.step("Получаем текст локатора")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Перетащим ингредиент'")
    def drag_and_drop(self, locator1, locator2):
        drag = self.driver.find_element(*locator1)
        drop = self.driver.find_element(*locator2)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()

    @allure.step("Ожидаем появления текста в элементе")
    def wait_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 20).until(expected_conditions.text_to_be_present_in_element(locator, text))

