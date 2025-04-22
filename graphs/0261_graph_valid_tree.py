"""
LeetCode Question #261: Graph Valid Tree

Problem Statement:
You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

A valid tree has the following properties:
1. It is connected: There is a path between any two nodes.
2. It contains no cycles: The graph is acyclic.

Constraints:
- `1 <= n <= 2000`
- `0 <= edges.length <= 2000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- There are no duplicate edges.

"""

from collections import defaultdict, deque

def validTree(n: int, edges: list[list[int]]) -> bool:
    # A valid tree must have exactly n - 1 edges
    if len(edges) != n - 1:
        return False

    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Perform BFS to check connectivity
    visited = set()
    queue = deque([0])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    # Check if all nodes are visited (graph is connected)
    return len(visited) == n


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: A valid tree
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(n1, edges1))  # Expected output: True

    # Test Case 2: Not a valid tree (contains a cycle)
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(validTree(n2, edges2))  # Expected output: False

    # Test Case 3: Not a valid tree (not connected)
    n3 = 4
    edges3 = [[0, 1], [2, 3]]
    print(validTree(n3, edges3))  # Expected output: False

    # Test Case 4: Single node (valid tree)
    n4 = 1
    edges4 = []
    print(validTree(n4, edges4))  # Expected output: True

    # Test Case 5: Two nodes with one edge (valid tree)
    n5 = 2
    edges5 = [[0, 1]]
    print(validTree(n5, edges5))  # Expected output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(E), where E is the number of edges.
- BFS traversal visits each node and edge once, so it takes O(V + E), where V is the number of nodes.
- Overall time complexity: O(V + E).

Space Complexity:
- The adjacency list requires O(V + E) space.
- The visited set and queue require O(V) space.
- Overall space complexity: O(V + E).

Topic: Graphs
"""