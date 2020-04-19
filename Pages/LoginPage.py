from .BasePage import BasePage
from .Locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def go_to_login_page(self):
     link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
     link.click()


    def should_be_login_link(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_LINK_INVALID), "Login link is not presented"

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), "User icon is not presented"

    def register_new_user(self, password):
        mail = self.browser.find_element(*LoginPageLocators.Reg_email)
        mail.send_keys(str(time.time()) + "@fakemail.org")
        pwd = self.browser.find_element(*LoginPageLocators.Reg_password)
        pwd.send_keys(password)
        confirm_pwd = self.browser.find_element(*LoginPageLocators.Reg_password2)
        confirm_pwd.send_keys(password)
        self.browser.find_element(*LoginPageLocators.Reg_submit).click()
        time.sleep(5)
        self.should_be_authorized_user()
