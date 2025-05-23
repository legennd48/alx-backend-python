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
            self.connection.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True

# Example usage
if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        # selecet all users
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
        