import sqlite3

class BookManagement:
    def __init__(self):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS books
                            (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            year INTEGER NOT NULL,
                            price REAL NOT NULL,
                            stock INTEGER NOT NULL)"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS customers
                            (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL)"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS orders
                            (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer_id INTEGER NOT NULL,
                            book_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                            FOREIGN KEY (book_id) REFERENCES books(book_id))"""
        )
        self.conn.commit()
        if self.cursor.rowcount == -1:
            print("Database already exists")
        self.conn.close()

    # Method definitions should be outside of the __init__ method

    def insert_book(self, title, author, year, price, stock):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """INSERT INTO books (title, author, year, price, stock)
                            VALUES (?, ?, ?, ?, ?)""",
            (title, author, year, price, stock),
        )
        self.conn.commit()
        self.conn.close()
        print("Book added successfully")

    def update_stock(self, book_id, stock):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """UPDATE books SET stock = ? WHERE book_id = ?""", (stock, book_id)
        )
        self.conn.commit()
        self.conn.close()
        print(f"Stock level updated successfully")

    def delete_book(self, book_id):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""DELETE FROM books WHERE book_id = ?""", (book_id,))
        self.conn.commit()
        self.conn.close()
        print(f"Book deleted successfully")

    def get_books(self):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""SELECT * FROM books""")
        books = self.cursor.fetchall()
        self.conn.close()
        return books

    def new_order(self, customer_id, book_id, quantity):
        if self.check_stock(book_id, quantity):
            self.conn = sqlite3.connect("bookManagement.sqlite")
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                """INSERT INTO orders (customer_id, book_id, quantity)
                                VALUES (?, ?, ?)""",
                (customer_id, book_id, quantity),
            )
            self.conn.commit()
            self.cursor.execute(
                """UPDATE books SET stock = stock - ? WHERE book_id = ?""",
                (quantity, book_id),
            )
            self.conn.commit()
            self.conn.close()
            print("Order placed successfully")
        else:
            print("Not enough stock for this order.")

    def check_orders(self):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        self.conn.close()
        return orders

    def sales_report(self):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """SELECT books.title, SUM(orders.quantity) AS total_sales
           FROM orders
           JOIN books ON orders.book_id = books.book_id
           GROUP BY books.book_id, books.title
           ORDER BY total_sales DESC"""
        )
        sales = self.cursor.fetchall()
        self.conn.close()
        print("Sales report generated successfully")
        for sale in sales:
            print(f"Title: {sale[0]}, Total Sales: {sale[1]}")
        return sales

    def check_stock(self, book_id, quantity):
        self.conn = sqlite3.connect("bookManagement.sqlite")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""SELECT stock FROM books WHERE book_id = ?""", (book_id,))
        result = self.cursor.fetchone()
        self.conn.close()

        if result is None:
            print(f"Book with ID {book_id} not found")
            return False

        stock = result[0]
        return stock >= quantity


# Create an instance of the BookManagement class
bookManagement = BookManagement()

# Add a new book to the database
bookManagement.insert_book('The Alchemist', 'Paulo Coelho', 1988, 10.99, 100)
bookManagement.insert_book('The Catcher in the Rye', 'J.D. Salinger', 1951, 9.99, 50)
bookManagement.insert_book('To Kill a Mockingbird', 'Harper Lee', 1960, 12.99, 75)

# Update the stock level of a book
bookManagement.update_stock(1, 50)

# Delete a book from the database
bookManagement.delete_book(10)

# Retrieve all books from the database
print(f"Books in the database: {bookManagement.get_books()}")

# Place a new order
bookManagement.new_order(1, 9, 10)

# Generate a sales report
print(bookManagement.sales_report())

# Check stock levels
print(bookManagement.check_stock(6, 100))

# Check orders
print(bookManagement.check_orders())
