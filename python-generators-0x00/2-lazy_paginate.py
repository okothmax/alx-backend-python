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

def paginate_users(page_size, offset):
    """
    Fetches a page of users starting at the given offset.

    :param page_size: Number of rows per page.
    :param offset: The starting point for the page.
    :return: A list of rows for the given page.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        connection.close()

def lazy_paginate(page_size):
    """
    A generator function to lazily load pages of users from the database.

    :param page_size: Number of rows per page.
    :yield: A page of rows as a list of dictionaries.
    """
    offset = 0
    while True:
        # Fetch the next page
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more rows are available
            break
        yield page
        offset += page_size

# Example usage
if __name__ == "__main__":
    page_size = 2  # Define the page size
    for page in lazy_paginate(page_size):
        print("Fetched Page:")
        for user in page:
            print(user)  # Print each user in the page
