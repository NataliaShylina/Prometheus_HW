from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ITEM = (By.CLASS_NAME, "inventory_item")
    #ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    #REMOVE_BUTTON = (By.CLASS_NAME, "btn_secondary")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def add_sauce_labs_backpack_to_cart(self):
        self.driver.find_elements(*self.ADD_TO_CART_BUTTON)[0].click()

    def get_item_price(self):
        return self.driver.find_elements(*self.ITEM_PRICE)[0].text
    
    def get_cart_badge_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
    
    def remove_sauce_labs_backpack_from_cart(self):
        self.driver.find_elements(*self.REMOVE_BUTTON)[0].click()

    def sort_items_by(self, option_value):
        sort_dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        sort_dropdown.click()
        sort_dropdown.find_element(By.CSS_SELECTOR, f"option[value='{option_value}']").click()