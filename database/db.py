import sqlite3
from config import DATABASE

def connect_db():
    return sqlite3.connect(DATABASE)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        category TEXT,
        priority TEXT,
        summary TEXT
    )
    """)

    conn.commit()
    conn.close()
