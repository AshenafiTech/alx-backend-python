# ALX Backend Python: MySQL Database Seeding with Generators

This project demonstrates how to set up a MySQL database, create a table, and populate it with data from a CSV file using Python. It also includes a generator to stream rows from the database one by one.

## Features

- Connects to a MySQL server
- Creates a database (`ALX_prodev`) and a table (`user_data`) if they do not exist
- Populates the table from a CSV file (`user_data.csv`)
- Skips duplicate entries based on email
- Example code to fetch and display rows from the table

## Table Schema

- `user_id` (Primary Key, UUID, Indexed)
- `name` (VARCHAR, NOT NULL)
- `email` (VARCHAR, NOT NULL)
- `age` (DECIMAL, NOT NULL)

## Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` package

Install dependencies:
```sh
pip install mysql-connector-python
```

## Usage

1. **Prepare your CSV file**  
   Place a `user_data.csv` file in the project directory with columns:  
   ```
   name,email,age
   ```

2. **Run the main script**  
   Activate your virtual environment if you have one, then run:
   ```sh
   python3 0-main.py
   ```
   or, if you have made the script executable and are using the correct shebang:
   ```sh
   ./0-main.py
   ```

3. **What happens:**  
   - The script connects to MySQL, creates the database and table if needed, and inserts data from the CSV.
   - It prints confirmation messages and displays the first 5 rows from the `user_data` table.

## Project Structure

```
.
├── 0-main.py         # Main script to run the setup and seeding
├── seed.py           # Contains all database and CSV logic
├── user_data.csv     # Your data source (not included here)
```

## Notes

- Make sure your MySQL server is running and credentials in `seed.py` are correct.
- The script uses UUIDs for `user_id` and skips inserting rows with duplicate emails.

## License

This project is for educational purposes.