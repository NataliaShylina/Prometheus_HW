import pytest
from modules.ui.page_objects.main_page_rozetka import MainPageRozetka
from modules.ui.page_objects.item_page import ItemPage

@pytest.fixture
def main_page_rozetka(driver):
    return MainPageRozetka(driver)

@pytest.fixture
def item_page(driver):
    return ItemPage(driver)
"""
@pytest.mark.rozetka
def test_choose_item_on_main_page_page_object():
    main_page_rozetka = MainPageRozetka()

    main_page_rozetka.go_to_rozetka()
    main_page_rozetka.choose_element_purina_gourmet()
    assert main_page_rozetka.check_title("Упаковка вологого корму для кішок Purina Gourmet Gold Паштет з куркою 24 шт по 85 г")
    main_page_rozetka.close()
"""
@pytest.mark.rozetka
def test_open_main_page(main_page_rozetka):
    main_page_rozetka.go_to_rozetka()
    assert "ROZETKA" in main_page_rozetka.driver.title

@pytest.mark.rozetka
def test_choose_item(main_page_rozetka, item_page):
    main_page_rozetka.go_to_rozetka()
    main_page_rozetka.search_for_item("Purina Gourmet Gold")

    assert "Purina Gourmet Gold" in item_page.get_item_title()

@pytest.mark.rozetka
def test_check_price_and_title(main_page_rozetka, item_page):
    main_page_rozetka.go_to_rozetka()
    main_page_rozetka.search_for_item("Purina Gourmet Gold")

    title = item_page.get_item_title()
    price = item_page.get_item_price()

    assert "Purina Gourmet Gold" in title
    assert price.startswith("₴")  # Assuming the price is in Ukrainian Hryvnia

@pytest.mark.rozetka
def test_add_item_to_cart(main_page_rozetka, item_page):
    main_page_rozetka.go_to_rozetka()
    main_page_rozetka.search_for_item("Purina Gourmet Gold")

    item_page.add_to_cart()
    cart_count = item_page.get_cart_count()

    assert cart_count == "1"  # Assuming the cart count should be 1 after adding one item