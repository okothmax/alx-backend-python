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
        conn = sqlite3.connect("users.db")  # Replace 'users.db' with your database file
        try:
            # Pass the connection to the wrapped function
            return func(conn, *args, **kwargs)
        finally:
            # Close the database connection
            conn.close()

    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetches a user by ID from the users table.
    :param conn: Database connection passed by the decorator.
    :param user_id: ID of the user to fetch.
    :return: The user's details as a tuple.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Example usage: Fetch user by ID with automatic connection handling
if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)
