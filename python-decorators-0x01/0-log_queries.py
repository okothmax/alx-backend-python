import sqlite3
import functools

def log_queries():
    """
    A decorator that logs the SQL query before executing it.
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

            # Log the SQL query
            print(f"Executing SQL Query: {query}")

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
    # Fetch users while logging the query
    users = fetch_all_users(query="SELECT * FROM users")
    print("Fetched Users:")
    print(users)
