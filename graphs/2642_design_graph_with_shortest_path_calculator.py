"""
LeetCode Problem #2642: Design Graph With Shortest Path Calculator

Problem Statement:
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:
- Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
- addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
- int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1)
- edges[i].length == 3
- 0 <= fromi, toi, edgeCosti <= n - 1
- fromi != toi
- There are no repeated edges.
- At most 100 calls will be made for addEdge.
- At most 100 calls will be made for shortestPath.

Examples:
Input:
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output:
[null, 6, -1, null, 6]

Explanation:
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 is: 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the edge [1, 3, 4].
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 is: 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
"""

import heapq
from collections import defaultdict

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        """
        Initialize the graph with n nodes and given edges.
        
        :param n: Number of nodes in the graph
        :param edges: List of edges [from, to, cost]
        """
        self.n = n
        self.graph = defaultdict(list)
        
        # Build adjacency list representation
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge: list[int]) -> None:
        """
        Add an edge to the graph.
        
        :param edge: Edge to add [from, to, cost]
        """
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        """
        Find the shortest path from node1 to node2 using Dijkstra's algorithm.
        
        :param node1: Starting node
        :param node2: Destination node
        :return: Minimum cost or -1 if no path exists
        """
        if node1 == node2:
            return 0
            
        # Dijkstra's algorithm
        distances = [float('inf')] * self.n
        distances[node1] = 0
        
        # Priority queue: (distance, node)
        pq = [(0, node1)]
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            
            # If we've already found a shorter path, skip
            if current_dist > distances[current_node]:
                continue
                
            # If we reached the destination, return the distance
            if current_node == node2:
                return current_dist
                
            # Explore neighbors
            for neighbor, edge_cost in self.graph[current_node]:
                new_dist = current_dist + edge_cost
                
                # If we found a shorter path to the neighbor
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        # No path found
        return -1

def build_tree_from_list(values):
    """Helper function to build a tree from a list (for testing purposes)"""
    if not values or values[0] is None:
        return None
    # This is a placeholder for tree building if needed
    return values

def tree_to_list(root):
    """Helper function to convert tree to list (for testing purposes)"""
    if not root:
        return []
    # This is a placeholder for tree conversion if needed
    return root

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("Test Case 1:")
    graph = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(graph.shortestPath(3, 2))  # Expected Output: 6 (3->0->1->2: 3+2+1=6)
    print(graph.shortestPath(0, 3))  # Expected Output: -1 (no path from 0 to 3)
    graph.addEdge([1, 3, 4])
    print(graph.shortestPath(0, 3))  # Expected Output: 6 (0->1->3: 2+4=6)
    
    # Test Case 2: Same node
    print("\nTest Case 2:")
    graph2 = Graph(3, [[0, 1, 1], [1, 2, 1]])
    print(graph2.shortestPath(0, 0))  # Expected Output: 0
    print(graph2.shortestPath(1, 1))  # Expected Output: 0
    
    # Test Case 3: No edges
    print("\nTest Case 3:")
    graph3 = Graph(3, [])
    print(graph3.shortestPath(0, 1))  # Expected Output: -1
    print(graph3.shortestPath(0, 2))  # Expected Output: -1
    
    # Test Case 4: Adding multiple edges
    print("\nTest Case 4:")
    graph4 = Graph(4, [[0, 1, 10]])
    print(graph4.shortestPath(0, 2))  # Expected Output: -1
    graph4.addEdge([1, 2, 5])
    print(graph4.shortestPath(0, 2))  # Expected Output: 15 (0->1->2: 10+5=15)
    graph4.addEdge([0, 2, 8])
    print(graph4.shortestPath(0, 2))  # Expected Output: 8 (0->2: 8)
    
    # Test Case 5: Complex graph
    print("\nTest Case 5:")
    graph5 = Graph(5, [[0, 1, 4], [0, 2, 2], [1, 3, 1], [2, 3, 5], [3, 4, 3]])
    print(graph5.shortestPath(0, 4))  # Expected Output: 8 (0->1->3->4: 4+1+3=8)
    graph5.addEdge([2, 4, 1])
    print(graph5.shortestPath(0, 4))  # Expected Output: 3 (0->2->4: 2+1=3)

"""
Time and Space Complexity Analysis:

Graph.__init__(n, edges):
- Time Complexity: O(E), where E is the number of edges
- Space Complexity: O(E) for storing the adjacency list

Graph.addEdge(edge):
- Time Complexity: O(1)
- Space Complexity: O(1)

Graph.shortestPath(node1, node2):
- Time Complexity: O(E + V log V), where V is the number of nodes and E is the number of edges
  - Dijkstra's algorithm with a priority queue
- Space Complexity: O(V) for the distances array and priority queue

Overall Design:
- The Graph class uses an adjacency list representation for efficient edge storage and traversal
- Dijkstra's algorithm is used for finding shortest paths, which is optimal for this problem
- The design supports dynamic edge addition while maintaining efficient shortest path queries

Topic: Graph, Shortest Path, Dijkstra's Algorithm
"""
