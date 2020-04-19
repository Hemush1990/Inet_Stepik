import pytest
from Pages.BasePage import BasePage
from Pages.MainPage import MainPage
from Pages.Locators import BasePagelocators
from Pages.ProductPage import Product


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, BasePagelocators.LOGIN_LINK)
        page.open()
        page.go_to_login_page()


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, BasePagelocators.LOGIN_LINK_INVALID)
        page.open()
        page.should_be_login_link()
#чтобы запустить -pytest -m login_guest


