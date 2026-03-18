import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price FLOAT
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    date TEXT
)
""")

# Insert data
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", [
    (1, "Alice", "Delhi"),
    (2, "Bob", "Mumbai"),
    (3, "Charlie", "Bangalore")
])

cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", [
    (1, "Laptop", 80000),
    (2, "Phone", 40000),
    (3, "Tablet", 30000)
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 1, 1, "2024-01-01"),
    (2, 2, 2, 2, "2024-01-02"),
    (3, 1, 3, 1, "2024-01-03")
])

conn.commit()
conn.close()

print("Database created successfully!")