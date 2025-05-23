"""
Objective: create a class based context manager
to handle opening and closing database connections
automatically
"""
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # open a database connection with specified db
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # close the database connection
        if self.connection:
            if exc_type is None:
                # commit the transaction if no exception occurred
                self.connection.commit()
            self.connection.close()  # Always close the connection
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True

# Example usage
if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        # Create the users table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        # Optionally insert a test user if table is empty
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        # select all users
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(user)
