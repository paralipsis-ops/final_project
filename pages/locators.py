from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#login_form")
    REG = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p strong')
    NAME = (By.CSS_SELECTOR, 'h1')
    MESSAGE_NAME = (By.CSS_SELECTOR, 'div.alertinner strong')

