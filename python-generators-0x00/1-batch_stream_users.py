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

def stream_users_in_batches(batch_size):
    """
    A generator function that fetches rows from the user_data table in batches.

    :param batch_size: Number of rows to fetch in each batch.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for readability
    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            # Fetch the next batch of rows
            rows = cursor.fetchmany(batch_size)
            if not rows:  # Stop when there are no more rows
                break
            yield rows
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Processes each batch of users to filter users over the age of 25.

    :param batch_size: Number of rows in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        # Filter users over the age of 25
        filtered_users = [user for user in batch if user['age'] > 25]
        yield filtered_users

# Example usage
if __name__ == "__main__":
    batch_size = 2  # Define the batch size
    for processed_batch in batch_processing(batch_size):
        print("Filtered Batch:")
        for user in processed_batch:
            print(user)  # Display filtered users
