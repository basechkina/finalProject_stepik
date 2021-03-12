from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_no_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET), "Product is presented in basket, but should not be"

    def check_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)
