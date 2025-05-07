import sqlite3

conn = sqlite3.connect('./db/lesson.db')
cursor = conn.cursor()

sql = """
SELECT customer_name, order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;
"""

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
print()

conn.close()

conn = sqlite3.connect('C:/Users/nns08/python_class/working/python_homework/db/lesson.db')

conn = sqlite3.connect("./db/lesson.db")
cursor = conn.cursor()

query = """
SELECT 
    o.order_id,
    SUM(li.quantity * p.price) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

print("First 5 orders and their total prices:")
for order_id, total_price in results:
    print(f"Order ID: {order_id}, Total Price: ${total_price:.2f}")
print()

conn.close()


conn = sqlite3.connect("./db/lesson.db")
cursor = conn.cursor()
query = """
SELECT 
    c.customer_name, 
    AVG(o_summary.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        o.order_id,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS o_summary ON c.customer_id = o_summary.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query)
rows = cursor.fetchall()

for customer_name, avg_price in rows:
    print(f"{customer_name}: ${avg_price:.2f}" if avg_price is not None else f"{customer_name}: No orders")

conn.close()
print()

import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    try:
        conn.execute("BEGIN")

        # Get customer_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Ivanov",))
        customer_id = cursor.fetchone()[0]

        # Get employee_id
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Ivan", "Ivanov"))
        employee_id = cursor.fetchone()[0]


        # Get product_ids of 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert a new order and get the order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING order_id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        # Insert line items for the order (10 of each product)
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, product_id, 10))

        conn.commit()

        # Retrieve and display the order's line items
        cursor.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
        """, (order_id,))
        print(f"\nLine items for order {order_id}:")
        for row in cursor.fetchall():
            print(row)
        print()

    except Exception as e:
        conn.rollback()
        print("Transaction failed:", e)
        


import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.execute("""
        SELECT e.first_name, e.last_name, COUNT(*) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(*) > 5;
    """)
    for row in cursor:
        print(row)



