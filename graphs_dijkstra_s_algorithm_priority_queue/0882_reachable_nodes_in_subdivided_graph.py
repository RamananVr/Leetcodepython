"""
LeetCode Question #882: Reachable Nodes In Subdivided Graph

Problem Statement:
You are given an undirected graph (the "original graph") with `n` nodes, labeled from `0` to `n - 1`. 
You are given a 2D integer array `edges`, where `edges[i] = [u, v, cnt]` indicates that there is an edge 
between nodes `u` and `v`, and there are `cnt` new nodes on that edge. 

Note that the `cnt` new nodes are not part of the original graph, and the edge's endpoints `u` and `v` 
are part of the original graph.

You are also given an integer `maxMoves`, which indicates the maximum number of moves you can make.

You can start at any node, and you can move to any node (including new nodes) that is a neighbor of the 
current node.

Return the number of nodes that you can reach in the graph, including both the original nodes and the 
new nodes.

Constraints:
- `0 <= edges.length <= 10^4`
- `edges[i].length == 3`
- `0 <= u < n`
- `0 <= v < n`
- `0 <= cnt <= 10^4`
- `0 <= maxMoves <= 10^9`
- `1 <= n <= 3000`
- The graph may have multiple edges between two nodes.

"""

from heapq import heappop, heappush
from collections import defaultdict

def reachableNodes(edges, maxMoves, n):
    # Build the graph as an adjacency list
    graph = defaultdict(dict)
    for u, v, cnt in edges:
        graph[u][v] = cnt
        graph[v][u] = cnt

    # Dijkstra's algorithm to find the maximum reachable nodes
    pq = [(-maxMoves, 0)]  # Priority queue: (-remaining_moves, node)
    visited = {}
    reachable = 0

    while pq:
        moves_left, node = heappop(pq)
        moves_left = -moves_left  # Convert back to positive

        if node in visited:
            continue
        visited[node] = moves_left
        reachable += 1  # Count the original node

        for neighbor, cnt in graph[node].items():
            # If we haven't visited the neighbor, calculate the moves left
            if neighbor not in visited and moves_left > cnt:
                heappush(pq, (-(moves_left - cnt - 1), neighbor))

            # Count the reachable new nodes on the edge
            reachable += min(moves_left, cnt)
            graph[neighbor][node] -= min(moves_left, cnt)

    return reachable

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
    maxMoves = 6
    n = 3
    print(reachableNodes(edges, maxMoves, n))  # Output: 13

    # Test Case 2
    edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8]]
    maxMoves = 10
    n = 3
    print(reachableNodes(edges, maxMoves, n))  # Output: 23

    # Test Case 3
    edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 1], [3, 4, 1]]
    maxMoves = 17
    n = 5
    print(reachableNodes(edges, maxMoves, n))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(E), where E is the number of edges.
- Dijkstra's algorithm runs in O((V + E) * log(V)), where V is the number of nodes.
- In the worst case, V = n and E = len(edges), so the complexity is O((n + len(edges)) * log(n)).

Space Complexity:
- The graph representation takes O(E).
- The priority queue and visited dictionary take O(V).
- Overall, the space complexity is O(n + len(edges)).

Topic: Graphs, Dijkstra's Algorithm, Priority Queue
"""