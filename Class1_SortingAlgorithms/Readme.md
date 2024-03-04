# Python Course

## Class 1 - Sorting Algorithms

### Lesson Overview
- Introduction to Sorting Algorithms
- Understanding Lists in Python
- Implementing the Bubble Sort Algorithm
- Real-World Application: Sorting User Data for an API Endpoint

#### 1 - Introduction to Sorting Algorithms

Sorting algorithms are methods for reordering elements in a list or array according to a specific relationship among the elements (e.g., ascending or descending for numerical values, alphabetical order for strings). Common sorting algorithms include Bubble Sort, Merge Sort, Quick Sort, and Insertion Sort. Each has its own set of advantages and use cases depending on the size and nature of the data set.

#### 2 - Understanding Lists in Python

In Python, a list is a mutable, ordered sequence of elements. Lists are versatile and can hold a mixture of data types, including integers, strings, and even other lists. They are fundamental in data structure manipulation and a key component in algorithm implementation.

#### 3 - Implementing the Bubble Sort Algorithm

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.


Write a Python function to sort a list of integers using the Bubble Sort algorithm.
    
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

Imagine you have a line of toy blocks, each with a number on it. We want to arrange these blocks so that their numbers go from smallest to biggest, from left to right.

```python 
def bubble_sort(arr)
```
This is like saying, "We have a game called 'bubble sort,' and we need our line of blocks (which we're calling arr) to play this game."

```python 
n = len(arr)
```
Here, we're counting how many blocks we have in our line. If we have 10 blocks, n becomes 10. It's like saying, "I have 10 blocks to organize."

```python 
for i in range(n):
```
This is like saying, "I'm going to walk down my line of blocks n times (so, if we have 10 blocks, I'll walk down the line 10 times). Each walk down the line, I'll call a 'round,' and each round, I'm going to try and make sure at least one block gets to where it's supposed to be."

```python 
for j in range(0, n-i-1):
```
Now, this might sound a bit tricky, but think of it like this: Each time you complete a round (walking down the line), the last block in the line is definitely in the right spot, so we don't need to check it again. So, in the next round, we check one less block. This line is just our way of saying, "Let's not go all the way to the end since the last few blocks are already sorted. Let's stop a bit earlier each time."

```python 
if arr[j] > arr[j+1]:
```
Here, we're looking at two blocks at a time, the one we're currently at (let's call it Block A) and the next one (Block B). We're checking if Block A's number is bigger than Block B's number. If it is, it means they're in the wrong order because the bigger number should be on the right.

```python 
arr[j], arr[j+1] = arr[j+1], arr[j]
```
When we find that Block A and Block B are in the wrong order, we switch their places. It's like saying, "Oops, you two need to swap spots so that the smaller number is on the left."

```python 
return arr
```
After we've walked down the line enough times and made all the necessary swaps, our line of blocks is now organized from the smallest number to the biggest. We're done! This line is like saying, "Look, all the blocks are in order now!"

So, inside our big walk down the line (the first loop), we have a smaller walk (the second loop) where we're checking each pair of blocks and making sure they're in the right order by swapping them if needed. And with each big walk, we have to check fewer and fewer blocks because the biggest numbers are finding their way to the end of the line, just like bubbles floating up to the surface of the water. That's why it's called "Bubble Sort"!

#### 4 - Real-World Application: Sorting User Data for an API Endpoint -> Check the file [sorting_user_data.py](https://github.com/IMPWNG/Python_Algo_Data_Class/blob/main/Class1_SortingAlgorithms/user_sorting.py)

Imagine you're developing a backend for a user management system, and you need to create an API endpoint that returns a list of users sorted by their registration date.

Task Description
You have a list of user dictionaries, each containing username and registration_date.
Implement a sorting function to organize this list by registration_date.
Prepare a mock API endpoint function that uses this sorting function to return sorted user data.