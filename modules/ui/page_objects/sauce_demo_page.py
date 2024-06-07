from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SauceDemoPage(BasePage):
    URL_SAUSE_DEMO = 'https://www.saucedemo.com'
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGO = (By.CLASS_NAME, "app_logo")
    
    def __init__(self) -> None:
        super().__init__()

    def open_sauce_demo(self):
        self.driver.get(SauceDemoPage.URL_SAUSE_DEMO)

    def login_to_sauce_demo(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.driver.find_element(*self.LOGO).is_displayed()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
