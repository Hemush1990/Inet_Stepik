from .Locators import MainPagelocators
from .BasePage import BasePage
class BasketPage(BasePage):
    def check_basket_price(self):
        assert self.is_not_element_present(*MainPagelocators.basketprice), \
            "The basket price is active"

    def check_the_basket_message(self):
        assert self.is_not_element_present(*MainPagelocators.basketmessage), \
            "The basket isn\'t empty"
