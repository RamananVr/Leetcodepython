"""
LeetCode Problem #1782: Count Pairs of Nodes

Problem Statement:
You are given an undirected graph represented by an integer `n`, the number of nodes, and an array `edges`, 
where `edges[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi`. 
You are also given an integer array `queries`.

The answer to the j-th query is the number of pairs of nodes `(a, b)` such that:
1. `1 <= a < b <= n`
2. The sum of the degrees of `a` and `b` is greater than `queries[j]`.

Return an array `answers` such that `answers[j]` is the answer to the j-th query.

Constraints:
- `2 <= n <= 2 * 10^4`
- `1 <= edges.length <= 10^5`
- `1 <= ui, vi <= n`
- `ui != vi`
- `1 <= queries.length <= 20`
- `0 <= queries[j] < 2 * 10^5`
"""

from collections import Counter
from itertools import combinations

def countPairs(n, edges, queries):
    # Step 1: Calculate the degree of each node
    degree = [0] * (n + 1)
    shared_edges = Counter()
    
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        shared_edges[(min(u, v), max(u, v))] += 1

    # Step 2: Sort degrees for efficient counting
    sorted_degree = sorted(degree[1:])
    result = []

    for q in queries:
        total_pairs = 0
        j = n - 1

        # Two-pointer approach to count pairs with degree sum > q
        for i in range(n):
            while j > i and sorted_degree[i] + sorted_degree[j] > q:
                j -= 1
            total_pairs += n - 1 - j

        # Remove double counting
        total_pairs -= sum(sorted_degree[i] *