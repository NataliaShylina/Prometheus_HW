import pytest
from modules.common.database import Database
import time


@pytest.mark.database
def test_database_connection():
    db = Database()
    try:
        db.test_connection() # Connection successful, no assertion needed here
    except DatabaseConnectionError:  # Assuming I have a custom DatabaseConnectionError exception
        assert False, "Failed to connect to database"


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)
      
    assert users, "No users found in the database" # Assuming 'get_all_users' returns a list of user objects or dictionaries

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'  
    assert user[0][2] == '3127'  
    assert user[0][3] == 'Ukraine'      


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25    


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30  

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0     

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 2

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'  
    assert orders[0][2] == 'солодка вода'  
    assert orders[0][3] == 'з цукром'     

    #INDIVIDUAL_PART

@pytest.mark.database
def test_customer_insert():
    db = Database()
    customer = db.insert_customer(3, 'Natalia', 'Peremohy 2', 'Kyiv', 8122, 'Ukraine')
    city = db.select_customer_city_by_id(3)
    print("Новий кастомер", customer)

    assert city[0][0] == 'Kyiv'

@pytest.mark.database
def test_customer_city_update():
    db = Database()
    db.update_customer_city_by_id(3, 'Lviv')
    city = db.select_customer_city_by_id(3)

    assert city[0][0] == 'Lviv'  

@pytest.mark.database
def test_customers_data_is_not_null():
    db = Database()
    data = db.customers_data_is_not_empty()

    print(data)
      
    assert data, "Customer's data for important columns is not empty" 

@pytest.mark.database
def test_order_insert_by_date():
    db = Database()
    db.insert_order(3, 3, 3, '09:06:2024')
    db.insert_order(4, 4, 4, '09:06:2024')
    db.insert_order(5, 5, 5, '08:06:2024')
    db.insert_order(6, 6, 6, '08:06:2024')
    
    orders_0906 = db.select_orders_by_order_date('09:06:2024')
    orders_0806 = db.select_orders_by_order_date('08:06:2024')

    # Assertions for orders on '09:06:2024'
    assert len(orders_0906) == 2, "There should be 2 orders on '09:06:2024'"
    assert orders_0906[0][0] == 3, "First order ID on '09:06:2024' should be 3"
    assert orders_0906[1][0] == 4, "Second order ID on '09:06:2024' should be 4"

    # Assertions for orders on '08:06:2024'
    assert len(orders_0806) == 4, "There should be 4 orders on '08:06:2024'"
    assert orders_0806[0][0] == 1, "First order ID on '08:06:2024' should be 1"
    assert orders_0806[1][0] == 2, "Second order ID on '08:06:2024' should be 2"
    assert orders_0806[2][0] == 5, "Third order ID on '08:06:2024' should be 5"
    assert orders_0806[3][0] == 6, "Fourth order ID on '08:06:2024' should be 6"

    # Print statements for debugging
    print("Orders on 09:06:2024:", orders_0906)
    print("Orders on 08:06:2024:", orders_0806)

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    expected_number_of_orders = 6

    assert len(orders) == expected_number_of_orders, f"Expected {expected_number_of_orders} orders"

    for order in orders:
        print(order)

@pytest.mark.database
def test_get_order_info_for_appropriate_date():
    db = Database()

    db.insert_customer(4, 'Yuliia', 'Yabluneva 5', 'Vinnytsia', '12345', 'Ukraine')
    db.insert_customer(5, 'Kateryna', 'Vyshneva 6', 'Krakiv', '67890', 'Poland')
    db.insert_product(5, 'Сок', 'Апельсиновий', 7)
    db.insert_product(6, 'Морозиво', 'Ванільне', 10)     
    db.insert_order(4, 4, 5, '10:06:2024')
    db.insert_order(5, 5, 6, '10:06:2024')   

    orders_info = db.get_order_info_for_appropriate_date()

    # Assertions
    expected_orders_info = [
        (4, 'Yuliia', 'Сок', '10:06:2024'),
        (5, 'Kateryna', 'Морозиво', '10:06:2024')
    ]

    # Check that each expected order is in the orders_info
    for expected_order in expected_orders_info:
        assert expected_order in orders_info, f"Expected {expected_order} to be in {orders_info}"

    print("Orders info:", orders_info)

@pytest.mark.database
def test_get_customer_info_for_appropriate_country():
    db = Database()

    db.insert_customer(4, 'Yuliia', 'Yabluneva 5', 'Vinnytsia', '12345', 'Ukraina')
    db.insert_customer(5, 'Kateryna', 'Vyshneva 6', 'Krakiv', '67890', 'Poland')
    db.insert_customer(6, 'Maryna', 'Soborna 7', 'Krakiv', '54321', 'Poland')

    customers_info = db.get_customer_info_for_appropriate_country('Poland')

    expected_customers_info = [
        (5, 'Kateryna', 'Vyshneva 6', 'Krakiv', '67890', 'Poland'),
        (6, 'Maryna', 'Soborna 7', 'Krakiv', '54321', 'Poland')
    ]

    for expected_customer in expected_customers_info:
        assert expected_customer in customers_info, f"Expected {expected_customer} to be in {customers_info}"

    print("Customers info:", customers_info)

@pytest.mark.database
def test_search_for_products_with_keyword():
    db = Database()

    db.insert_product(7, 'Питна вода', 'негазована', 15)
    db.insert_product(8, 'Мінеральна вода', 'без газу', 12)

    products_with_water = db.search_for_products_with_keyword('вода')

    expected_products_with_water = [
        (7, 'Питна вода', 'негазована', 15),
        (8, 'Мінеральна вода', 'без газу', 12),
    ]

    for expected_product in expected_products_with_water:
        assert expected_product in products_with_water, f"Expected {expected_product} to be in {products_with_water}"

    print("Products with 'вода':", products_with_water)

@pytest.mark.database
def test_delete_product_that_is_not_in_demand():
    db = Database()

    db.insert_product(9, 'Молоко', 'жирність 1,5%', 20)

    db.delete_product(3)

    remaining_products = db.search_for_products_with_keyword('Молоко')

    expected_remaining_products = [
        (9, 'Молоко', 'жирність 1,5%', 20)
    ]

    # Assert the number of remaining products matches the expected number
    assert len(remaining_products) == len(expected_remaining_products), f"Expected {len(expected_remaining_products)} products, but got {len(remaining_products)}"

    # Assert each expected product is in the remaining products
    for expected_product in expected_remaining_products:
        assert expected_product in remaining_products, f"Expected {expected_product} to be in {remaining_products}"

    print("Remaining products after deletion:", remaining_products)    