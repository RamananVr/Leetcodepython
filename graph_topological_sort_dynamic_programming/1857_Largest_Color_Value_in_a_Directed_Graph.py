"""
LeetCode Problem #1857: Largest Color Value in a Directed Graph

Problem Statement:
There is a directed graph of `n` colored nodes and `m` edges. The nodes are numbered from `0` to `n - 1`.

You are given a string `colors` where `colors[i]` is a lowercase English letter representing the color of the `i-th` node in this graph (0-indexed). You are also given a 2D array `edges` where `edges[j] = [aj, bj]` indicates that there is a directed edge from node `aj` to node `bj`.

A valid path in the graph is a sequence of nodes `x1 -> x2 -> x3 -> ... -> xk` such that there is a directed edge from `xi` to `xi+1` for every `1 <= i < k`. The color value of the path is the number of nodes that are colored with the most frequent color along that path.

Return the largest color value of any valid path in the given graph, or `-1` if the graph contains a cycle.

Constraints:
- `n == colors.length`
- `m == edges.length`
- `1 <= n <= 10^5`
- `0 <= m <= 10^5`
- `colors` consists of lowercase English letters.
- `0 <= aj, bj < n`

"""

from collections import defaultdict, deque

def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    graph = defaultdict(list)
    in_degree = [0] * n

    # Build the graph and calculate in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Topological sort using Kahn's algorithm
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the topological order does not include all nodes, there is a cycle
    if len(topo_order) != n:
        return -1

    # DP to calculate the largest color value
    dp = [[0] * 26 for _ in range(n)]  # dp[node][c] = max count of color c at node
    max_color_value = 0

    for node in topo_order:
        color_index = ord(colors[node]) - ord('a')
        dp[node][color_index] += 1  # Increment the count of the node's color
        max_color_value = max(max_color_value, dp[node][color_index])

        for neighbor in graph[node]:
            for c in range(26):
                dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])

    return max_color_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    print(largestPathValue(colors, edges))  # Output: 3

    # Test Case 2
    colors = "a"
    edges = [[0, 0]]
    print(largestPathValue(colors, edges))  # Output: -1

    # Test Case 3
    colors = "abc"
    edges = [[0, 1], [1, 2]]
    print(largestPathValue(colors, edges))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph and calculating in-degrees: O(m), where m is the number of edges.
- Topological sort (Kahn's algorithm): O(n + m), where n is the number of nodes and m is the number of edges.
- DP computation: O(n * 26) = O(n), since we iterate over all nodes and process 26 colors for each node.
Overall: O(n + m)

Space Complexity:
- Graph representation: O(n + m) for adjacency list.
- In-degree array: O(n).
- DP table: O(n * 26) = O(n).
Overall: O(n + m)

Topic: Graph, Topological Sort, Dynamic Programming
"""