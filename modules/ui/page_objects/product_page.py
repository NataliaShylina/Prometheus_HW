from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from waiter import wait


class ProductPage(BasePage):
    ITEM = (By.CLASS_NAME, 'inventory_item')
    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_FLEECE_JACKET_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_link')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')

    def __init__(self, driver):
        super().__init__(driver)

    def add_sauce_labs_backpack_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_BACKPACK_TO_CART_BUTTON)
       
        wait(10)
        add_to_cart_button.click()

    def add_fleece_jacket_to_cart(self):
        add_fleece_jacket_to_cart_button = self.driver.find_element(*self.ADD_FLEECE_JACKET_TO_CART_BUTTON)
        add_fleece_jacket_to_cart_button.click()

    def get_item_price(self):
        return self.driver.find_elements(*self.ITEM_PRICE)[0].text
    
    def get_cart_badge_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
    
    def remove_sauce_labs_backpack_from_cart(self):
        remove_sauce_labs_backpack_from_cart_button = self.driver.find_element(*self.REMOVE_BUTTON)
        remove_sauce_labs_backpack_from_cart_button.click()

    def sort_items_by(self, option_value):
        sort_dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        sort_dropdown.click()
        sort_dropdown.find_element(By.CSS_SELECTOR, f"option[value='{option_value}']").click()
