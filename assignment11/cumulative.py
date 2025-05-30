import sqlite3
import pandas as pd
import plotly.express as px
import plotly.data as pldata
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('./db/lesson.db')
query = """
SELECT 
    o.order_id, 
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

df = pd.read_sql_query(query, conn)

conn.close()

def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()

df['cumulative_apply'] = df.apply(cumulative, axis=1)

df['cumulative'] = df['total_price'].cumsum()

print(df)

# Plot cumulative revenue vs order_id
df.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    figsize=(10, 6),
    color='green',
    legend=False
)

plt.title('Cumulative Revenue vs Order ID')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.show()



df = pldata.wind(return_type='pandas')

print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))

df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True)
df['strength'] = df['strength'].astype(float)


fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
    template='plotly',
    hover_data=['direction']
)


fig.write_html("wind.html")

print("Plot saved to wind.html — open it in a browser to verify it works.")

import webbrowser
webbrowser.open("wind.html")
