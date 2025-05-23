import mysql.connector
from seed import DB_CONFIG, DB_NAME

def paginate_users(page_size, offset):
    """Fetch a single page of users starting from the given offset."""
    conn = mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def lazy_paginate(page_size):
    """Generator that yields pages of users, loading each page only when needed."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size