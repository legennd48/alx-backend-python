import sqlite3
import functools
import logging
from datetime import datetime

# Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(levelname)s - %(message)s'
# )

#### decorator to lof SQL queries

def log_queries(func):
    """Decorator to log SQL queries executed by the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0] if args else kwargs.get('query')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # logging.info(f"{now} - Executing query: {query}")
        print(f"{now} - Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")