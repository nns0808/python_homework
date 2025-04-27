import pandas as pd
import sqlite3


with sqlite3.connect("./db/lesson.db") as conn:
    query = """
    SELECT c.customer_name, o.order_id, p.product_name
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id;
    """
    df = pd.read_sql_query(query, conn)
    print(df.head())

with sqlite3.connect("./db/lesson.db") as conn:
    query = """
    SELECT 
        li.line_item_id, 
        li.quantity, 
        li.product_id, 
        p.product_name, 
        p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id;
    """
    df = pd.read_sql_query(query, conn)
    print(df.head())

    df['total'] = df['quantity'] * df['price']
    print(df.head())

    grouped = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    })

    print(grouped.head())
print()
grouped = grouped.sort_values(by='product_name')
print(grouped.head())
print()

grouped.to_csv("assignment7/order_summary.csv", index=False)
