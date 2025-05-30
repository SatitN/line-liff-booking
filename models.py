import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userId TEXT,
            name TEXT,
            date TEXT,
            time TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()

    