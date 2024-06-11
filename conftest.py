import pytest
from modules.api.clients.github import GitHub
from selenium import webdriver

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Natalia'
        self.second_name = 'Shylina'

    def remove(self):
        self.name = ' '
        self.second_name = ' '    


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  
    driver.implicitly_wait(10)
    yield driver
    driver.quit()    