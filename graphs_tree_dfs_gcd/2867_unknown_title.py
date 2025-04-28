"""
LeetCode Problem #2867: Count Valid Paths in a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n-1` and exactly `n-1` edges. The tree is represented as an array `edges` of length `n-1`, where `edges[i] = [ui, vi]` indicates that there is an undirected edge between nodes `ui` and `vi`.

A path in the tree is valid if it satisfies the following conditions:
1. The path starts and ends at different nodes.
2. All nodes in the path are distinct.
3. The greatest common divisor (GCD) of the values of all nodes in the path is equal to 1.

You are also given an array `values` of length `n`, where `values[i]` is the value assigned to the node `i`.

Return the number of valid paths in the tree.

Constraints:
- `1 <= n <= 10^4`
- `1 <= values[i] <= 10^4`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ui, vi <= n - 1`
- `ui != vi`
- `values` are positive integers.

"""

# Python Solution
from math import gcd
from collections import defaultdict, deque

def countValidPaths(n, edges, values):
    def dfs(node, parent):
        # Store the GCDs of all paths ending at this node
        current_gcds = defaultdict(int)
        current_gcds[values[node]] += 1
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            child_gcds = dfs(neighbor, node)
            
            for g in child_gcds:
                new_gcd = gcd(g, values[node])
                current_gcds[new_gcd] += child_gcds[g]
        
        # Count valid paths ending at this node
        nonlocal valid_paths
        valid_paths += current_gcds[1]
        
        return current_gcds
    
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    valid_paths = 0
    dfs(0, -1)
    return valid_paths

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0, 1], [1, 2], [1, 3]]
    values1 = [2, 3, 6, 2]
    print(countValidPaths(n1, edges1, values1))  # Expected Output: 6

    # Test Case 2
    n2 = 3
    edges2 = [[0, 1], [1, 2]]
    values2 = [2, 4, 6]
    print(countValidPaths(n2, edges2, values2))  # Expected Output: 0

    # Test Case 3
    n3 = 5
    edges3 = [[0, 1], [0, 2], [1, 3], [1, 4]]
    values3 = [1, 2, 3, 4, 5]
    print(countValidPaths(n3, edges3, values3))  # Expected Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs a DFS traversal of the tree, which takes O(n) time.
- For each node, we compute GCDs for all paths ending at that node. In the worst case, this involves O(n) operations per node, leading to a total complexity of O(n^2).
- However, optimizations (e.g., pruning paths with GCD > 1 early) can reduce the effective complexity in practice.

Space Complexity:
- The graph representation uses O(n) space.
- The `current_gcds` dictionary at each node can store up to O(n) entries in the worst case, leading to a total space complexity of O(n^2).

Topic: Graphs, Tree, DFS, GCD
"""