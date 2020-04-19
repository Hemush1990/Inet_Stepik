from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import math

class BasePage(object):

    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True






