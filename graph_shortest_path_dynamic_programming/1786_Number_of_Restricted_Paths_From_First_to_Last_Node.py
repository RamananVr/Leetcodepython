"""
LeetCode Problem #1786: Number of Restricted Paths From First to Last Node

Problem Statement:
There is an undirected weighted connected graph with `n` nodes labeled from `1` to `n`, and `m` edges.

You are given an array `edges` where `edges[i] = [u, v, weight]` represents a bidirectional and weighted edge between nodes `u` and `v`. A restricted path is a path that starts at node `1` and ends at node `n`, such that for all consecutive nodes `u` and `v` on the path, `dist(u) > dist(v)`. Here, `dist(x)` is the shortest distance from node `x` to node `n`.

Return the number of restricted paths from node `1` to node `n`. Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- `1 <= n <= 2 * 10^4`
- `n - 1 <= m <= 5 * 10^4`
- `edges[i].length == 3`
- `1 <= u, v <= n`
- `u != v`
- `1 <= weight <= 10^5`
- There is at least one valid path between nodes `1` and `n`.

"""

from heapq import heappop, heappush
from collections import defaultdict
import sys

MOD = 10**9 + 7

def countRestrictedPaths(n: int, edges: list[list[int]]) -> int:
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    
    # Step 2: Dijkstra's algorithm to find shortest distances from node n
    dist = [sys.maxsize] * (n + 1)
    dist[n] = 0
    min_heap = [(0, n)]  # (distance, node)
    
    while min_heap:
        d, node = heappop(min_heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heappush(min_heap, (dist[neighbor], neighbor))
    
    # Step 3: Sort nodes by distance from node n
    nodes = sorted(range(1, n + 1), key=lambda x: dist[x])
    
    # Step 4: Dynamic programming to count restricted paths
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: there's exactly one way to reach node n from itself
    
    for node in nodes:
        for neighbor, _ in graph[node]:
            if dist[node] > dist[neighbor]:  # Restricted path condition
                dp[node] = (dp[node] + dp[neighbor]) % MOD
    
    return dp[1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]
    n1 = 5
    print(countRestrictedPaths(n1, edges1))  # Expected Output: 3

    # Test Case 2
    edges2 = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [1, 5, 10]]
    n2 = 5
    print(countRestrictedPaths(n2, edges2))  # Expected Output: 1

"""
Time Complexity:
- Dijkstra's algorithm: O((n + m) * log(n)), where `n` is the number of nodes and `m` is the number of edges.
- Sorting nodes by distance: O(n * log(n)).
- Dynamic programming traversal: O(m), as we iterate over all edges.
Overall: O((n + m) * log(n)).

Space Complexity:
- Graph representation: O(m) for adjacency list.
- Distance array: O(n).
- DP array: O(n).
- Min-heap: O(n).
Overall: O(n + m).

Topic: Graph, Shortest Path, Dynamic Programming
"""