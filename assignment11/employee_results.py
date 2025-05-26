import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('./db/lesson.db')

query = """
SELECT 
    e.*, 
    o.order_id, 
    o.date AS order_date, 
    li.product_id, 
    li.quantity, 
    p.product_name, 
    p.price
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
"""

employee_results = pd.read_sql_query(query, conn)


print(employee_results.head())

query = """
SELECT 
    e.last_name, 
    SUM(p.price * l.quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id
"""

employee_results = pd.read_sql_query(query, conn)
print(employee_results)

conn.close()

employee_results.plot(
    x='last_name',
    y='revenue',
    kind='bar',
    legend=False,
    color='skyblue',
    figsize=(10, 6)
)

plt.title('Revenue by Employee', fontsize=16)
plt.xlabel('Employee Last Name', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


