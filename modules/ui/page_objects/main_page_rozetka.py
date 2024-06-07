#from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPageRozetka():
    URL_ROZETKA = 'https://rozetka.com.ua/ua/'
    SEARCH_BOX = (By.NAME, "search")
    #SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-form__submit")
    
    """def __init__(self) -> None:
        super().__init__()"""

    def __init__(self, driver):
        self.driver = driver

    def go_to_rozetka(self):
        self.driver.get(MainPageRozetka.URL_ROZETKA)

    def search_for_item(self, item_name):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(item_name)
        # search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        # search_button.click()
        search_box.send_keys(Keys.RETURN)

    """
    def choose_element_purina_gourmet(self):
        element_purina_gourmet = self.driver.find_element(By.CLASS_NAME, "tile__inner") 
        element_purina_gourmet.click()

    def check_title(self, expected_title_rozetka):
        return self.driver.title == expected_title_rozetka
    
    def check_price(self, expected_price):
        return self.driver.title == expected_price
    """    