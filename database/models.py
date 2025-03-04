import sqlite3


def make_table():
    with sqlite3.connect('tbiliso.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS booking(
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            date_booking TEXT,
            guests INTEGER,
            requirements TEXT,
            status TEXT
        )
        ''')
        conn.commit()