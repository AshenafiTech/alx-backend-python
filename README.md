# ALX Backend Python Projects

This repository contains a collection of backend Python projects and exercises, including Django web applications, testing utilities, decorators, and generator-based data processing scripts. Each subproject demonstrates key backend engineering concepts and best practices.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Subprojects Overview](#subprojects-overview)
  - [0x03-Unittests_and_integration_tests](#0x03-unittests_and_integration_tests)
  - [Django-Middleware-0x03](#django-middleware-0x03)
  - [Django-signals_orm-0x04](#django-signals_orm-0x04)
  - [messaging_app](#messaging_app)
  - [python-decorators-0x01](#python-decorators-0x01)
  - [python-generators-0x00](#python-generators-0x00)
- [General Setup](#general-setup)
- [License](#license)

---

## Project Structure

```
.
├── 0x03-Unittests_and_integration_tests/
├── Django-Middleware-0x03/
├── Django-signals_orm-0x04/
├── messaging_app/
├── python-decorators-0x01/
├── python-generators-0x00/
```

---

## Subprojects Overview

### 0x03-Unittests_and_integration_tests

- **Purpose:** Practice writing unit and integration tests in Python using `unittest`, `parameterized`, and `unittest.mock`.
- **Features:**
  - Unit vs. integration testing
  - Mocking readonly properties and API calls
  - Parameterized tests
  - Fixtures for structured test data
  - Memoization and cache-aware testing
- **How to Run:**
  ```sh
  python3 -m unittest test_utils.py
  python3 -m unittest test_client.py
  ```

---

### Django-Middleware-0x03

- **Purpose:** Django project focused on custom middleware, authentication, and REST API best practices.
- **Features:**
  - Custom middleware for role-based permissions
  - JWT authentication with `rest_framework_simplejwt`
  - Pagination, filtering, and search in APIs
- **How to Run:**
  ```sh
  cd Django-Middleware-0x03
  pip install -r requirements.txt
  python3 manage.py migrate
  python3 manage.py runserver
  ```

---

### Django-signals_orm-0x04

- **Purpose:** Demonstrates Django ORM usage and custom signals for event-driven logic.
- **Features:**
  - Custom model managers
  - Signal handling for model events
  - Example test cases for signals and models
- **How to Run:**
  ```sh
  cd Django-signals_orm-0x04
  python3 manage.py migrate
  python3 manage.py runserver
  ```

---

### messaging_app

- **Purpose:** Full-featured Django REST API for messaging, with CI/CD, Docker, and Kubernetes deployment scripts.
- **Features:**
  - JWT authentication, custom user model, and chat/message models
  - REST API endpoints for chats, messages, and user management
  - Pagination, filtering, and permissions
  - Docker and Kubernetes deployment files
  - Jenkins pipeline for CI/CD
- **How to Run Locally:**
  ```sh
  cd messaging_app
  pip install -r requirements.txt
  python3 manage.py migrate
  python3 manage.py runserver
  ```
- **Run with Docker:**
  ```sh
  docker-compose up --build
  ```
- **Run Tests:**
  ```sh
  pytest chats/tests.py
  ```

---

### python-decorators-0x01

- **Purpose:** Practice and demonstrate Python decorators for logging, database connections, transactions, retries, and caching.
- **Features:**
  - Logging query execution
  - Automatic DB connection management
  - Transactional operations
  - Retry on failure
  - Query result caching

---

### python-generators-0x00

- **Purpose:** Demonstrates Python generators for efficient data processing and MySQL database seeding.
- **Features:**
  - Stream users from a CSV file to a MySQL database
  - Batch processing and lazy pagination
  - Generator-based data streaming
- **How to Run:**
  1. Place a `user_data.csv` file in the directory with columns: `name,email,age`
  2. Install dependencies:
     ```sh
     pip install mysql-connector-python
     ```
  3. Run the main script:
     ```sh
     python3 0-main.py
     ```

---

## General Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/O-G-W-A-L/alx-backend-python.git
   cd alx-backend-python
   ```
2. **(Optional) Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies for each subproject as needed.**

---

## License

This repository is for educational purposes as part of the ALX Backend Python curriculum.

---
