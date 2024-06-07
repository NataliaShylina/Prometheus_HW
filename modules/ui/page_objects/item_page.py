from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ItemPage():
    ITEM_TITLE = (By.CSS_SELECTOR, ".product__title")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product-prices__big")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".buy-button")
    CART_COUNT = (By.CSS_SELECTOR, ".header-actions__button-counter")
    
    def __init__(self, driver):
        self.driver = driver

    def get_item_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ITEM_TITLE)).text

    def get_item_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ITEM_PRICE)).text

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    def get_cart_count(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_COUNT)).text