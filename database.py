import sqlite3
from datetime import datetime
file = "database.db"
conn = sqlite3.connect(file)
print("Database Sqlite3.db formed.")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, type TEXT NOT NULL)''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS time_logs (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  duration REAL NOT NULL,
                  date TEXT NOT NULL,
                  category_id INTEGER,
                  FOREIGN KEY (category_id) REFERENCES categories (id))
  ''')

cursor.execute("SELECT * FROM categories")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()

def add_category(category_name, category_type):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO categories (name, type) VALUES (?, ?)", (category_name, category_type))

        conn.commit()
        print(f"Category '{category_name}' added successfully")
    except sqlite3.IntegrityError:
        print("Error: That category name already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

#get categories to dsiplay
def get_categories():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM categories")

    rows = cursor.fetchall()

    conn.close()

    # convert tuples into strings
    categories = [row[0] for row in rows]

    return categories

def get_category_id(category_name):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM categories WHERE name = ?",(category_name,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None

#add timer logs to database
def log_time(duration, category_id,):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO time_logs (duration, date, category_id) VALUES (?, ?, ?)", (duration, datetime.now(), category_id))
    conn.commit()
    conn.close()

