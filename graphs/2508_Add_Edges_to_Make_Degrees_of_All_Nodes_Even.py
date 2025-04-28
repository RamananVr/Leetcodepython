"""
LeetCode Problem #2508: Add Edges to Make Degrees of All Nodes Even

Problem Statement:
You are given an undirected graph with `n` nodes labeled from `1` to `n` and an array `edges` where `edges[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi`. The graph may not be connected.

You are allowed to add at most two edges to this graph. Return `true` if it is possible to make the degree of every node in the graph even by adding at most two edges, and `false` otherwise.

An undirected graph is a graph where edges have no direction. A node's degree is the number of edges connected to it.

Constraints:
- `n == number of nodes`
- `1 <= n <= 100`
- `0 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- There are no duplicate edges.

"""

def isPossible(n: int, edges: list[list[int]]) -> bool:
    from collections import defaultdict

    # Step 1: Build the adjacency list and degree count
    graph = defaultdict(set)
    degree = [0] * (n + 1)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # Step 2: Find all nodes with odd degrees
    odd_degree_nodes = [i for i in range(1, n + 1) if degree[i] % 2 == 1]

    # Step 3: Handle cases based on the number of odd-degree nodes
    if len(odd_degree_nodes) == 0:
        # All nodes already have even degrees
        return True
    elif len(odd_degree_nodes) == 2:
        # Try to connect the two odd-degree nodes directly
        u, v = odd_degree_nodes
        if v not in graph[u]:
            return True
        # Try to connect each odd-degree node to a third node
        for i in range(1, n + 1):
            if i != u and i != v and i not in graph[u] and i not in graph[v]:
                return True
    elif len(odd_degree_nodes) == 4:
        # Try to pair the four odd-degree nodes
        u, v, x, y = odd_degree_nodes
        if (v not in graph[u] and y not in graph[x]) or (x not in graph[u] and y not in graph[v]) or (y not in graph[u] and x not in graph[v]):
            return True

    # If none of the above cases work, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All nodes already have even degrees
    n1 = 4
    edges1 = [[1, 2], [2, 3], [3, 4], [4, 1]]
    print(isPossible(n1, edges1))  # Output: True

    # Test Case 2: Two odd-degree nodes can be connected
    n2 = 4
    edges2 = [[1, 2], [2, 3], [3, 4]]
    print(isPossible(n2, edges2))  # Output: True

    # Test Case 3: Four odd-degree nodes can be paired
    n3 = 6
    edges3 = [[1, 2], [2, 3], [4, 5]]
    print(isPossible(n3, edges3))  # Output: True

    # Test Case 4: Impossible to make all degrees even
    n4 = 3
    edges4 = [[1, 2], [2, 3]]
    print(isPossible(n4, edges4))  # Output: False

    # Test Case 5: No edges, all nodes have degree 0 (even)
    n5 = 5
    edges5 = []
    print(isPossible(n5, edges5))  # Output: True

"""
Time Complexity:
- Building the adjacency list and degree array takes O(E), where E is the number of edges.
- Finding odd-degree nodes takes O(N), where N is the number of nodes.
- Checking possible connections involves iterating over at most O(N) nodes.
- Overall complexity: O(N + E).

Space Complexity:
- The adjacency list uses O(E) space.
- The degree array uses O(N) space.
- Overall complexity: O(N + E).

Topic: Graphs
"""