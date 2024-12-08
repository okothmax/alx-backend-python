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

def stream_user_ages():
    """
    A generator function that fetches user ages from the user_data table one by one.

    :yield: Age of a user as a float.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    try:
        # Query to select all user ages
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield float(row[0])  # Yield each age
    finally:
        cursor.close()
        connection.close()

def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.

    :return: Average age as a float.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count == 0:  # Avoid division by zero
        return 0
    return total_age / count

# Example usage
if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
