import sqlite3


def insert_to_table_users(telegram_id, date_join):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users(telegram_id, date_join)
        VALUES(?, ?)
        ''', (telegram_id, date_join))
        conn.commit()


def get_user_by_id(telegram_id):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE telegram_id = ?
        ''', (telegram_id, ))
        user = cursor.fetchone()
        return user or None


def get_users():
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users
        ''')
        users = cursor.fetchall()
        return users