import time
import sqlite3
import functools

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

def retry_on_failure(retries=3, delay=2):
    """
    A decorator that retries the decorated function if it raises an exception.
    :param retries: Number of retry attempts.
    :param delay: Delay (in seconds) between retries.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    # Try executing the function
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            # If all retries fail, raise the last exception
            print("All retries failed.")
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetches all users from the database, with retry handling for transient errors.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Example usage: Attempt to fetch users with automatic retry on failure
if __name__ == "__main__":
    try:
        users = fetch_users_with_retry()
        print(users)
    except Exception as e:
        print(f"Error: {e}")
