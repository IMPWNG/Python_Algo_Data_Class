from collections import deque
import json

class Graph:
    def __init__(self, filepath, start, goal):
        with open(filepath, "r") as file:
            data = json.load(file)
            
        # Assuming there's only one social network in the file
        if "socialNetworks" in data and len(data["socialNetworks"]) > 0:
            self.graph = data["socialNetworks"][0] # Load the graph from the file.
        else:
            raise ValueError("The file does not contain a social network.")
        self.start = start
        self.goal = goal
        
        #Debug 
        # print("Loaded graph:", self.graph)
        
        # if self.start not in self.graph:
        #     raise ValueError(f"The start node {self.start} is not in the graph.")
        # if self.goal not in self.graph and not any(self.goal in neighbors for neighbors in self.graph.values()):
        #     raise ValueError(f"The goal node {self.goal} is not in the graph.")

    def bfs(self):
        self.visited = set() # Set to keep track of visited nodes.
        self.queue = deque([(self.start, [self.start])]) # Initialize the queue with the start node.
        
        while self.queue:
            current_node, path = self.queue.popleft() # Get the first element from the queue.
            if current_node == self.goal:
                return path
            
            for neighbor in self.graph[current_node]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor) # Mark the node as visited.
                    self.queue.append((neighbor, path + [neighbor])) # Add the neighbor to the queue.
                    
        return "No path exists between the start and goal nodes."
    
    def print_path(self):
        path = self.bfs()
        if isinstance(path, list): # Ensure the BFS algorithm returned a valid path.
            num_nodes = len(path) - 2 # Subtract 2 to exclude the start and goal nodes.
            print(f"The path from {self.start} to {self.goal} is {path} and it contains {num_nodes} nodes.")
        else:
            print(path)

# Example usage
filepath = "socialNetwork.json"
start_node = "Alice"
goal_node = "Dennis"

graph = Graph(filepath, start_node, goal_node)
graph.print_path()
