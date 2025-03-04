import sqlite3


def insert_to_booking(user_id, date_booking, guests, requirements, status):
    with sqlite3.connect('tbiliso.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO booking(user_id, date_booking, guests, requirements, status) VALUES (?, ?, ?, ?, ?)
        ''', (user_id, date_booking, guests, requirements, status))
        conn.commit()


def update_booking(user_id, status):
    with sqlite3.connect('tbiliso.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE booking SET status = ? WHERE user_id = ?', (status, user_id))
        conn.commit()

