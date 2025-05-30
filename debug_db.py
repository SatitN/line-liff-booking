# debug_db.py

import sqlite3

def show_bookings():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()

    print("=== Bookings Table ===")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    show_bookings()
