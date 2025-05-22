import csv
import uuid
import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    'user': 'root',
    'password': 'dohardthings',
    'host': 'localhost'
}

DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'

# connect to the mysql database server
def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
# create the database ALX_prodev if it does not exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database {DB_NAME} created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

#  connect the the ALX_prodev database in MYSQL
def connect_to_prodev():
    try:
        conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to {DB_NAME}: {err}")
        return None
    
# create a table user_data if it does not exists with the required fields
def create_table(connection):
    cursor = connection.cursor()
    try:
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX(user_id)
        );
        """
        cursor.execute(create_table_query)
        print(f"Table {TABLE_NAME} created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    finally:
        cursor.close()

# insert data into the database if it does not exist
def insert_data(connection, csv_file):
    cursor = connection.cursor()

    try: 
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Check if record already exists
                cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE email = %s", (row['email'],))
                if cursor.fetchone()[0] == 0:
                    uid = str(uuid.uuid4())
                    cursor.execute(
                        f"INSERT INTO {TABLE_NAME} (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (uid, row['name'], row['email'], row['age'])
                    )
            connection.commit()
            print("Data inserted successfully.")
    except FileNotFoundError:
        print(f"{csv_file} not found.")
    except mysql.connector.Error as err:
        print("Erro inserting data: {err}")
    finally:
        cursor.close()