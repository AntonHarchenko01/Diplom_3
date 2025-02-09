from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ASSEMBLE_BURGER_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    INGREDIENT = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[2]/ul[1]/a[2]/img[1]")
    DITAIL_INGREDIENT = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[2]//p[contains(@class, "num")]')
    BASKET_ORDER = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    YOU_ORDER_STARTED = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")