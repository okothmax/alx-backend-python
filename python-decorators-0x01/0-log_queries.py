import sqlite3
import functools
from datetime import datetime  # Importing datetime for timestamp

def log_queries():
    """
    A decorator that logs the SQL query and its execution timestamp before executing it.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Extract the SQL query from the function arguments
            if 'query' in kwargs:
                query = kwargs['query']
            elif args:
                query = args[0]
            else:
                query = "Unknown Query"

            # Log the SQL query with a timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Executing SQL Query: {query}")

            # Execute the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    """
    Fetches all users from the database using the given query.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Example Usage
if __name__ == "__main__":
    # Fetch users while logging the query and timestamp
    users = fetch_all_users(query="SELECT * FROM users")
    print("Fetched Users:")
    print(users)
