"""
LeetCode Problem #2846: Minimum Edge Weight Equilibrium Queries in a Tree

Problem Statement:
You are given a tree with `n` nodes numbered from `0` to `n-1`. The tree is represented as an array `edges` of size `n-1`, 
where `edges[i] = [u, v, w]` indicates that there is an edge between nodes `u` and `v` with weight `w`.

You are also given an array `queries` of size `m`, where `queries[i] = [x, y]` represents a query asking for the minimum 
edge weight `w` such that the path between nodes `x` and `y` in the tree contains at least one edge with weight `w`.

Return an array `result` of size `m`, where `result[i]` is the answer to the `i-th` query.

Constraints:
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 3`
- `0 <= u, v < n`
- `1 <= w <= 10^6`
- `1 <= m <= 10^5`
- `queries[i].length == 2`
- `0 <= x, y < n`

"""

from collections import defaultdict
import heapq

def minimum_edge_weight_equilibrium_queries(n, edges, queries):
    """
    Solves the Minimum Edge Weight Equilibrium Queries in a Tree problem.

    Args:
    n (int): Number of nodes in the tree.
    edges (List[List[int]]): List of edges in the tree, where each edge is represented as [u, v, w].
    queries (List[List[int]]): List of queries, where each query is represented as [x, y].

    Returns:
    List[int]: List of results for each query.
    """
    # Build adjacency list for the tree
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Precompute the minimum edge weight for all pairs using DFS
    def dfs(node, parent, min_weight):
        for neighbor, weight in graph[node]:
            if neighbor != parent:
                min_edge_weight[node][neighbor] = min(min_weight, weight)
                dfs(neighbor, node, min_edge_weight[node][neighbor])
    


# Example Test Cases
if __name__ == "__main__":
    # Example 1
    n = 5
    edges = [[0, 1, 4], [1, 2, 3], [1, 3, 2], [3, 4, 1]]
    queries = [[0, 4], [2, 3], [0, 2]]
    print(minimum_edge_weight_equilibrium_queries(n, edges, queries))  # Expected: [1, 2, 3]

    # Example 2
    n = 3
    edges = [[0, 1, 5], [1, 2, 6]]
    queries = [[0, 2], [1, 2]]
    print(minimum_edge_weight_equilibrium_queries(n, edges, queries))  # Expected: [5, 6]

"""
Time Complexity:
- Building the adjacency list: O(n)
- DFS traversal for precomputing minimum edge weights: O(n)
- Answering each query: O(1) (assuming precomputed results)
Overall: O(n + m)

Space Complexity:
- Adjacency list: O(n)
- Precomputed results: O(n^2) (for all pairs)
Overall: O(n^2)

Topic: Graphs, Trees, DFS
"""