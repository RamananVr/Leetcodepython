"""
LeetCode Problem #2646: Minimize the Total Price of the Trips

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. Each node has a price associated with it, given in the array `price`, where `price[i]` is the price of the `i-th` node.

The tree is represented by a 2D integer array `edges` of size `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an undirected edge connecting nodes `u_i` and `v_i`.

You are also given a 2D integer array `trips`, where `trips[j] = [start_j, end_j]` indicates that you start at the node `start_j` and travel to the node `end_j` by any path in the tree.

You can choose to halve the price of any node, but at most once. Return the minimum total price of all trips.

Constraints:
- `1 <= n <= 50`
- `1 <= price.length <= n`
- `0 <= price[i] <= 1000`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= u_i, v_i <= n - 1`
- `trips.length >= 1`
- `trips[j].length == 2`
- `0 <= start_j, end_j <= n - 1`

"""

from collections import defaultdict, Counter
from functools import lru_cache

def minimumTotalPrice(n, edges, price, trips):
    # Build the adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Count the frequency of visits for each node
    freq = Counter()

    def dfs_path_count(node, target, parent):
        if node == target:
            freq[node] += 1
            return True
        for neighbor in graph[node]:
            if neighbor != parent and dfs_path_count(neighbor, target, node):
                freq[node] += 1
                return True
        return False

    for start, end in trips:
        dfs_path_count(start, end, -1)

    # Dynamic programming to minimize the total price
    @lru_cache(None)
    def dfs(node, parent, halved):
        total = 0
        for neighbor in graph[node]:
            if neighbor != parent:
                total += min(
                    dfs(neighbor, node, False),  # Do not halve the neighbor
                    dfs(neighbor, node, True)   # Halve the neighbor
                )
        if halved:
            return total + (price[node] // 2) * freq[node]
        else:
            return total + price[node] * freq[node]

    return min(dfs(0, -1, False), dfs(0, -1, True))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0, 1], [1, 2], [1, 3]]
    price1 = [2, 2, 10, 6]
    trips1 = [[0, 3], [2, 1], [2, 3]]
    print(minimumTotalPrice(n1, edges1, price1, trips1))  # Expected Output: 23

    # Test Case 2
    n2 = 2
    edges2 = [[0, 1]]
    price2 = [2, 2]
    trips2 = [[0, 0]]
    print(minimumTotalPrice(n2, edges2, price2, trips2))  # Expected Output: 1

    # Test Case 3
    n3 = 3
    edges3 = [[0, 1], [1, 2]]
    price3 = [5, 3, 4]
    trips3 = [[0, 2], [2, 0]]
    print(minimumTotalPrice(n3, edges3, price3, trips3))  # Expected Output: 12


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Building the adjacency list: O(n)
   - Counting the frequency of visits using DFS: O(n * t), where `t` is the number of trips.
   - Dynamic programming with memoization: O(n) since each node is visited once for each state (halved or not halved).
   - Overall: O(n * t)

2. Space Complexity:
   - Adjacency list: O(n)
   - Frequency counter: O(n)
   - Memoization cache: O(n)
   - Call stack for DFS: O(n)
   - Overall: O(n)

Topic: Dynamic Programming, Tree, Graph
"""