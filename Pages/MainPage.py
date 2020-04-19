from .BasePage import BasePage
from .Locators import MainPagelocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def open_basket_page(self):
        viewbask = self.browser.find_element(*MainPagelocators.viewbasket)
        viewbask.click()

    def check_basket_price(self):
        assert self.is_not_element_present(*MainPagelocators.basketprice), \
        "The basket price is active"


    def check_the_basket_message(self):
        assert self.is_not_element_present(*MainPagelocators.basketmessage), \
        "The basket isn\'t empty"



