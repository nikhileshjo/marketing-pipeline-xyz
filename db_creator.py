import sqlite3
import random

DB_NAME = "Data Engineer_ETL Assignment.db"

def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Exception as e:
        print(f"Connection error: {e}")
        return None


def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY,
            age INTEGER NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sales (
            sales_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            sales_id INTEGER,
            item_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        );
        """)

        conn.commit()

    except Exception as e:
        print(f"Table creation error: {e}")


def insert_items(conn):
    try:
        cursor = conn.cursor()

        items = [
            (1, 'x'),
            (2, 'y'),
            (3, 'z')
        ]

        cursor.executemany("INSERT OR IGNORE INTO Items VALUES (?, ?);", items)
        conn.commit()

    except Exception as e:
        print(f"Insert items error: {e}")


def insert_customers(conn, num_customers=5):
    try:
        cursor = conn.cursor()

        customers = []
        for i in range(1, num_customers + 1):
            age = random.randint(18, 50)
            customers.append((i, age))

        cursor.executemany("INSERT OR IGNORE INTO Customer VALUES (?, ?);", customers)
        conn.commit()

    except Exception as e:
        print(f"Insert customers error: {e}")


def insert_sales(conn, num_sales=10, num_customers=5):
    try:
        cursor = conn.cursor()

        sales = []
        for i in range(1, num_sales + 1):
            customer_id = random.randint(1, num_customers)
            sales.append((i, customer_id))

        cursor.executemany("INSERT OR IGNORE INTO Sales VALUES (?, ?);", sales)
        conn.commit()

    except Exception as e:
        print(f"Insert sales error: {e}")


def insert_orders(conn, num_orders=30, num_sales=10):
    try:
        cursor = conn.cursor()

        orders = []
        for i in range(1, num_orders + 1):
            sales_id = random.randint(1, num_sales)
            item_id = random.randint(1, 3)

            # Randomly assign NULL quantity (not purchased)
            quantity = random.choice([None, random.randint(1, 5)])

            orders.append((i, sales_id, item_id, quantity))

        cursor.executemany(
            "INSERT OR IGNORE INTO Orders VALUES (?, ?, ?, ?);",
            orders
        )

        conn.commit()

    except Exception as e:
        print(f"Insert orders error: {e}")


def main():
    conn = create_connection()

    if conn:
        create_tables(conn)
        insert_items(conn)
        insert_customers(conn)
        insert_sales(conn)
        insert_orders(conn)

        print("Database created and populated successfully!")
        conn.close()


if __name__ == "__main__":
    main()
