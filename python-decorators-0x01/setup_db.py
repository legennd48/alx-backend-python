import sqlite3

def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    # Insert dummy data
    users = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('charlie', 'charlie@example.com'),
        ('david', 'david@example.com'),
        ('eve', 'eve@example.com'),
        ('frank', 'frank@example.com'),
        ('grace', 'grace@example.com'),
        ('heidi', 'heidi@example.com'),
        ('ivan', 'ivan@example.com'),
        ('judy', 'judy@example.com'),
        ('mallory', 'mallory@example.com'),
        ('niaj', 'niaj@example.com'),
        ('oscar', 'oscar@example.com'),
        ('peggy', 'peggy@example.com'),
        ('trent', 'trent@example.com')
    ]
    cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)
    conn.commit()
    conn.close()
    print("Database setup complete with dummy data.")

if __name__ == "__main__":
    setup_database()