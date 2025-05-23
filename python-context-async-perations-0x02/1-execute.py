import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params is not None else ()
        self.connection = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Let exceptions propagate

# Example usage
if __name__ == "__main__":
    # Ensure the table and data exist
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        cursor.execute("INSERT OR IGNORE INTO users (id, name, age) VALUES (1, 'Alice', 30)")
        cursor.execute("INSERT OR IGNORE INTO users (id, name, age) VALUES (2, 'Bob', 22)")
        conn.commit()

    # Use the context manager to execute the query
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with ExecuteQuery("users.db", query, params) as results:
        for row in results:
            print(row)