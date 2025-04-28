"""
LeetCode Problem #323: Number of Connected Components in an Undirected Graph

Problem Statement:
You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.

Example:
Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: 1
"""

from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
    # Helper function for DFS
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Build the adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = 0

    # Perform DFS for each unvisited node
    for node in range(n):
        if node not in visited:
            components += 1
            dfs(node)

    return components

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    print(countComponents(n1, edges1))  # Output: 2

    # Test Case 2
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(countComponents(n2, edges2))  # Output: 1

    # Test Case 3
    n3 = 4
    edges3 = [[0, 1], [2, 3]]
    print(countComponents(n3, edges3))  # Output: 2

    # Test Case 4
    n4 = 6
    edges4 = [[0, 1], [1, 2], [3, 4], [4, 5]]
    print(countComponents(n4, edges4))  # Output: 2

"""
Time Complexity:
- Building the adjacency list takes O(E), where E is the number of edges.
- The DFS traversal visits each node and edge once, so it takes O(V + E), where V is the number of nodes.
- Overall time complexity: O(V + E).

Space Complexity:
- The adjacency list takes O(V + E) space.
- The visited set takes O(V) space.
- The recursion stack for DFS can go as deep as O(V) in the worst case.
- Overall space complexity: O(V + E).

Topic: Graphs
"""