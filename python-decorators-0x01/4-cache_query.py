import sqlite3
import functools

query_cache = {}  # Dictionary to store cached query results

def with_db_connection(func):
    """
    A decorator that automatically opens and closes a database connection,
    passing the connection to the wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open the database connection
        conn = sqlite3.connect("users.db")
        try:
            # Pass the connection to the wrapped function
            return func(conn, *args, **kwargs)
        finally:
            # Close the database connection
            conn.close()

    return wrapper

def cache_query(func):
    """
    A decorator that caches the results of database queries.
    The cache key is based on the SQL query string.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the SQL query string from arguments
        query = kwargs.get('query') if 'query' in kwargs else args[1]
        
        # Check if the query is in the cache
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]
        
        # Execute the query and cache the result
        result = func(*args, **kwargs)
        query_cache[query] = result
        print("Caching result for query:", query)
        return result

    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetches users from the database based on the query, with caching.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Example Usage
if __name__ == "__main__":
    # First call will cache the result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print("First fetch:", users)

    # Second call will use the cached result
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print("Second fetch:", users_again)
