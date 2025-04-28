"""
LeetCode Problem #2421: Number of Good Paths

Problem Statement:
There is a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

You are given a 0-indexed integer array `vals` of length `n` where `vals[i]` denotes the value of the `i-th` node. You are also given a 2D integer array `edges` where `edges[i] = [ai, bi]` denotes that there exists an undirected edge connecting nodes `ai` and `bi`.

A good path is a simple path that satisfies the following conditions:
1. The starting node and the ending node have the same value.
2. All nodes between the starting node and the ending node (inclusive) have values less than or equal to the starting node.

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

Constraints:
- `n == vals.length`
- `1 <= n <= 3 * 10^4`
- `0 <= vals[i] <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- `edges` represents a valid tree.
"""

from collections import defaultdict
from itertools import groupby

def numberOfGoodPaths(vals, edges):
    # Helper function for union-find
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            if size[root1] > size[root2]:
                root1, root2 = root2, root1
            parent[root1] = root2
            size[root2] += size[root1]

    n = len(vals)
    parent = list(range(n))
    size = [1] * n
    value_to_nodes = defaultdict(list)

    # Group nodes by their values
    for i, val in enumerate(vals):
        value_to_nodes[val].append(i)

    # Sort edges by the maximum value of the two nodes they connect
    edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))

    good_paths = 0
    for value, nodes in sorted(value_to_nodes.items()):
        # Process all edges where both nodes have values <= current value
        while edges and max(vals[edges[0][0]], vals[edges[0][1]]) <= value:
            u, v = edges.pop(0)
            union(u, v)

        # Count good paths for the current value
        group_count = defaultdict(int)
        for node in nodes:
            root = find(node)
            group_count[root] += 1

        for count in group_count.values():
            good_paths += count * (count + 1) // 2

    return good_paths

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(numberOfGoodPaths(vals, edges))  # Output: 6

    # Test Case 2
    vals = [1, 1, 2, 2, 3]
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(numberOfGoodPaths(vals, edges))  # Output: 7

    # Test Case 3
    vals = [1]
    edges = []
    print(numberOfGoodPaths(vals, edges))  # Output: 1

"""
Time Complexity:
- Sorting the edges: O((n - 1) * log(n - 1)) = O(n log n)
- Sorting the nodes by value: O(n log n)
- Union-Find operations: O(α(n)) per operation, where α is the inverse Ackermann function.
  In the worst case, we perform O(n) union-find operations, so this is O(n α(n)).
Overall: O(n log n)

Space Complexity:
- Union-Find parent and size arrays: O(n)
- Value-to-nodes dictionary: O(n)
- Group count dictionary: O(n)
Overall: O(n)

Topic: Union-Find (Disjoint Set Union), Graphs
"""