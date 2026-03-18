import sqlite3

def get_connection():
    return sqlite3.connect()

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_schema():
    return """
    Tables:
    customers(id, name, city)
    products(id, name, price)
    orders(id, customer_id, product_id, quantity, date)
    """