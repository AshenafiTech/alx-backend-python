import mysql.connector
from seed import DB_CONFIG, DB_NAME, TABLE_NAME

def stream_users_in_batches(batch_size):
    """Yields batches of users from the user_data table."""
    conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
    cursor.close()
    conn.close()
    return None

def batch_processing(batch_size):
    """Processes each batch and prints users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if float(user['age']) > 25]
        for user in filtered:
            print(user)