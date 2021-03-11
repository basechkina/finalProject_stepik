from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BASKET), "Product was not added to basket!"

    def check_product_name_in_message(self):
        text_success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert product_name in text_success_message, "Product name is no the same!"

    def check_product_price_in_message(self):
        text_price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert text_price_message == product_price, "Price is wrong!"
