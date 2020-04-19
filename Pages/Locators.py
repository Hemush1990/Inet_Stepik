from selenium.webdriver.common.by import By
class PrPage(object):
    basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    current_price = (By.CSS_SELECTOR, ".product_main  .price_color")
    item_name = (By.CSS_SELECTOR, ".product_main h1")
    basketitem = (By.CSS_SELECTOR, ".alert:first-of-type strong")
    basketprice = (By.CSS_SELECTOR,".alert:last-child strong" )
    success_message = (By.CSS_SELECTOR, ".alert:first-of-type")



class MainPagelocators(object):
    viewbasket = (By.LINK_TEXT, "View basket")
    basketmessage = (By.CSS_SELECTOR, "#content_inner")
    basketprice = (By.CSS_SELECTOR, "div h2.col-sm-6")

class LoginPageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    password = '1234567test'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    Reg_email = (By.CSS_SELECTOR, "[name = registration-email]")
    Reg_password = (By.CSS_SELECTOR, "[name = registration-password1]")
    Reg_password2 = (By.CSS_SELECTOR, "[name = registration-password2]")
    Reg_submit = (By.CSS_SELECTOR, "[name = registration_submit")


