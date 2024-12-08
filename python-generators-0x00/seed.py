import mysql.connector
import csv
import uuid

# Function to connect to the MySQL server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="orain",
            password="CasablancaHero23@",
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

# Function to create the database ALX_prodev if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

# Function to connect to the ALX_prodev database
def connect_to_prodev():
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

# Function to create the user_data table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,1) NOT NULL,
            INDEX(user_id)
        )
    """)
    connection.commit()
    cursor.close()

# Function to insert data into the database if it does not already exist
def insert_data(connection, data):
    cursor = connection.cursor()
    for row in data:
        # Check if the email already exists in the database
        cursor.execute("SELECT * FROM user_data WHERE email = %s", (row['email'],))
        if not cursor.fetchone():  # If the email does not exist
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()

# Load CSV data and insert it into the database 
def load_csv_data(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

# Main function to run the script
def main():
    # Step 1: Connect to MySQL server
    connection = connect_db()
    
    # Step 2: Create database
    create_database(connection)
    connection.close()
    
    # Step 3: Connect to ALX_prodev database
    connection = connect_to_prodev()
    
    # Step 4: Create user_data table
    create_table(connection)
    
    # Step 5: Load data from CSV and insert it into the database
    csv_file_path = "user_data.csv"
    sample_data = load_csv_data(csv_file_path)
    insert_data(connection, sample_data)
    
    print("Database seeding completed successfully.")
    connection.close()

if __name__ == "__main__":
    main()
