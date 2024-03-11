# Algorith & Data Structure Course

## Class 7 - Recursion & Dynamic Programming

### Lesson Overview
- Introduction to Recursion:
    - Definition and Concept
    - How Recursion Works
    - Visualization of the call stack during recursive calls
    - Simple Examples: Factorial and Fibonacci
    - In simple terms

- Recursion in Depth:
    - Writing recursive functions: Best practices and common pitfalls
    - Tail recursion and its benefits
    - Recursion vs. Iteration: When to use which
    - In simple terms

- Introduction to Dynamic Programming
    - The concept of Overlapping Subproblems
    - The concept of Optimal Substructure
    - Memoization: What it is and how it works
    - Top-Down vs. Bottom-Up Approaches

- Dynamic Programming in Practice
    - Identifying when to use dynamic programming
    - Step-by-step approach to solving problems with dynamic programming
    - Classic dynamic programming problems:
        - Rod Cutting Problem
        - Longest Common Subsequence
        - Knapsack Problem

- Combining Recursion and Dynamic Programming
    - Problems best suited for this approach
    - Efficiency considerations and examples

- Lab Session
    - Hands-on coding exercises on platforms like LeetCode, HackerRank, or CodeSignal
    - Solving problems that involve recursion and dynamic programming
    - Debugging and optimizing solutions

- Wrap-Up and Q&A
    - Recap of key concepts
    - Best practices for approaching recursive and dynamic programming problems
    - Open floor for questions and discussion on complex problems

- Exercies and Real Life Problem: 

- Recursion Exercises

Factorial Calculation: Write a recursive function to calculate the factorial of a number.
Fibonacci Series: Implement a recursive function to generate the nth Fibonacci number.
Binary Search: Implement a recursive binary search algorithm.
Directory Size: Write a recursive function that calculates the total size of files in a directory, including subdirectories.

- Dynamic Programming Exercises

Coin Change Problem: Given an unlimited supply of coins of given denominations, find the minimum number of coins required to make a specific amount of money.
Longest Increasing Subsequence: Find the length of the longest subsequence in a given array such that all elements of the subsequence are sorted in increasing order.
0-1 Knapsack Problem: Given weights and values of n items, put these items in a knapsack of a fixed capacity to get the maximum total value in the knapsack.
Real-Life Problem: Project Planning and Resource Allocation
Imagine you're managing a series of projects for a software development company. Each project has a potential profit associated with its completion and requires a certain number of developers to work on it. However, your resources are limited; you have a fixed number of developers and a time frame within which you can complete these projects.

Your Objective: Maximize the total profit while ensuring that the number of developers and the time frame constraints are not exceeded.

- Problem Breakdown:

You have N projects, each with its profit Pi and the number of developers required Di.
You have M developers available and a time frame of T months.
A project can only be started if enough developers are available, and once started, it occupies the developers for the entire duration of the project.

- Approach:

Use dynamic programming to find the optimal combination of projects that maximizes profit without exceeding the available developers and time frame.
Define the state as DP[i][j], representing the maximum profit achievable by considering the first i projects with j developers available.
The state transition would consider whether to take a project (if developers and time are sufficient) or skip it.

- Exercise:

Develop a function or program that takes the projects' details (profits, developers required, and durations) along with the total available developers and time frame as inputs and outputs the maximum profit achievable and the list of projects to undertake.

#### 1 - Introduction to Recursion

Recursion is a programming technique qhere a function calls itself directly or indirectly to solve a problem. This method is particularly useful for solving problems that can be broken down into smaller, similar problems. Recursion is widely used in computer science and is a fundamental concept in data structures and algorithms.

##### 1.1 Definition and Concept

At its core, recursion is about solving a problem by having a function call itself as a subroutine. This approach can make some problems easier to think about and can lead to elegant solutions that are both concise and readable.

##### 1.2 How Recursion Works

Recursion consists of two main components:

- **Base Case**: This is the condition under which the recursion ends. It's the simplest instance of the problem, which can be solved directly without any further recursion.
- **Recursive Step: This involves the function calling itself with a simpler or smaller version of the original problem, moving it closer to the base case.

The recursive process continues until it reaches a base case, at which point the stack of calls starts unwinding, and the function calls return their results back up the chain.

##### 1.3 Visualization of the Call Stack During Recursive Calls

When a function calls itself recursively, each call gets its own separate execution context and is placed on the call stack. The call stack is a data structure that stores information about the active subroutines of a program. With recursion, as each call waits for its recursive calls to complete, it creates a stack of calls that grows with each recursive step until the base case is reached. After hitting the base case, the stack starts to unwind as the calls complete and return their results.

##### 1.4 Simple Examples: Factorial and Fibonacci

Two classic examples of problems that can be solved using recursion are the factorial and Fibonacci sequence.

- **Factorial**: The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It's denoted by n!. The base case is 0! = 1.

```python
def factorual(n):
    # Base Case
    if n == 0:
        return 1
    # Recursive Step
    else:
        Return n * factorial(n-1)
```

- **Fibonacci Sequence**: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. That is, fib(0) = 0, fib(1) = 1, and fib(n) = fib(n-1) + fib(n-2) for n > 1.

```python
def fibonacci(n):
    # Base Case
    if n  == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Step
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

##### 1.5 In Simple Terms

- What's Recursion?

Recursion is like a loop in a cartoon where the character keeps going through the same door and ending up back where they started. In programming, it's when a function (a set of instructions) calls itself to solve a problem.

- How Does It Work?

Recursion has two main parts:

Base Case: This is like a stop sign. It tells the function when to stop calling itself. For example, if you're counting LEGO blocks and have no more blocks to count, you stop.

Recursive Step: This is when the function calls itself but with a smaller problem. Like taking one block from the big pile and then counting the rest.

- The LEGO Pile: A Visual Example:

Imagine you want to count your LEGO blocks using recursion:
First, you start with the big pile (the original problem).
You take one block and set it aside (the recursive step). Now you have a slightly smaller pile to count.
You keep doing this (taking one block from the pile and setting it aside) until there are no blocks left in the pile (the base case).
Each time you set a block aside, you know that's one block counted, and you keep a running total in your head.

- Simple Examples:

Counting LEGO Blocks (like Factorial)
If you have 5 LEGO blocks and want to count them one by one, you can think of each block as a step. You take one block and say, "This is 1." Then you take another and add it to the count, saying, "Now, I have 2," and so on until there are no blocks left.

Building a LEGO Tower (like Fibonacci)
Imagine you're building towers with your LEGO blocks. The rule is, you can only stack them in a certain way: A tower that's 1 block high is just a single block. A tower that's 2 blocks high is two single blocks stacked. But for taller towers, you can make them by putting a 1-block tower on top of a smaller tower or a 2-block tower on top of an even smaller tower.

So, if you want to build a 3-block high tower, you can do it by putting a 1-block tower on top of a 2-block tower you made before, or by stacking a 2-block tower on top of a 1-block tower.

#### 2 - Recursion in Depth

##### 2.1 Writing Recursive Functions: Best Practices and Common Pitfalls

When writing recursive functions, it's important to keep the following best practices in mind:

- Define the Base Case: Always define a clear base case to prevent infinite recursion. The base case is when the function stops calling itself.
- Profress Toward the Base Case: Each recursive call should bring you closer to the base case. This often involves reducing the size of the problem with each call.
- Keep It Simple: Recursive functions should be kept as simple as possible. Complex logic can often be refactored or handled outside the recursion.
- Test with Small Inputs: Start by testing your recursive function with small inputs where you know the expected output, ensuring it works correctly before scaling up.

Common pitfalls to avoid when working with recursion include:

- No Base Case or Incorrect Base Case: This can lead to infinite recursion, causing the program to crash.
- Not Progressing Toward Base Case: If each recursive call doesn't reduce the problem size, you'll end up with infinite recursion.
- Excessice Overhead: Each recursive call adds a new layer to the call stack, which can lead to performance issues with large inputs.

##### 2.2 Tail Recursion and Its Benefits

Tail recursion occurs when the recursive call is the last operation in the function. This is significant because it allows for "tail call optimization" (TCO), where the compiler can optimize the recursive calls to avoid adding new frames to the call stack, effectively turning the recursion into a loop internally and preventing stack overflow errors.

Benefits of Tail Recursion:

- Improved Performance: With TCO, tail-recursive functions can run as efficiently as their iterative counterparts.
- Prevents Stack Overflow: Since TCO doesn't add new frames to the stack for each call, tail-recursive functions can handle larger inputs without crashing.

Example of Tail-Recursive Function:

```python
def factorial(n, accumulator=1):
    # Base Case
    if n == 0:
        return accumulator
    # Recursive Step
    else:
        return factorial(n - 1, n * accumulator)
```

In this example, the `accumulator` parameter is used to store the intermediate results of the factorial calculation, and the recursive call is the last operation in the function.

##### 2.3 Recursion vs. Iteration: When to Use Which

Both recursion and iteration are tools for repeating tasks, but they have different use cases.

Use Recursion When:

- The Problem is Naturally Recursive: Some problems, like tree traversals or solving puzzles like the Tower of Hanoi, are naturally suited to recursion because they break down into smaller, similar problems.
-Clarity and Simplicity: If a recursive solution is more straightforward and easier to understand than an iterative one, it might be the better choice.

Use Iteration When:

- Performance is Critical: Iterative solutions typically use less memory than recursive ones because they don't add to the call stack with each iteration.
- The Problem is Linear: For tasks that involve simple, linear steps, iteration often results in more straightforward and efficient code.

##### 2.4 In Simple Terms

- Writing Recursive Functions: Like Building a LEGO Tower
Imagine you're building a tower with your LEGO blocks. You decide to build each level of the tower by adding one block at a time until you reach the desired height.

- Best Practices:

Clear Base Case: You decide the tower will be 10 blocks high. When you place the 10th block, that's your signal to stop. That's like the base case in recursion - a clear stopping point.
Progress Towards Base Case: Each time you add a block, you're one step closer to completing your tower. In recursion, every step should get you closer to the base case.

Keep It Simple: You use the same type of block for each level to keep things simple. Similarly, a recursive function should be straightforward and not too complex.
Common Pitfalls:

No Base Case: If you didn't decide how tall your tower should be, you might keep adding blocks forever (or until you run out of blocks)! That's like a recursive function without a base case - it can go on indefinitely.

Not Progressing Towards Base Case: If you keep planning without actually adding a block, your tower will never get built. Every recursive call needs to move closer to the base case.
Tail Recursion: Passing the Baton in a Relay Race

Think of a relay race where each runner passes a baton to the next. In a normal race, every runner waits for their turn, runs, and then rests. But imagine if, as soon as a runner passes the baton, they could leave the race and not wait around.

Tail Recursion is like this efficient relay race. When a function makes its final action a call to itself (passes the baton), it doesn't need to do anything after (the runner can leave). This means we don't need extra space to keep track of all the runners; we just focus on the one running.

- Recursion vs. Iteration: Climbing Stairs

Imagine you're climbing a staircase. You can climb it step by step (iteration) or think of a smaller staircase and imagine climbing that first before tackling the rest (recursion).

- Use Recursion When:

It's like having a set of nested staircases. You conquer the smaller staircase, rest a bit, and then tackle the next one. This is good when the problem feels naturally broken down into smaller problems, like if each staircase had a different theme or game at each level.

- Use Iteration When:

If it's just a straight staircase, walking up step by step might be easier and straightforward. This is like iteration - you know exactly how many steps you need to take, and you just go one after the other until you reach the top.

