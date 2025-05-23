import mysql.connector
from seed import DB_CONFIG, DB_NAME

def stream_user_ages():
    """Generator that yields user ages one by one from the user_data table."""
    conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield float(age)
    cursor.close()
    conn.close()

def compute_average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    average = total / count if count else 0
    print(f"Average age of users: {average}")

if __name__ == "__main__":
    compute_average_age()