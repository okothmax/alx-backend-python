import mysql.connector

def connect_to_prodev():
    """
    Connects to the ALX_prodev database and returns the connection object.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="orain",
            password="CasablancaHero23@",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

def stream_users():
    """
    A generator function that fetches rows from the user_data table one by one.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for better readability
    try:
        # Fetch all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row  # Yield each row one by one
    finally:
        cursor.close()
        connection.close()

# Example usage
if __name__ == "__main__":
    for user in stream_users():
        print(user)  # Streams rows one at a time
