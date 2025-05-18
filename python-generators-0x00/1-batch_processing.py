import mysql.connector
import os


def stream_users_in_batches(batch_size):
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
    for i in range(0, len(rows), batch_size):
        batch = [dict(zip(columns, row)) for row in rows[i:i + batch_size]]
        yield batch
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process user data in batches."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 30:
                print(user) 

    
