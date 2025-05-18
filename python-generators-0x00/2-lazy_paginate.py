import mysql.connector
import os

def paginate_users(page_size, offset):
    """function to paginate users from the user_data table."""
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator function to paginate users from the user_data table."""
    offset = 0
    while True:
        batch = paginate_users(page_size, offset)
        if not batch:
            break
        yield batch
        offset += page_size