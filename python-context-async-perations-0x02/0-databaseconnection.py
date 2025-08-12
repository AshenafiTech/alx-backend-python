import sqlite3

class DatabaseConnection:
	def __init__(self, db_path):
		self.db_path = db_path
		self.conn = None

	def __enter__(self):
		self.conn = sqlite3.connect(self.db_path)
		return self.conn

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.conn:
			self.conn.close()

# Usage example
if __name__ == "__main__":
	db_path = "my_database.db"  # Change this to your actual database file
	with DatabaseConnection(db_path) as conn:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users")
		results = cursor.fetchall()
		for row in results:
			print(row)
