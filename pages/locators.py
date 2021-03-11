from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE_BASKET = (By.XPATH, "//div[@id='messages']/div[1]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info p:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
