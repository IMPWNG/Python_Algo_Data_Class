import json

# Path to your JSON file
file_path = "books_database.json"


# Function to generate a random book title and author
def generate_book_info(id):
    # For simplicity, these are basic placeholders. You could make these more complex or fetch real data.
    title = f"Random Book Title {id}"
    author = f"Random Author {id}"
    return {"id": id, "title": title, "author": author}


# Read the existing JSON data
with open(file_path, "r") as file:
    data = json.load(file)

# Get the starting ID for new books based on the last ID in the current data
start_id = data["books"][-1]["id"] + 1

# Append 50 new books
for i in range(start_id, start_id + 50):
    new_book = generate_book_info(i)
    data["books"].append(new_book)

# Write the updated data back to the JSON file
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

print("50 new entries added.")
