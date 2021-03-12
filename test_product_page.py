import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
main_page_url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_success_message()
    page.check_product_name_in_message()
    page.check_product_price_in_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.add_product_to_basket()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, main_page_url)
    page.open()
    page.go_to_basket_page()
    page.check_no_products_in_basket()
    page.check_empty_basket()
