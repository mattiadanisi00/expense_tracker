import sqlite3


def get_db():
    connection = sqlite3.connect('data.db')
    return connection


def init_db():
    db = get_db()
    cursor = db.cursor()

    # create expenses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    db.commit()
    db.close()

