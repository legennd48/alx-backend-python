import mysql.connector
import csv
import uuid

def connect_db():
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            password='',
            user='root'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def create_database(connection):
    """Create the database and tables."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def create_table(connection):
    """Create user_data table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY UUID,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        );
    """)
    connection.commit()
    print("Table created successfully.")
    cursor.close()

def insert_data(connection, file_path):
    """Insert data into user_data table from csv file."""
    cursor = connection.cursor()
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for line in reader:
            user_id = str(uuid.uuid4())  # Generate a new UUID
            try:
                cursor.execute("""
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, line['name'], line['email'], line['age']))
            except mysql.connector.Error as err:
                print(f"Error inserting row: {err}")
    connection.commit()
    cursor.close()