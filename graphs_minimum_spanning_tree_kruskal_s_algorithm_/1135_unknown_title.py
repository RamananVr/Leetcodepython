"""
LeetCode Problem #1135: Connecting Cities With Minimum Cost

Problem Statement:
There are `n` cities labeled from 1 to `n`. You are given an array `connections` where 
`connections[i] = [city1, city2, cost]` represents the cost to connect city1 and city2 together. 
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost to connect all the `n` cities such that there is at least one path between 
each pair of cities. If it is impossible to connect all the cities, return -1.

The cost is the sum of the connection costs used. A valid solution uses exactly `n-1` connections 
to connect all the cities.

Constraints:
- 1 <= n <= 1000
- 1 <= connections.length <= 10^4
- connections[i].length == 3
- 1 <= city1, city2 <= n
- city1 != city2
- 0 <= cost <= 10^5
- The graph may not be connected initially.
"""

from typing import List

def minimumCost(n: int, connections: List[List[int]]) -> int:
    # Helper function to find the root of a node in the Union-Find structure
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])  # Path compression
        return parent[x]

    # Helper function to union two sets in the Union-Find structure
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        return False

    # Sort connections by cost (Kruskal's algorithm)
    connections.sort(key=lambda x: x[2])

    # Initialize Union-Find structure
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    total_cost = 0
    edges_used = 0

    # Process each connection
    for city1, city2, cost in connections:
        if union(parent, rank, city1, city2):
            total_cost += cost
            edges_used += 1
            # If we have used exactly n-1 edges, we can stop
            if edges_used == n - 1:
                return total_cost

    # If we used fewer than n-1 edges, the graph is not fully connected
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    n1 = 3
    connections1 = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    print(minimumCost(n1, connections1))  # Expected output: 6

    # Test Case 2: Impossible to connect all cities
    n2 = 4
    connections2 = [[1, 2, 3], [3, 4, 4]]
    print(minimumCost(n2, connections2))  # Expected output: -1

    # Test Case 3: Already connected graph
    n3 = 4
    connections3 = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 1, 4]]
    print(minimumCost(n3, connections3))  # Expected output: 6

    # Test Case 4: Large input with minimum connections
    n4 = 5
    connections4 = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]]
    print(minimumCost(n4, connections4))  # Expected output: 4

"""
Time Complexity:
- Sorting the connections takes O(E * log(E)), where E is the number of edges (connections).
- Union-Find operations (find and union) are nearly constant time, O(α(n)), where α is the inverse Ackermann function.
- In the worst case, we process all edges, so the total complexity is O(E * log(E) + E * α(n)).
- Since α(n) is very small, the complexity is effectively O(E * log(E)).

Space Complexity:
- The Union-Find structure requires O(n) space for the parent and rank arrays.
- Sorting the connections does not require additional space beyond the input.
- Total space complexity is O(n).

Topic: Graphs (Minimum Spanning Tree, Kruskal's Algorithm)
"""