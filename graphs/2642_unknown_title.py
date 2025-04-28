"""
LeetCode Problem #2642: Design Graph With Shortest Path Calculator

Problem Statement:
You are tasked with designing a graph data structure that supports the following operations:

1. `addEdge(int u, int v, int weight)`: Adds a directed edge from node `u` to node `v` with a given `weight`. 
   If an edge already exists, the weight is updated to the new value.

2. `shortestPath(int start, int end)`: Returns the shortest path distance from node `start` to node `end`. 
   If there is no path between the two nodes, return `-1`.

Implement the `Graph` class:

- `Graph()`: Initializes the graph object.
- `addEdge(int u, int v, int weight)`: Adds or updates a directed edge in the graph.
- `shortestPath(int start, int end)`: Returns the shortest path distance between two nodes.

Constraints:
- The number of nodes in the graph is not fixed and can grow dynamically as edges are added.
- The graph may contain cycles.
- The weights of the edges are non-negative integers.
- The graph is directed.

Example:
Input:
    graph = Graph()
    graph.addEdge(1, 2, 4)
    graph.addEdge(2, 3, 3)
    graph.addEdge(1, 3, 7)
    print(graph.shortestPath(1, 3))  # Output: 7
    print(graph.shortestPath(3, 1))  # Output: -1
"""

import heapq
from collections import defaultdict
import math

class Graph:
    def __init__(self):
        # Adjacency list to store the graph
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int, weight: int) -> None:
        """
        Adds a directed edge from node u to node v with the given weight.
        If the edge already exists, updates the weight.
        """
        # Remove any existing edge from u to v
        self.graph[u] = [(node, w) for node, w in self.graph[u] if node != v]
        # Add the new edge
        self.graph[u].append((v, weight))

    def shortestPath(self, start: int, end: int) -> int:
        """
        Returns the shortest path distance from node start to node end.
        If no path exists, returns -1.
        """
        # Min-heap for Dijkstra's algorithm
        min_heap = [(0, start)]  # (distance, node)
        # Dictionary to store the shortest distance to each node
        distances = {start: 0}

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            # If we reach the target node, return the distance
            if current_node == end:
                return current_distance

            # If the current distance is greater than the recorded distance, skip
            if current_distance > distances.get(current_node, math.inf):
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                # If a shorter path to the neighbor is found
                if distance < distances.get(neighbor, math.inf):
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        # If the end node is not reachable, return -1
        return -1


# Example Test Cases
if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(1, 2, 4)
    graph.addEdge(2, 3, 3)
    graph.addEdge(1, 3, 7)
    print(graph.shortestPath(1, 3))  # Output: 7
    print(graph.shortestPath(3, 1))  # Output: -1
    graph.addEdge(1, 3, 2)
    print(graph.shortestPath(1, 3))  # Output: 2
    graph.addEdge(3, 4, 1)
    graph.addEdge(4, 2, 1)
    print(graph.shortestPath(1, 4))  # Output: 3
    print(graph.shortestPath(1, 5))  # Output: -1


"""
Time and Space Complexity Analysis:

1. `addEdge`:
   - Time Complexity: O(E), where E is the number of edges from node `u`. This is because we may need to iterate through the adjacency list of `u` to remove an existing edge.
   - Space Complexity: O(1) additional space.

2. `shortestPath`:
   - Time Complexity: O((V + E) * log(V)), where V is the number of nodes and E is the number of edges. This is the complexity of Dijkstra's algorithm using a priority queue.
   - Space Complexity: O(V + E) for storing the graph and the distances dictionary.

Topic: Graphs
"""