"""
LeetCode Problem #2203: Minimum Weighted Subgraph With the Required Paths

Problem Statement:
You are given a positive integer `n` representing the number of nodes in a weighted directed graph. The nodes are numbered from `0` to `n - 1`.

You are also given a 2D array `edges` where `edges[i] = [ui, vi, weighti]` indicates that there is a directed edge from node `ui` to node `vi` with a weight of `weighti`.

You are given three distinct integers `src1`, `src2`, and `dest` representing three nodes in the graph.

Find the minimum weight of a subgraph of the graph such that it is possible to reach `dest` from both `src1` and `src2` via any path. In the subgraph, you can delete some edges, but the edges that remain must retain their original weights.

Return the minimum weight of the subgraph. If there is no such subgraph, return `-1`.

Constraints:
- `1 <= n <= 10^5`
- `1 <= edges.length <= 10^5`
- `edges[i].length == 3`
- `0 <= ui, vi < n`
- `1 <= weighti <= 10^5`
- `src1 != src2`, `src1 != dest`, `src2 != dest`

"""

from heapq import heappop, heappush
from collections import defaultdict
import sys

def minimumWeight(n, edges, src1, src2, dest):
    def dijkstra(start, graph):
        """Helper function to perform Dijkstra's algorithm."""
        dist = [float('inf')] * n
        dist[start] = 0
        min_heap = [(0, start)]  # (distance, node)
        
        while min_heap:
            d, node = heappop(min_heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(min_heap, (new_dist, neighbor))
        
        return dist

    # Build the graph and its reverse graph
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))
    
    # Perform Dijkstra's algorithm from src1, src2, and dest
    dist_from_src1 = dijkstra(src1, graph)
    dist_from_src2 = dijkstra(src2, graph)
    dist_to_dest = dijkstra(dest, reverse_graph)
    
    # Calculate the minimum weight
    min_weight = float('inf')
    for i in range(n):
        if dist_from_src1[i] != float('inf') and dist_from_src2[i] != float('inf') and dist_to_dest[i] != float('inf'):
            min_weight = min(min_weight, dist_from_src1[i] + dist_from_src2[i] + dist_to_dest[i])
    
    return min_weight if min_weight != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [3, 4, 4], [5, 4, 2]]
    src1 = 0
    src2 = 1
    dest = 4
    print(minimumWeight(n, edges, src1, src2, dest))  # Output: 9

    # Test Case 2
    n = 3
    edges = [[0, 1, 1], [1, 2, 1], [2, 0, 1]]
    src1 = 0
    src2 = 1
    dest = 2
    print(minimumWeight(n, edges, src1, src2, dest))  # Output: -1

"""
Time Complexity:
- Building the graph and reverse graph takes O(E), where E is the number of edges.
- Dijkstra's algorithm runs in O((V + E) * log(V)), where V is the number of nodes.
- Since we run Dijkstra's algorithm three times, the total time complexity is O(3 * (V + E) * log(V)) = O((V + E) * log(V)).

Space Complexity:
- The space complexity is O(V + E) for storing the graph and reverse graph.
- Additionally, we use O(V) space for the distance arrays and the priority queue in Dijkstra's algorithm.
- Overall, the space complexity is O(V + E).

Topic: Graphs, Dijkstra's Algorithm
"""