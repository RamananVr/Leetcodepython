"""
LeetCode Problem #1319: Number of Operations to Make Network Connected

Problem Statement:
There are `n` computers numbered from `0` to `n-1` connected by ethernet cables `connections`, where `connections[i] = [a, b]` represents a connection between computers `a` and `b`. Any computer can reach any other computer directly or indirectly through the network.

You are given `n` and the list `connections`. You need to determine the minimum number of operations needed to connect all the computers. In one operation, you can remove any cable between two directly connected computers and place it between any two disconnected computers.

Return the minimum number of operations needed to connect all the computers. If it is not possible, return `-1`.

Constraints:
- `1 <= n <= 10^5`
- `1 <= connections.length <= min(10^5, n * (n - 1) / 2)`
- `connections[i].length == 2`
- `0 <= a, b < n`
- `a != b`
- There are no repeated connections.
- No two computers are connected by more than one cable.

"""

from typing import List

def makeConnected(n: int, connections: List[List[int]]) -> int:
    # If there are fewer cables than n-1, it's impossible to connect all computers
    if len(connections) < n - 1:
        return -1

    # Create an adjacency list for the graph
    graph = {i: [] for i in range(n)}
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    # Perform DFS to count the number of connected components
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Count the number of connected components
    components = 0
    for i in range(n):
        if i not in visited:
            components += 1
            dfs(i)

    # To connect all components, we need (components - 1) operations
    return components - 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    connections1 = [[0, 1], [0, 2], [1, 2]]
    print(makeConnected(n1, connections1))  # Output: 1

    # Test Case 2
    n2 = 6
    connections2 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(makeConnected(n2, connections2))  # Output: -1

    # Test Case 3
    n3 = 5
    connections3 = [[0, 1], [0, 2], [3, 4], [2, 3]]
    print(makeConnected(n3, connections3))  # Output: 0

    # Test Case 4
    n4 = 3
    connections4 = [[0, 1], [1, 2]]
    print(makeConnected(n4, connections4))  # Output: 0


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Building the adjacency list takes O(E), where E is the number of connections.
   - The DFS traversal visits each node and edge once, so it takes O(V + E), where V is the number of nodes (n).
   - Overall time complexity: O(V + E), which simplifies to O(n + connections.length).

2. Space Complexity:
   - The adjacency list requires O(V + E) space.
   - The visited set requires O(V) space.
   - The recursion stack for DFS can go as deep as O(V) in the worst case.
   - Overall space complexity: O(V + E), which simplifies to O(n + connections.length).

Topic: Graphs
"""