"""
LeetCode Question #1364: Number of Trusted Connections

Problem Statement:
You are given an integer n representing the number of people in a social network, labeled from 1 to n. 
You are also given a list of pairs `connections`, where each pair [a, b] represents a trusted connection 
between person a and person b. A trusted connection is bidirectional, meaning if person a trusts person b, 
then person b also trusts person a.

Your task is to determine the number of connected components in the social network. A connected component 
is a group of people such that every person in the group is directly or indirectly connected to every other 
person in the group.

Write a function `countComponents(n: int, connections: List[List[int]]) -> int` that returns the number of 
connected components in the social network.

Constraints:
- 1 <= n <= 10^4
- 0 <= len(connections) <= 10^4
- connections[i].length == 2
- 1 <= connections[i][0], connections[i][1] <= n
- connections[i][0] != connections[i][1]
- There are no duplicate connections.

Example:
Input: n = 5, connections = [[1, 2], [2, 3], [4, 5]]
Output: 2
Explanation: There are two connected components: {1, 2, 3} and {4, 5}.
"""

from typing import List

def countComponents(n: int, connections: List[List[int]]) -> int:
    # Helper function for DFS traversal
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Build the graph as an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    # Perform DFS to count connected components
    visited = set()
    components = 0

    for node in range(1, n + 1):
        if node not in visited:
            components += 1
            dfs(node)

    return components

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    connections1 = [[1, 2], [2, 3], [4, 5]]
    print(countComponents(n1, connections1))  # Output: 2

    # Test Case 2
    n2 = 4
    connections2 = [[1, 2], [2, 3], [3, 4]]
    print(countComponents(n2, connections2))  # Output: 1

    # Test Case 3
    n3 = 6
    connections3 = [[1, 2], [3, 4], [5, 6]]
    print(countComponents(n3, connections3))  # Output: 3

    # Test Case 4
    n4 = 3
    connections4 = []
    print(countComponents(n4, connections4))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(len(connections)).
- DFS traversal for each node takes O(V + E), where V is the number of nodes (n) and E is the number of edges (len(connections)).
- In the worst case, we traverse all nodes and edges, so the overall time complexity is O(n + len(connections)).

Space Complexity:
- The graph representation as an adjacency list takes O(n + len(connections)).
- The visited set takes O(n) space.
- The recursion stack for DFS can take up to O(n) space in the worst case.
- Overall space complexity is O(n + len(connections)).

Topic: Graphs
"""