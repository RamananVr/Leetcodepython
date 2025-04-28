"""
LeetCode Problem #2699: Modify Graph Edge Weights

Problem Statement:
You are given an undirected graph with `n` nodes labeled from `0` to `n - 1`, represented by a 2D integer array `edges` where `edges[i] = [u_i, v_i, w_i]` denotes that there exists an undirected edge connecting nodes `u_i` and `v_i` with weight `w_i`.

Some edges have a weight of `-1` (indicating that their weight is unknown), while others have a positive weight (indicating that their weight is fixed). Your task is to modify all edges with a weight of `-1` by assigning them positive integer weights in such a way that the shortest distance between the source node `src` and the destination node `dest` becomes exactly equal to an integer `target`. If it is not possible to achieve such a modification, return an empty array.

Return the modified graph as an array of edges. If there are multiple solutions, return any of them. If no solution exists, return an empty array.

Constraints:
- `n == edges.length`
- `1 <= n <= 100`
- `1 <= edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `w_i == -1 or 1 <= w_i <= 10^6`
- `1 <= target <= 10^9`
- `0 <= src, dest < n`
- The graph is connected.

---

Solution:
"""

from heapq import heappop, heappush
import math

def modifyGraphEdges(n, edges, src, dest, target):
    def dijkstra(start, graph):
        dist = [math.inf] * n
        dist[start] = 0
        pq = [(0, start)]  # (distance, node)
        
        while pq:
            d, node = heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                if weight == -1:
                    weight = 1  # Temporarily treat -1 as 1
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(pq, (new_dist, neighbor))
        return dist

    # Build the graph
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Step 1: Check if the target distance is achievable
    dist_from_src = dijkstra(src, graph)
    if dist_from_src[dest] < target:
        return []  # Target is too large to achieve

    # Step 2: Modify the graph to achieve the target distance
    for i, (u, v, w) in enumerate(edges):
        if w == -1:
            edges[i][2] = 1  # Assign a temporary weight of 1

    # Rebuild the graph with updated weights
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist_from_src = dijkstra(src, graph)
    if dist_from_src[dest] != target:
        return []  # Not possible to achieve the target distance

    return edges

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [3, 4, 2]]
    src = 0
    dest = 4
    target = 6
    print(modifyGraphEdges(n, edges, src, dest, target))  # Expected: Modified edges to achieve target distance

    # Test Case 2
    n = 3
    edges = [[0, 1, -1], [1, 2, -1], [0, 2, 3]]
    src = 0
    dest = 2
    target = 5
    print(modifyGraphEdges(n, edges, src, dest, target))  # Expected: Modified edges to achieve target distance

    # Test Case 3
    n = 4
    edges = [[0, 1, 2], [1, 2, -1], [2, 3, -1]]
    src = 0
    dest = 3
    target = 10
    print(modifyGraphEdges(n, edges, src, dest, target))  # Expected: []

"""
Time Complexity:
- Dijkstra's algorithm runs in O((V + E) * log(V)), where V is the number of nodes and E is the number of edges.
- In the worst case, we may need to run Dijkstra's algorithm multiple times, so the overall complexity is O(k * (V + E) * log(V)), where k is the number of iterations.

Space Complexity:
- The space complexity is O(V + E) due to the adjacency list representation of the graph and the distance array.

Topic: Graphs, Dijkstra's Algorithm
"""