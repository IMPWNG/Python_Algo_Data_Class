# Python Course

## Class 6 - Linked Lists

### Lesson Overview
- Introduction to Linked Lists
- Components of a Linked List
- Types of Linked Lists
- Advantages and Disadvantages of Linked Lists
- Real-World Application: Music Player
- Exerice: Implementing a Singly Linked List


#### 1 - Introduction to Linked Lists

A linked list is a linear data structure where elements are stored in nodes. Each node contains a data element and a reference (or link) to the next node in the sequence. Linked lists are a fundamental data structure in computer science and are used to implement other data structures such as stacks, queues, and graphs. This structure allows for efficient insertion and removal of elements from any position in the sequence.

#### 2 - Components of a Linked List

- **Node**: The basic building block of a linked list. Each node contains a data element and a reference (or link) to the next node in the sequence.
- **Head**: The first node in the linked list.
- **Tail**: The last node in the linked list.
- **Pointer**: A reference to another node.

#### 3 - Types of Linked Lists

- **Singly Linked List**: Each node contains a data element and a reference to the next node in the sequence.
- **Doubly Linked List**: Each node contains a data element, a reference to the next node, and a reference to the previous node in the sequence.
- **Circular Linked List**: The last node points back to the first node, creating a circular structure, instead of ending with a null reference.

#### 4 - Advantages and Disadvantages of Linked Lists

- **Advantages**:
  - Dynamic size: Linked lists can grow or shrink in size during program execution.
  - Efficient insertion and deletion: Adding or removing elements from a linked list is more efficient than arrays or other data structures, because it does not require shifting elements to accommodate new or removed elements.
  - No wasted memory: Linked lists can use memory more efficiently than arrays, as they only allocate memory when new elements are added.

- **Disadvantages**:
    - Sequential access: Unlike arrays, linked lists do not provide constant-time access to individual elements. To access an element, you must traverse the entire list from the beginning.
    - Extra memory: Each element in a linked list requires extra memory to store the reference to the next node, which can add up for large lists.

#### 5 - Real-World Application: Music Player

Consider a music playlist as a real-world analogy for a linked list. Each song in the playlist can be thought of as a node, with details about the song (like its title and artist) as the node's data. The "next" pointer in each song/node points to the next song in the playlist. Adding a new song to the playlist is akin to inserting a new node in the linked list, and skipping a song is like moving to the next node.

#### 6 - Exercise: Implementing a Singly Linked List

Write a Python class to implement a singly linked list. The class should support the following operations:

```python
append(data) # Add a new node to the end of the list
display() # Print the elements of the list
```

```python
class Node:
    def__init__(self, data= None):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

        def display(self):
            current_node = self.head
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")

# Example usage
11 = LinkedList()
11.append('A')
11.append('B')
11.append('C')
11.display()
```



