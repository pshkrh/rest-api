import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS orders (order_no INTEGER PRIMARY KEY, product_code text, name text, quantity text, price text, delivery_date text, currency text)"
cursor.execute(create_table)

connection.commit()
connection.close()