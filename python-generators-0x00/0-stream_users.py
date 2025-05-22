import mysql.connector
from seed import DB_CONFIG, DB_NAME, TABLE_NAME

def stream_users():
    conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for row in cursor:
        yield row
    cursor.close()
    conn.close()