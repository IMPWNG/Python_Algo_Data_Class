# This is a simple Python program that sorts a list of users by their registration date. 
# The list of users is a list of dictionaries, where each dictionary contains the username and the registration date of a user. 
# The program defines a function called sort_users_by_registration_date that takes a list of users as input and returns the list of users sorted by their registration date. 
# The program also defines a function called get_sorted_users_api that calls the sort_users_by_registration_date function and prints the sorted list of users. 
# The program uses the bubble sort algorithm to sort the list of users by their registration date.

users = [
    {"username": "alice", "registration_date": "2022-01-15"},
    {"username": "bob", "registration_date": "2022-03-22"},
    {"username": "charlie", "registration_date": "2021-12-10"},
    {"username": "david", "registration_date": "2022-02-05"},
    {"username": "eve", "registration_date": "2022-01-01"},
    {"username": "frank", "registration_date": "2022-01-01"},
    {"username": "grace", "registration_date": "2022-24-21"},
    {"username": "harry", "registration_date": "2022-04-22"},
    {"username": "ian", "registration_date": "2022-23-09"},
    {"username": "jane", "registration_date": "2024-02-01"},
]


def sort_users_by_registration_date(users):
    # Get the length of the list
    n = len(users)
    # Traverse through all elements in the list
    for i in range(n):
        # Here we start from the first element and traverse the list from the beginning to the end. 
        # We compare the current element with the next element. 
        # If the current element is greater than the next element, we swap them. 
        for j in range(0, n-i-1):
            # As Python doesn't know how to compare dictionaries by default, especially when it doesn't know which key-value pairs should be used for the comparison. 
            # We need to specify the key to be used for the comparison. ["registration_date"] is used to specify the key to be used for the comparison.
            if users[j]["registration_date"] > users[j + 1]["registration_date"]:
                # Swap the elements
                users[j], users[j+1] = users[j+1], users[j]
    # As the list is already sorted, just return it
    return users


def get_sorted_users_api():
    sorted_users = sort_users_by_registration_date(users)
    # This would actually involve more steps in a real API, like serialization
    for user in sorted_users:
        print(
            f"Username: {user['username']}, Registration Date: {user['registration_date']}"
        )
# Test the function
get_sorted_users_api()
