"""
LeetCode Problem #2360: Longest Cycle in a Graph

Problem Statement:
You are given a directed graph of `n` nodes numbered from `0` to `n - 1`, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from node `i`, then `edges[i] == -1`.

Return the length of the longest cycle in the graph. If no cycle exists, return `-1`.

A cycle is a path that starts and ends at the same node.

Constraints:
- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`

Example:
Input: edges = [3, 3, 4, 2, 3]
Output: 3
Explanation: The longest cycle is the cycle: 2 -> 4 -> 3 -> 2. The length is 3.

Input: edges = [2, -1, 3, 1]
Output: -1
Explanation: There are no cycles in this graph.
"""

# Python Solution
def longestCycle(edges):
    """
    Finds the length of the longest cycle in a directed graph.

    :param edges: List[int] - The graph represented as an adjacency list.
    :return: int - The length of the longest cycle, or -1 if no cycle exists.
    """
    n = len(edges)
    visited = [False] * n
    in_cycle = [-1] * n  # Stores the index of the node in the current cycle path

    longest = -1

    for start in range(n):
        if visited[start]:
            continue

        current = start
        path_index = 0
        path_map = {}

        while current != -1 and not visited[current]:
            visited[current] = True
            path_map[current] = path_index
            in_cycle[current] = path_index
            path_index += 1
            current = edges[current]

        if current != -1 and current in path_map:
            cycle_length = path_index - path_map[current]
            longest = max(longest, cycle_length)

    return longest


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Cycle exists
    edges1 = [3, 3, 4, 2, 3]
    print(longestCycle(edges1))  # Output: 3

    # Test Case 2: No cycle exists
    edges2 = [2, -1, 3, 1]
    print(longestCycle(edges2))  # Output: -1

    # Test Case 3: Single cycle
    edges3 = [1, 2, 0]
    print(longestCycle(edges3))  # Output: 3

    # Test Case 4: Multiple disconnected components
    edges4 = [1, 2, -1, 4, 5, 3]
    print(longestCycle(edges4))  # Output: 3

    # Test Case 5: Self-loop
    edges5 = [0, -1, -1]
    print(longestCycle(edges5))  # Output: 1


# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node is visited at most once, and each edge is traversed at most once.
- Therefore, the time complexity is O(n), where n is the number of nodes.

Space Complexity:
- The `visited` array and `in_cycle` array each take O(n) space.
- The `path_map` dictionary can store up to O(n) entries in the worst case.
- Therefore, the space complexity is O(n).
"""

# Topic: Graphs