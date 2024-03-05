# Python Course

- [ ] : Create a real life exemple of cache system with a weather API. Implement a caching system that stores weather data for different cities. When a user requests the weather for a city, the application should check the cache first. If the data is in the cache, return it immediately. If not, fetch it from the weather API, store it in the cache, and then return it.

The cache is not working. Try to find why and fix it. ()

## Class 2 - Dictionaries & Hash Tables

### Lesson Overview
- Understanding Dictionaries in Python
- Introduction to Hash Tables
- Implementing a Simple Caching System

#### 1. Introduction to Dictionaries in Python

In Python, a dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are very fast for looking up data because of how they're implemented under the hood (using hash tables).If you try to add a key that already exists, its value will be updated.

__Creating a Dictionary__

```python
# Creating a dictionary with some key-value pairs
user_ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

# Accessing a value using its key
print(user_ages["Alice"]) # Output: 25

# Adding a new key-value pair
user_ages["David"] = 40

# Updating an existing key's value
user_ages["Alice"] = 26

# Removing a key-value pair
del user_ages["Bob"]

# Printing the updated dictionary
print(user_ages) # Output: {'Alice': 26, 'Charlie': 35, 'David': 40}
```

__Iterating Through a Dictionary__

You can iterate through a dictionary using a for loop, which allows you to access keys, values, or both.

```python
# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

__Dictionary Comprehension__

You can also create dictionaries using dictionary comprehensions, which are similar to list comprehensions.

```python
# Creating a dictionary using dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### 2. Introduction to Hash Tables

A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of slots, from which the desired value can be found. This makes data retrieval extremely efficient, ideally approaching O(1) time complexity.

> [SIMPLE] Imagine you have a giant library with lots of books, but it doesn't have any system to find books quickly. If you want a specific book, you might have to look through every single book, which could take forever! A hash table is like a magical library system that helps you find your books super fast.

>Let's say every book has a unique name. The hash table uses a special magic spell (called a "hash function") on the name of the book you're looking for. This spell doesn't turn the book into a frog or anything like that; instead, it turns the name into a special number. This number is very special because it tells you exactly where the book is on the shelf.

>Here's how it works:

>Magic Spell (Hash Function): You tell the hash table the name of the book you want. The hash table uses its magic spell on the name and gets a special number. Let's say you're looking for "Harry Potter", and the spell turns "Harry Potter" into the number 42.

>Finding the Book: The hash table knows that every number matches a specific spot on the shelf. So, when it gets the number 42 from the spell, it goes straight to spot number 42 on the shelf. And guess what? "Harry Potter" is right there!

>Super Fast: Because of this system, finding a book doesn't require looking at every book in the library. You just use the spell, get the number, and go straight to your book. It's like magic!

>But, there's a little catch. Sometimes, two different book names might get turned into the same number by the spell. This is called a "collision". It's like two books trying to fit into the same spot on the shelf. The hash table has a smart way to handle this, like adding a little extension to the shelf so both books can fit.

>So, a hash table is a magical system in a computer that helps it find and store information super quickly, using a special spell to turn information (like book names) into special numbers that tell the computer exactly where that information is kept. It's like having a magic wand for finding and organizing things instantly!

#### 3. Implementing a Simple Caching System

In web applications, caching is the process of storing data in a temporary storage area so that future requests for that data can be served faster. It's reducing the load on the server and improving the user experience. A cache is like a short-term memory for your data.
Using a dictionary as a cache is a simple and effective way to store data that's frequently accessed. The key-value pairs in the dictionary represent the data and its corresponding results, and the dictionary itself acts as the cache.

#### 4. Real-World Application: User Profile Cache

Imagine you're building a web service where user profiles are frequently accessed but rarely updated. To optimize performance, you decide to cache user profiles in memory.

1. Task Description

- Implement a cache using a Python dictionary to store user profiles accessed from a database.
- When a user profile is requested, the application should check the cache first.
- If the profile is in the cache, return it immediately.
- If not, fetch it from the database, store it in the cache, and then return it.

```python
# Sample code for implementing a user profile cache
class UserProfileCache:
    def __init__(self):
        self.cache = {}

    def get_user_profile(self, user_id):
        # Check if the user's profile is in the cache 
        if user_id in self.cache:
            print("Returning cached profile for user:" user_id)
            return self.cache[user_id]

        # If not, fetch the profile from the database
        print("Fetching profile from the database for user:" user_id)
        user_profile = f"Profile data for user {user_id}" # Simulated database fetch, for real case use, remove the f-string and replace with actual database fetch
        self.cache[user_id] = user_profile # Store the profile in the cache

        return user_profile

# Testing the cache
cache = UserProfileCache()
print(cache.get_user_profile("Alice")) # Fetches from the database
print(cache.get_user_profile("Alice")) # Returns from the cache

```

### 5. Exercise comprehension [basic_operations.py](https://github.com/IMPWNG/Python_Algo_Data_Class/blob/main/Class2_Dictionaries%20_HashTables/basic_operations.py)


> [SIMPLE] Imagine our book database is like a big treasure chest full of different magical books. Each book has a special number, called an "ID," that is unique just like a magic spell. We keep all these books in our treasure chest so we can find and read them whenever we want.


>1. The New Magical Chest: BookDatabase

>In this new version of our treasure chest, called BookDatabase, we made some cool improvements to make finding and organizing our magical books even easier and faster!

>2. Loading the Treasure Chest

>When we first open our treasure chest (__init__), we use a special spell (load_database) to see all the books inside it. We put all these books into our magic bag (self.books) so we can carry them around easily and don't have to open the chest every time we want a book. This is much faster because opening and closing the chest a lot can be really slow!

>3. Adding New Magical Books

>When we want to add a new book (add_book), we first check to make sure we don't already have a book with the same magic spell (ID). If we don't, we put the new book in our magic bag. This way, we keep all our books unique and don't mix up their spells.

>4. Finding a Magical Book

>If we want to find a specific book (find_book_by_id), we just look at the spell (ID) on the book and instantly find it in our magic bag. It's like having a magic map that shows us exactly where the book is, without having to dig through the whole chest!

>5. Removing a Magical Book

>Sometimes we might need to take a book out of our treasure chest (delete_book). We use the book's special spell (ID) to find it quickly in our magic bag and then take it out. If we can't find the book we're looking for, we know it's not there, and we don't have to worry about it.

>6. Showing All Our Magical Books

>We can also spread out all our books on the floor to see them all at once (list_books). This way, we can admire our collection and easily see all the magical spells (IDs) and stories (titles and authors) we have.

>7. Saving Our Magical Books

>After we're done playing with our books, we put them all back in the treasure chest and lock it up (save_database). This way, they're safe and sound until we want to play again. We only do this once, even if we played with a lot of books, so it doesn't take too much time.

>- Why Is This Treasure Chest Better?

>Our new treasure chest is better because:

>- It's Faster: We don't have to open and close it every time we want a book. We just take all the books out once, play with them, and put them back when we're done.

>- No More Waiting: Finding and removing books is like magic now because we don't have to search through the whole chest. We just use the magic spells (IDs) to instantly find what we want.

>- Keeping It Tidy: We make sure every book has its own unique spell, so there are no mix-ups, and our treasure chest stays nice and organized.