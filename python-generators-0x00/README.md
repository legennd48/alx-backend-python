# Advanced Python Generators & Database Integration

## About the Project

This project explores advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations. The tasks focus on leveraging Python’s `yield` keyword to implement generators that provide iterative access to data, promoting optimal resource utilization and improving performance in data-driven applications.

## Learning Objectives

By completing this project, you will:

- **Master Python Generators:** Learn to create and utilize generators for iterative data processing, enabling memory-efficient operations.
- **Handle Large Datasets:** Implement batch processing and lazy loading to work with extensive datasets without overloading memory.
- **Simulate Real-world Scenarios:** Develop solutions to simulate live data updates and apply them to streaming contexts.
- **Optimize Performance:** Use generators to calculate aggregate functions like averages on large datasets, minimizing memory consumption.
- **Apply SQL Knowledge:** Use SQL queries to fetch data dynamically, integrating Python with databases for robust data management.

---

## Project Structure

- `seed.py` — Utilities for connecting to the database, creating tables, and seeding data from CSV.
- `0-stream_users.py` — Generator that streams user rows one by one from the database.
- `1-batch_processing.py` — Batch generator and processor for filtering users by age.
- `2-lazy_paginate.py` — Lazy pagination generator for fetching pages of users on demand.
- `4-stream_ages.py` — Generator and function for memory-efficient average age calculation.
- `user_data.csv` — Sample user data for seeding the database.
- `*_main.py` — Example/test scripts for each task.

---

## How to Run the Project

To run `0-main.py`, you must provide your MySQL connection details as environment variables.  
Use the following command, replacing the placeholders with your actual values:

```sh
DB_HOST=<your_host> DB_USER=<your_username> DB_PASSWORD=<your_password> DB_NAME=<your_database> python 0-main.py
```
- Make sure you have installed all dependencies and your MySQL server is running.
- If you are using a virtual environment, activate it before running the command.

---

## Script Descriptions

### 0. Stream Users (`0-stream_users.py`)
- **Function:** `stream_users()`
- **Description:** Generator that yields each user row as a dictionary from the `user_data` table.
- **Usage:** Used in `1-main.py` to print the first N users.

### 1. Batch Processing (`1-batch_processing.py`)
- **Functions:**  
  - `stream_users_in_batches(batch_size)` — Yields batches (lists) of user dictionaries.
  - `batch_processing(batch_size)` — Processes each batch, filtering users over age 25.
- **Usage:** Used in `2-main.py` to print filtered users in batches.

### 2. Lazy Pagination (`2-lazy_paginate.py`)
- **Functions:**  
  - `paginate_users(page_size, offset)` — Fetches a single page of users.
  - `lazy_pagination(page_size)` — Generator that yields each page of users, fetching only as needed.
- **Usage:** Used in `3-main.py` for paginated output.

### 4. Stream Ages and Compute Average (`4-stream_ages.py`)
- **Functions:**  
  - `stream_user_ages()` — Generator yielding user ages one by one.
  - `calculate_average_age()` — Computes and prints the average age using the generator.
- **Usage:** Run directly or import to print the average age of users.

---

## Notes

- All database credentials must be provided via environment variables.
- The project is designed for efficiency and scalability with large datasets.
- No SQL aggregate functions (like `AVG`) are used for average calculations; all aggregation is done in Python using generators.

---


