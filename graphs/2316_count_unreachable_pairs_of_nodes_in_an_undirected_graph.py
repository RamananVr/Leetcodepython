"""
LeetCode Question #2316: Count Unreachable Pairs of Nodes in an Undirected Graph

Problem Statement:
You are given an integer `n`. There is an undirected graph with `n` nodes, numbered from `0` to `n - 1`. 
You are also given a 2D integer array `edges`, where `edges[i] = [ai, bi]` indicates that there is an 
undirected edge between nodes `ai` and `bi`.

Return the number of pairs of different nodes that are unreachable from each other.

Example:
Input: n = 6, edges = [[0, 1], [0, 2], [3, 4], [2, 5]]
Output: 14
Explanation: There are 3 connected components in the graph:
- Component 1: {0, 1, 2, 5}
- Component 2: {3, 4}
- Component 3: {6}
There are 14 pairs of nodes that are unreachable from each other.

Constraints:
- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- There are no duplicate edges.
"""

# Solution
from collections import defaultdict

def count_unreachable_pairs(n: int, edges: list[list[int]]) -> int:
    def dfs(node):
        # Perform DFS to find all nodes in the current connected component
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                size += 1
                stack.extend(graph[current])
        return size

    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Find sizes of all connected components
    visited = [False] * n
    component_sizes = []
    for i in range(n):
        if not visited[i]:
            component_sizes.append(dfs(i))

    # Calculate the number of unreachable pairs
    total_pairs = n * (n - 1) // 2  # Total pairs of nodes
    reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)  # Pairs within components
    return total_pairs - reachable_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    edges1 = [[0, 1], [0, 2], [3, 4], [2, 5]]
    print(count_unreachable_pairs(n1, edges1))  # Output: 14

    # Test Case 2
    n2 = 5
    edges2 = [[0, 1], [1, 2], [3, 4]]
    print(count_unreachable_pairs(n2, edges2))  # Output: 8

    # Test Case 3
    n3 = 4
    edges3 = []
    print(count_unreachable_pairs(n3, edges3))  # Output: 6

    # Test Case 4
    n4 = 1
    edges4 = []
    print(count_unreachable_pairs(n4, edges4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(edges.length).
- DFS traversal for each node takes O(n + edges.length) in total, as each node and edge is visited once.
- Calculating reachable pairs takes O(k), where k is the number of connected components.
- Overall time complexity: O(n + edges.length).

Space Complexity:
- The graph representation uses O(n + edges.length) space.
- The visited array uses O(n) space.
- The stack for DFS uses O(n) space in the worst case.
- Overall space complexity: O(n + edges.length).

Topic: Graphs
"""