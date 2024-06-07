import pytest
from modules.ui.page_objects.sauce_demo_page import SauceDemoPage
from modules.ui.page_objects.product_page import ProductPage

@pytest.mark.saucedemo
class TestSauceDemo:

    def test_check_login_to_website_page_object():
        sauce_demo_page = SauceDemoPage()
        sauce_demo_page = ProductPage()

        sauce_demo_page.open_sauce_demo()
        sauce_demo_page.login_to_sauce_demo("standard_user", "sauce_demo")
        assert sauce_demo_page.check_title("Swag Labs")
        sauce_demo_page.close