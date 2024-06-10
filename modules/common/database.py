import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/andriishylin/folder1/Prometheus_HW' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers" 
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}' "    
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = '{product_id}' "    
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()    

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
     #INDIVIDUAL_PART

    def insert_customer(self, id, name, address, city, postal_code, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) VALUES ({id}, '{name}', '{address}', '{city}', {postal_code}, '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def select_customer_city_by_id(self, id):
        query = f"SELECT city FROM customers WHERE id = '{id}' "    
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    

    def update_customer_city_by_id(self, id, city):
        query = f"UPDATE customers SET city = '{city}' WHERE id = '{id}' "
        self.cursor.execute(query)
        self.connection.commit()

    def customers_data_is_not_empty(self):
        query = "SELECT address, city, postalCode, country FROM customers \
            WHERE city = 'Lviv' AND country IS NOT NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record    
    
    def insert_order(self, id, customer_id, product_id, order_date):
        query = "INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (id, customer_id, product_id, order_date))
        self.connection.commit()

    def select_orders_by_order_date(self, order_date):
        query = "SELECT * FROM orders WHERE order_date = ?"    
        self.cursor.execute(query, (order_date,))
        records = self.cursor.fetchall()
        return records
    
    def get_order_info_for_appropriate_date(self):
        query = "SELECT orders.id, customers.name, products.name, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    