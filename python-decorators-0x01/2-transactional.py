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

def transactional(func):
    """
    A decorator that ensures a function's database operations are wrapped in a transaction.
    Commits the transaction if the function succeeds; rolls back if an error occurs.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the wrapped function
            result = func(conn, *args, **kwargs)
            # Commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # Roll back the transaction on error
            conn.rollback()
            print(f"Transaction failed: {e}")
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Updates a user's email in the database.
    :param conn: Database connection passed by the decorator.
    :param user_id: ID of the user to update.
    :param new_email: New email to set.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Example usage: Update user's email with automatic transaction handling
if __name__ == "__main__":
    try:
        update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
        print("User email updated successfully.")
    except Exception as e:
        print(f"Error: {e}")
