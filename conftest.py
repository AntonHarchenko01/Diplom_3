import allure
import pytest
import requests
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from data.handles import Handles
from data.urls import Urls
from helpers import generate_data_user


@allure.step("Открываем браузер")
@pytest.fixture(params=["chrome", "firefox"], scope='function')
def get_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(Urls.MAIN_PAGE)
        driver.maximize_window()
    elif request.param== 'firefox':
        driver = webdriver.Firefox()
        driver.get(Urls.MAIN_PAGE)
        driver.maximize_window()
    else:
        raise ValueError('Unknown browser type')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def create_user():
    payload = generate_data_user()
    answer = requests.post(Handles.CREATE_USER, data=payload)
    token = answer.json().get("accessToken")
    yield payload, answer
    requests.delete(Handles.DELETE_USER, headers={"Authorization": f'{token}'})
