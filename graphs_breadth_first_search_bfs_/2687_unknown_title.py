"""
LeetCode Problem #2687: Find the Smallest Cycle in a Graph

Problem Statement:
You are given an undirected graph represented as an adjacency list. The graph contains `n` nodes labeled from `0` to `n-1`. 
Your task is to find the length of the smallest cycle in the graph. A cycle is a path that starts and ends at the same node, 
and it must contain at least one edge. If there is no cycle in the graph, return -1.

Input:
- `n` (int): The number of nodes in the graph.
- `edges` (List[List[int]]): A list of edges where each edge is represented as a pair of integers `[u, v]` indicating an 
  undirected edge between nodes `u` and `v`.

Output:
- (int): The length of the smallest cycle in the graph, or -1 if no cycle exists.

Constraints:
- `1 <= n <= 1000`
- `0 <= edges.length <= 3000`
- `0 <= u, v < n`
- `u != v`
- There are no duplicate edges.

Example:
Input: n = 4, edges = [[0, 1], [1, 2], [2, 0], [1, 3]]
Output: 3
Explanation: The smallest cycle is 0 -> 1 -> 2 -> 0, which has a length of 3.

Input: n = 4, edges = [[0, 1], [1, 2], [2, 3]]
Output: -1
Explanation: There is no cycle in the graph.
"""

from collections import deque, defaultdict

def findShortestCycle(n, edges):
    """
    Finds the length of the smallest cycle in an undirected graph.

    :param n: int - Number of nodes in the graph
    :param edges: List[List[int]] - List of edges in the graph
    :return: int - Length of the smallest cycle, or -1 if no cycle exists
    """
    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        """Performs BFS to find the shortest cycle starting from a given node."""
        visited = [-1] * n  # Distance from the start node
        queue = deque([(start, -1)])  # (current_node, parent_node)
        visited[start] = 0

        while queue:
            current, parent = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == -1:  # If the neighbor is not visited
                    visited[neighbor] = visited[current] + 1
                    queue.append((neighbor, current))
                elif neighbor != parent:  # If a cycle is detected
                    return visited[current] + visited[neighbor] + 1
        return float('inf')

    # Find the shortest cycle in the graph
    shortest_cycle = float('inf')
    for i in range(n):
        shortest_cycle = min(shortest_cycle, bfs(i))

    return shortest_cycle if shortest_cycle != float('inf') else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(findShortestCycle(n1, edges1))  # Output: 3

    # Test Case 2
    n2 = 4
    edges2 = [[0, 1], [1, 2], [2, 3]]
    print(findShortestCycle(n2, edges2))  # Output: -1

    # Test Case 3
    n3 = 6
    edges3 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 4]]
    print(findShortestCycle(n3, edges3))  # Output: 4

    # Test Case 4
    n4 = 3
    edges4 = [[0, 1], [1, 2], [2, 0]]
    print(findShortestCycle(n4, edges4))  # Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(E), where E is the number of edges.
- For each node, we perform a BFS. In the worst case, BFS visits all nodes and edges, taking O(V + E) time.
- Since we perform BFS for each node, the total time complexity is O(V * (V + E)), where V is the number of nodes.

Space Complexity:
- The adjacency list takes O(V + E) space.
- The BFS queue and visited array take O(V) space.
- Overall space complexity is O(V + E).

Topic: Graphs, Breadth-First Search (BFS)
"""