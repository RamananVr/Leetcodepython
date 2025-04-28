"""
LeetCode Problem #2872: Maximum Number of K-Divisible Components

Problem Statement:
You are given a tree (an undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1`, and an array `values` of length `n` where `values[i]` is the value of the `i-th` node. You are also given a 2D array `edges` where `edges[i] = [u, v]` indicates that there is an undirected edge between nodes `u` and `v`.

A component of the tree is k-divisible if the sum of the values of all nodes in the component is divisible by `k`.

Your task is to determine the maximum number of k-divisible components that the tree can be split into by removing some edges.

Return the maximum number of k-divisible components.

Constraints:
- `1 <= n <= 10^5`
- `values.length == n`
- `1 <= values[i] <= 10^9`
- `edges.length == n - 1`
- `0 <= u, v < n`
- `1 <= k <= 10^9`
"""

from collections import defaultdict
from typing import List

def maxKDivisibleComponents(values: List[int], edges: List[List[int]], k: int) -> int:
    """
    Function to calculate the maximum number of k-divisible components in the tree.
    """
    # Build the adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize variables
    result = 0

    def dfs(node: int, parent: int) -> int:
        """
        Perform a DFS to calculate the sum of values in each subtree.
        """
        nonlocal result
        subtree_sum = values[node]
        
        for neighbor in graph[node]:
            if neighbor != parent:
                child_sum = dfs(neighbor, node)
                subtree_sum += child_sum
        
        # If the subtree sum is divisible by k, we can form a k-divisible component
        if subtree_sum % k == 0:
            result += 1
            return 0  # Reset the sum for this component
        
        return subtree_sum

    # Start DFS from node 0 (assuming the tree is connected)
    dfs(0, -1)
    
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    values = [1, 2, 3, 4]
    edges = [[0, 1], [1, 2], [1, 3]]
    k = 3
    print(maxKDivisibleComponents(values, edges, k))  # Output: 2

    # Test Case 2
    values = [2, 2, 2, 2]
    edges = [[0, 1], [1, 2], [2, 3]]
    k = 4
    print(maxKDivisibleComponents(values, edges, k))  # Output: 2

    # Test Case 3
    values = [5, 10, 15]
    edges = [[0, 1], [1, 2]]
    k = 5
    print(maxKDivisibleComponents(values, edges, k))  # Output: 3


"""
Time Complexity:
- Building the adjacency list takes O(n) since there are n-1 edges.
- The DFS traversal visits each node and edge once, so it takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The recursion stack in the DFS can go as deep as O(n) in the worst case.
- Overall space complexity: O(n).

Topic: Graphs, Tree, DFS
"""