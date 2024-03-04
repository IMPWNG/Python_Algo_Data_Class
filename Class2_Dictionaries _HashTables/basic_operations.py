# TASK

# Add a New Book: Create a function to add a new book entry to the database books_database.json.
# Find a Book by ID: Create a function that retrieves a book's details by its id.
# Delete a Book: Create a function that removes a book from the database by its id.
# List All Books: Create a function that prints out all the books in the database.

import json 

class BooksDatabase:
    def __init__(self):
        self.database = self.load_database()
        self.books = self.database.get("books", [])

    def load_database(self):
        try:
            with open("books_database.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_database(self):
        with open("books_database.json", "w") as file:
            json.dump({"books": self.books}, file, indent=4)

    def add_book(self, id, title, author):
        # Check if the book already exists
        if any(book["id"] == id for book in self.books):
            print(f"Book with ID {id} already exists")
        else:
            self.books.append({"id": id, "title": title, "author": author})
        print(f"Book with ID {id} added")

    def find_books_by_id(self, id):
        for book in self.books:
            if book["id"] == id:
                return book
        return f"Book with ID {id} not found."

    def delete_book(self, id):
        for i, book in enumerate(self.books):
            if book['id'] == id:
                del self.books[i]
                print(f"Book with ID {id} has been deleted.")
                return
        print(f"Book with ID {id} not found.")

    def list_books(self):
        if not self.books:
            print("No books in the database.")
        for book in self.books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")


# Exemple usage

db = BooksDatabase()
db.add_book(1, "Jean", "F. Scott Fitzgerald")
db.add_book(5, "To Kill a Mockingbird", "Harper Lee")
db.list_books()
book = db.find_books_by_id(6)
print("\nFound book:", book)
db.delete_book(8)
db.list_books()
db.save_database()
