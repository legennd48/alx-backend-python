import mysql.connector
import os

def stream_user_ages():
    """Generator function to stream user ages from the user_data table."""
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    rows = cursor.fetchall()
    for row in rows:
        yield row['age']


def calculate_average_age():
    """
    Calculate the average age of the users,
    usin g the generator - stream_user_age.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count == 0:
        return 0
    return total_age / count


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"The average age of users is: {average_age}")