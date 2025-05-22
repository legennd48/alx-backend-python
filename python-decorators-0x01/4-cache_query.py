import time
import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    """Decorator to open and close a database connection automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def cache_query(func):
    """Decorator to cache query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Get the query string from args or kwargs
        if 'query' in kwargs:
            query = kwargs['query']
        else:
            # conn is the first arg, so query is the second
            query = args[0] if len(args) > 0 else None
        if query in query_cache:
            print("Using cached result for query.")
            return query_cache[query]
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")