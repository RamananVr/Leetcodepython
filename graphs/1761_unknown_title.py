"""
LeetCode Problem #1761: Minimum Degree of a Connected Trio in a Graph

Problem Statement:
You are given an undirected graph represented by an integer `n`, the number of nodes, and an array `edges`, 
where each edge is a pair of integers `[u, v]` representing an undirected edge connecting nodes `u` and `v`. 
A connected trio is a set of three nodes that are connected to each other.

The degree of a connected trio is defined as the total number of edges incident to the three nodes of the trio, 
excluding the edges that are part of the trio.

Return the minimum degree of a connected trio in the graph, or -1 if no connected trio exists.

Constraints:
- 2 <= n <= 400
- edges[i].length == 2
- 1 <= u, v <= n
- u != v
- There are no duplicate edges.
- The graph is undirected.

Example:
Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: The graph contains a connected trio (1, 2, 3) with a degree of 3.

"""

# Solution
def minTrioDegree(n, edges):
    from collections import defaultdict

    # Step 1: Build adjacency list and degree count
    graph = defaultdict(set)
    degree = [0] * (n + 1)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # Step 2: Find connected trios and calculate their degree
    min_degree = float('inf')
    for u in range(1, n + 1):
        for v in graph[u]:
            if v > u:  # Avoid duplicate processing
                for w in graph[u]:
                    if w > u and w in graph[v]:  # Trio found: u, v, w
                        # Calculate degree of the trio
                        trio_degree = degree[u] + degree[v] + degree[w] - 6
                        min_degree = min(min_degree, trio_degree)

    return min_degree if min_degree != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    edges1 = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
    print(minTrioDegree(n1, edges1))  # Output: 3

    # Test Case 2
    n2 = 7
    edges2 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]
    print(minTrioDegree(n2, edges2))  # Output: -1 (No connected trio exists)

    # Test Case 3
    n3 = 5
    edges3 = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 3], [1, 4], [2, 4]]
    print(minTrioDegree(n3, edges3))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list and degree array takes O(E), where E is the number of edges.
- For each node u, we iterate over its neighbors v and check for common neighbors w. 
  This results in a worst-case complexity of O(n^3) for a dense graph.
- Overall time complexity: O(n^3) in the worst case.

Space Complexity:
- The adjacency list requires O(E) space.
- The degree array requires O(n) space.
- Overall space complexity: O(E + n).

Topic: Graphs
"""