# Python Course

## Class 3 - Db Management

### Lesson Overview
- Introduction to Databases
- SQL Databases
- Python and Databases

#### 1. Introduction to Databases

1. Definition & Importance: A database is an organized collection of data. It's essential for storing, managing, and retrieving data in a structured way.

2. Types of Databases:
    - Relational Databases: Data is stored in tables and can be related to each other. Examples: MySQL, PostgreSQL, SQLite.
    - NoSQL Databases: Data is stored in a non-tabular format. Examples: MongoDB, Cassandra, Redis.

#### 2. SQL Databases

1. Relational Databases Concepts: In SQL databases, data is stored in tables, which relate to each other through foreing keys.

2. SQL Language: SQL (Structured Query Language) is the standard language for relational database management systems. It's used for querying and manipulating databases.

#### 3. Python and Databases

Python provides several libraries to interac with SQL Databases, such as:
- sqlite3: A built-in library for SQLite databases.
- MySQL Connector: A library for MySQL databases.
- Psycopg2: A library for PostgreSQL databases.


#### 4. Exercise: Create a Database

The goal of this exercise is to create a SQLite database to manage a library's books, authors, and dates of publication.

1. Create a new SQLite database file.

```python
import sqlite3

# Create a new SQLite database file
conn = sqlite3.connect("library.db")

#Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a new table
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                (id INTEGER PRIMARY KEY, title TEXT, author TEXT, published_date TEXT)''')

# Commit the changes and close the connection
conn.commit()
conn.close()
```

2. Insert data into the database.

```python
def add_book(title, author, published_date):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSTER INTO books (title, author, published_date) VALUES (?, ?, ?)",
                    (title, author, published_date))
    conn.commit()
    conn.close()

# Example : Inserting a new book
add_book('Python Programming', 'John Doe', '2020-01-01')
```

3. Query data from the database.

```python
def find_books_by_author(author):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
    books = cursor.fetchall()
    conn.close
    return books

# Example: Finding books by a specific author
print(find_books_by_author('John Doe'))
for book in books:
    print(book)
```
#### 5. Real Life Example

1. Scenario: MyBookStore - An Online Bookstore System

MyBookStore aims to provide an online platform for book lovers to browse, search, and purchase books. The system needs to manage book inventories, customer orders, and generate sales reports. As the backend developer, you'll create the database structure, insert sample data, and write Python scripts to interact with the database.

2. Requirements 

Database Setup: Design a database schema to accommodate books, customers, and orders.

Inventory Management: Implement functionality to add, update, and remove books from the inventory.

Order Processing: Develop a system for customers to place orders.

Sales Reporting: Generate reports for monthly sales and most popular books.

- Step 1: Database Schema Design
First, we need to design our database schema. Our schema will include three main tables:

Books: To store information about the books.
Customers: To keep track of customer information.
Orders: To record each book purchase.

- Step 2: Inventory Management
Implement Python functions to interact with the books table. You'll need functions to add new books, update stock levels, and remove books from the inventory.

- Step 3: Order Processing
Create Python functions to handle new orders. This includes inserting a new order record and updating the stock level for the ordered book(s).

- Step 4: Sales Reporting
Write queries and Python functions to generate sales reports. For example, you might want to see the total sales for the past month or find the top-selling books.

2. Real-Life Problem: Implementing the Backend for MyBookStore
Your task is to implement the backend logic for MyBookStore using Python and SQLite. Follow the steps outlined above, and consider the following challenges:

- Concurrency: Handle scenarios where multiple customers attempt to purchase the last copy of a book simultaneously.
Data Validation: Ensure that all data entered into the database is valid (e.g., stock levels should not be negative, email addresses should be unique, etc.).

- User Experience: Think about the end-user experience. How would the system inform the user if a book is out of stock or if their order has been successfully processed?

3. Exercises

- Implement the Inventory Management Functions: Write Python functions to add, update, and delete books in the inventory.

- Order Processing System: Develop the system to handle customer orders, ensuring that stock levels are updated accordingly.

- Generate Sales Reports: Create functions to generate and print sales reports, including total sales and top-selling books.

This scenario will challenge you to apply the concepts learned in the Database Management & SQL with Python class to solve a complex, real-world problem. It will also require you to think critically about database design, data integrity, and user experience.



