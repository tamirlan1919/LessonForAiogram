import sqlite3


def make_table_users():
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER UNIQUE,
                date_join DATETIME     
            )
        ''')
        conn.commit()


