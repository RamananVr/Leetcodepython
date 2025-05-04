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
        # Two-pointer approach to count pairs with sum > q
        left, right = 0, n - 1
        while left < right:
            if sorted_degree[left] + sorted_degree[right] > q:
                total_pairs += (right - left)
                right -= 1
            else:
                left += 1

        # Adjust for shared edges
        for (u, v), shared in shared_edges.items():
            if degree[u] + degree[v] > q and degree[u] + degree[v] - shared <= q:
                total_pairs -= 1

        result.append(total_pairs)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    edges1 = [[1, 2], [1, 3], [3, 4], [4, 5], [3, 5]]
    queries1 = [1, 2, 3]
    print(countPairs(n1, edges1, queries1))  # Expected Output: [10, 9, 6]

    # Test Case 2
    n2 = 4
    edges2 = [[1, 2], [2, 3], [4, 1], [2, 4]]
    queries2 = [2, 3]
    print(countPairs(n2, edges2, queries2))  # Expected Output: [4, 2]

"""
Time Complexity Analysis:
1. Calculating the degree of each node: O(edges.length)
2. Sorting the degrees: O(n log n)
3. Two-pointer approach for each query: O(n) per query
4. Adjusting for shared edges: O(edges.length)
Overall: O(edges.length + n log n + queries.length * n)

Space Complexity Analysis:
1. Degree array: O(n)
2. Shared edges counter: O(edges.length)
Overall: O(n + edges.length)

Topic: Graphs
"""