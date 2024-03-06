# Python Course

## Class 4 - Graph Algorithms - Breadth-First Search (BFS)

### Lesson Overview

- What is BFS?
- Key Concepts
- How BFS Works
- Applications
- Why BFS ?
- Exercise: Implement BFS 

#### 1. What is BFS?

Breadth-First Search (BFS) is an algorithm used to traverse or search tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

##### 1.1. Theory

A graph is data structure consisting of nodes (verticles) and edges (connections between nodes). BFS is an algorithm for traversing or searchinf tree or grap data structures. It starts at a chosen node and explores all of the neighbor nodes at the present depth prior to moving on the nodes at the next depth leve.

#### 2. Key Concepts

1. Graph: A graph is a collection of nodes and edges. It can be directed or undirected, and it can have weights or not. In programming, graphs can be represented using adjacency lists (using a hash table where keys are node identifiers and values are lists of adjacent nodes) or adjacency matrices (a 2D array where the cell at row i and column j indicates the presence/absence of an edge between nodes i and j).

2. Queue: A queue is a linear data structure that follows the First In First Out (FIFO) principle. It has two main operations: enqueue (inserting an element at the end) and dequeue (removing an element from the front). BFS uses a queue to keep track of the nodes that are next in line to be visited.
This ensure that nodes are explored in the order they were discovered.

3. Visited Array/List: A visited array or list is used to keep track of the nodes that have been visited. It's essential to avoid processing a node more than once. This is usually implemented as a boolean array, where the index represents the node identifier and the value indicates if the node has been visited or not, or hash set.

4. Level: The level of a node is the minimum number of edges that must be traversed to reach the node from the starting node. In BFS, the level of a node is also the shortest distance from the starting node to that node.

#### 3. How BFS Works

1. Start at the selected Node: The algorithm starts at the root node, mark it as visited, and enqueue it in the queue.
2. Explore the Neighbors: Dequeue the first node from the queue and explore its neighbors. Mark each neighbor as visited and enqueue it in the queue.
3. Repeat: Continue the process until the queue is empty.

```python
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

#### 4. Applications

1. Shortest Path and Minimum Spanning Tree for unweighted graph: BFS used to find the shortest path from one node to another in an unweighted graph. It's also used to find the minimum spanning tree of a graph.

2. Connectivity: BFS can be used to find all connected components in a graph. It can also determine if there is a path between two nodes in a graph.
        
3. Crawlers in Search Engines: Web crawlers use BFS to visit and index web pages starting from a root page.

4. Social Networking: BFS can be used to find people within a certain distance from a person in a social network.

Example:

Imagine a graph representing a network of friends where each node is a person and each edge represents a friendship. Using BFS, we can find the shortest chain of friends connecting two individuals, which is a common feature in social networking applications.

#### 5. Why BFS?

- Simplicity: BFS is easy to implement and understand.
- Versatility: BFS can be used to solve a wide range of problems, including finding the shortest path, connectivity, and more.
- Robustness: BFS is guaranteed to find the shortest path in an unweighted graph. (in terms of the number of edges)


#### 6. Exercise: Implement BFS

Implement a BFS algorithm in Python to find the shortest path of connections between two users in a social network. For simplicity, you can represent the social network as a graph using a dictionary where keys are user IDs and values are lists of friends' IDs.

Steps:

- Define your graph (social network).
- Implement the BFS algorithm to find the shortest path between two users.
- Test your algorithm with different user IDs to see the shortest path of connections.