import mysql.connector
import os

# def connect_to_database():
#     """Connect to the MySQL database and return the connection object."""
#     try:
#         connection = mysql.connector.connect(
#             host=os.getenv('DB_HOST'),
#             user=os.getenv('DB_USER'),
#             password=os.getenv('DB_PASSWORD'),
#             database=os.getenv('DB_NAME')
#         )
#         return connection
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None
    
def stream_users():
    """Generator function to stream users from the user_data table."""
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")
    if cursor.description is None:
        print("No data found in the user_data table.")
        return
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    for row in rows:
        yield dict(zip(columns, row))
    cursor.close()
    connection.close()


# stream_users = stream_users

import sys
sys.modules[__name__] = stream_users