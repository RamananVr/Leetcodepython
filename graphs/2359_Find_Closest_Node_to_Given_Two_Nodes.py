"""
LeetCode Problem #2359: Find Closest Node to Given Two Nodes

Problem Statement:
You are given a directed graph of `n` nodes numbered from `0` to `n - 1`, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from node `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

Return the index of the node that can be reached from both `node1` and `node2`, such that the maximum distance from `node1` to that node and from `node2` to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no such node exists, return `-1`.

Note that `edges` may contain cycles.

Constraints:
- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`
- `edges[i] != i`
- `0 <= node1, node2 < n`
"""

from collections import deque

def findClosestNode(edges, node1, node2):
    def bfs(start):
        """Helper function to calculate distances from a given start node."""
        distances = [-1] * len(edges)
        queue = deque([start])
        distances[start] = 0
        while queue:
            current = queue.popleft()
            neighbor = edges[current]
            if neighbor != -1 and distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
        return distances

    # Calculate distances from node1 and node2
    dist1 = bfs(node1)
    dist2 = bfs(node2)

    # Find the closest node
    min_distance = float('inf')
    result = -1
    for i in range(len(edges)):
        if dist1[i] != -1 and dist2[i] != -1:
            max_dist = max(dist1[i], dist2[i])
            if max_dist < min_distance or (max_dist == min_distance and i < result):
                min_distance = max_dist
                result = i

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    print(findClosestNode(edges, node1, node2))  # Output: 2

    # Test Case 2
    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    print(findClosestNode(edges, node1, node2))  # Output: 2

    # Test Case 3
    edges = [-1, 0, -1, 4, 2]
    node1 = 1
    node2 = 3
    print(findClosestNode(edges, node1, node2))  # Output: -1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The BFS function runs in O(n) time for each node since it visits each node at most once.
   - We call BFS twice (once for `node1` and once for `node2`), so the total time complexity is O(n).

2. Space Complexity:
   - The `distances` array used in BFS takes O(n) space.
   - The queue used in BFS also takes O(n) space in the worst case.
   - Therefore, the total space complexity is O(n).

Topic: Graphs
"""