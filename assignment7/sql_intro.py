import sqlite3
import pandas as pd

with  sqlite3.connect("db/magazines.db") as conn: 
    print("Database created and connected successfully.")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS magazines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    publisher_id INTEGER NOT NULL,
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subscribers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subscriber_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    expiration_date TEXT NOT NULL,
    FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id),
    UNIQUE (subscriber_id, magazine_id) -- optional: prevents duplicate subscriptions
);
""")

conn.commit()
conn.close()

# Connect to the database
conn = sqlite3.connect("db/magazines.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

def add_publisher(name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding magazine '{name}': {e}")

def add_subscriber(name, address):
    try:
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error adding subscription: {e}")
print()

# Add publishers
add_publisher("True Publishing")
add_publisher("World Group")
add_publisher("Most Readings")


# Add magazines
add_magazine("News", 1)
add_magazine("New Times", 2)
add_magazine("Nature", 3)


# Add subscribers
add_subscriber("Tom Cruz", "123 Park Dr")
add_subscriber("Tim Hangs", "444 Fort Ave")
add_subscriber("Sam Smitt", "765 Oak Blvd")

# Add subscriptions
add_subscription(1, 1, "2025-12-31")
add_subscription(1, 2, "2025-10-15")
add_subscription(2, 3, "2026-01-20")
add_subscription(3, 1, "2025-08-20")
add_subscription(3, 2, "2025-09-01")

conn.commit()

cursor = conn.execute("SELECT * FROM subscribers")
for row in cursor:
    print(row)
print()

cursor = conn.execute("SELECT * FROM magazines ORDER BY name")
for row in cursor:
    print(row)
print()

cursor = conn.execute("""
    SELECT magazines.*
    FROM magazines
    JOIN publishers ON magazines.publisher_id = publishers.id
    WHERE publishers.name = ?
""", ("Penguin Publishing",))
for row in cursor:
    print(row)
print()

# Retrieve and print all subscribers
print("\nAll subscribers:")
cursor = conn.execute("SELECT * FROM subscribers")
for row in cursor:
    print(row)
print()

# Retrieve and print all magazines sorted by name
print("\nAll magazines sorted by name:")
cursor = conn.execute("SELECT * FROM magazines ORDER BY name")
for row in cursor:
    print(row)
print()

# Retrieve and print all magazines for a specific publisher
publisher_name = "Time Media Group"
print(f"\nMagazines published by {publisher_name}:")
cursor = conn.execute("""
    SELECT magazines.*
    FROM magazines
    JOIN publishers ON magazines.publisher_id = publishers.id
    WHERE publishers.name = ?
""", (publisher_name,))
for row in cursor:
    print(row)
