from selenium.webdriver.common.by import By
class PrPage(object):
    basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    current_price = (By.CSS_SELECTOR, ".product_main  .price_color")
    item_name = (By.CSS_SELECTOR, ".product_main h1")
    basketitem = (By.CSS_SELECTOR, ".alert:first-of-type strong")
    basketprice = (By.CSS_SELECTOR,".alert:last-child strong" )
