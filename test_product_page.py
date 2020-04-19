import pytest
from Pages.MainPage import MainPage
from Pages.ProductPage import Product
from Pages.LoginPage import LoginPage
from Pages.Locators import LoginPageLocators as LP
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks = pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])




class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(LP.password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = Product(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.check_item()
        page.check_price()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = Product(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.check_item()
        page.check_price()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = Product(browser, link)
        page.open()
        page.add_item_to_basket()
        page.should_not_be_success_message()

    def test_user_cant_see_success_message(self, browser, link):
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = Product(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = Product(browser, link)
        page.open()
        page.product_is_disappeared()

    def test_user_should_see_login_link_on_product_page(self, browser, link):
        # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_user_can_go_to_login_page_from_product_page(self, browser, link):
        # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = Product(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)
        page.open()
        page.open_basket_page()
        page.check_the_basket_message()
        page.check_basket_price()















    



