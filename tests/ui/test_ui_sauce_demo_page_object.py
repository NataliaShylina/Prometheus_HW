import pytest
from modules.ui.page_objects.sauce_demo_page import SauceDemoPage
from modules.ui.page_objects.product_page import ProductPage

@pytest.mark.saucedemo
class TestSauceDemo:

    @pytest.fixture(autouse=True)
    def test_check_login_to_website_page_object(self, driver):
        self.sauce_demo_page = SauceDemoPage(driver)
        self.product_page = ProductPage(driver)

        self.sauce_demo_page.open_sauce_demo()
        self.sauce_demo_page.login_to_sauce_demo("standard_user", "secret_sauce")
        assert self.sauce_demo_page.check_title("Swag Labs")

    def test_login_success(self):
        assert self.sauce_demo_page.is_logged_in()

    def test_add_item_to_cart(self):
        self.product_page.add_sauce_labs_backpack_to_cart()
        assert self.product_page.get_cart_badge_count() == "1"

    def test_remove_item_from_cart(self):
        self.product_page.remove_sauce_labs_backpack_from_cart()
        assert self.product_page.get_cart_badge_count() == ""

    def test_sort_items_by_price_low_to_high(self):
        self.product_page.sort_items_by("lohi")
        first_price = self.product_page.get_item_price()
        assert first_price == "$7.99"  # Expected price for the cheapest item

    def test_cart_badge_number_after_adding_items(self):
        self.product_page.add_sauce_labs_backpack_to_cart()
        self.product_page.add_fleece_jacket_to_cart()  # Add a second item
        assert self.product_page.get_cart_badge_count() == "2"   