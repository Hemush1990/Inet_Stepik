from selenium.common.exceptions import NoAlertPresentException
from .BasePage import BasePage
from .Locators import PrPage
from selenium.webdriver.common.by import By
import math
import time


class Product(BasePage):
    def add_item_to_basket(self):
        bask = self.browser.find_element(By.CSS_SELECTOR, "[value='Add to basket']")
        bask.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
            return True
        except NoAlertPresentException:
            print("No second alert presented")
            return False

    def should_be_second_alert(self):
        assert self.solve_quiz_and_get_code(), "second alert should be present"



    def check_item(self):
        item_name = self.browser.find_element(*PrPage.item_name).text
        basketite =self.browser.find_element(*PrPage.basketitem).text
        assert item_name == basketite, f"Not equal {item_name} and {basketite}"

    def check_price(self):
        price = self.browser.find_element(*PrPage.current_price).text
        basketpr = self.browser.find_element(*PrPage.basketprice).text
        assert price == basketpr, f"Different prices within {price} and {basketpr}"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PrPage.success_message), \
        "Success message is presented, but should not be"

    def product_is_disappeared(self):
        assert self.is_disappeared(*PrPage.success_message), \
        "Success message is presented, but should be disappeared"


