Database Seeder for ALX_prodev
This script (seed.py) sets up a MySQL database (ALX_prodev), creates a table (user_data), and populates it with data from a CSV file. It is designed for ease of use and ensures that the database is properly configured before inserting data.

Features
Connects to a MySQL server.
Creates the ALX_prodev database if it doesn't exist.
Creates a user_data table with the following fields:
user_id (Primary Key, UUID, Indexed)
name (VARCHAR, NOT NULL)
email (VARCHAR, NOT NULL)
age (DECIMAL, NOT NULL)
Reads and inserts data from a user_data.csv file into the table, avoiding duplicates.
Ensures efficient database setup and data seeding.
Prerequisites
MySQL Server installed and running.
Python 3.x installed.
Required Python libraries:
mysql-connector-python
uuid
A user_data.csv file in the same directory as the script.
Installation
Clone the repository or download the seed.py script.
Install the required Python libraries:
bash
Copy code
pip install mysql-connector-python
Ensure your MySQL server credentials are configured in the script.
Usage
Prepare the CSV File: Ensure the file user_data.csv exists in the same directory as the script and follows this format:

csv
Copy code
name,email,age
John Doe,johndoe@example.com,29
Jane Smith,janesmith@example.com,34
Alice Johnson,alicej@example.com,42
Run the Script: Execute the script with Python:

bash
Copy code
python seed.py
Expected Output:

Creates the ALX_prodev database.
Creates the user_data table.
Inserts rows from the CSV file into the database.
Displays a success message:
Copy code
Database seeding completed successfully.
File Structure
bash
Copy code
.
├── seed.py            # Python script for setting up and seeding the database
├── user_data.csv      # Sample data file to populate the database
Functions Overview
connect_db(): Connects to the MySQL server.

create_database(connection): Creates the ALX_prodev database if it does not exist.

connect_to_prodev(): Connects to the ALX_prodev database.

create_table(connection): Creates the user_data table with the specified schema.

insert_data(connection, data): Inserts data into the table, avoiding duplicates.

load_csv_data(file_path): Reads data from a CSV file and formats it for insertion.

Troubleshooting
MySQL Connection Issues:

Ensure the MySQL server is running.
Verify the user and password values in the script.
CSV File Errors:

Confirm the file user_data.csv exists in the same directory as the script.
Ensure the CSV format matches the expected structure (name,email,age).
Library Missing:

Install required libraries using pip:
bash
pip install mysql-connector-python