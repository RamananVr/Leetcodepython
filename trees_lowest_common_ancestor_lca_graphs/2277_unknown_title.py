"""
LeetCode Problem #2277: Closest Node to Path in Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n-1` and exactly `n-1` edges. The root of the tree is node `0`.

Each node has a value associated with it, and you are given an array `values` where `values[i]` is the value of the `i-th` node.

You are also given a list of queries, where each query is represented as a tuple `(u, v, x)`. For each query:
- Find the path from node `u` to node `v` in the tree.
- Return the node on this path whose value is closest to `x`. If there are multiple such nodes, return the smallest node index.

Return an array of integers where the `i-th` integer is the answer to the `i-th` query.

Constraints:
- `1 <= n <= 10^5`
- `values.length == n`
- `0 <= values[i] <= 10^9`
- `1 <= queries.length <= 10^5`
- `0 <= u, v < n`
- `0 <= x <= 10^9`

---

Solution:
"""

from collections import defaultdict, deque
import bisect

def closestNodeToPath(n, edges, values, queries):
    # Step 1: Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: Precompute parent and depth using BFS
    parent = [-1] * n
    depth = [0] * n
    def bfs():
        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    queue.append(neighbor)
    bfs()

    # Step 3: Precompute LCA using Binary Lifting
    LOG = 17  # log2(10^5) is approximately 17
    up = [[-1] * LOG for _ in range(n)]
    for i in range(n):
        up[i][0] = parent[i]
    for j in range(1, LOG):
        for i in range(n):
            if up[i][j - 1] != -1:
                up[i][j] = up[up[i][j - 1]][j - 1]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if diff & (1 << i):
                u = up[u][i]
        if u == v:
            return u
        for i in range(LOG - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return parent[u]

    # Step 4: Answer each query
    def get_path(u, v):
        common_ancestor = lca(u, v)
        path = []
        while u != common_ancestor:
            path.append(u)
            u = parent[u]
        path.append(common_ancestor)
        temp = []
        while v != common_ancestor:
            temp.append(v)
            v = parent[v]
        path.extend(reversed(temp))
        return path

    result = []
    for u, v, x in queries:
        path = get_path(u, v)
        closest_node = -1
        closest_diff = float('inf')
        for node in path:
            diff = abs(values[node] - x)
            if diff < closest_diff or (diff == closest_diff and node < closest_node):
                closest_diff = diff
                closest_node = node
        result.append(closest_node)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
    values = [1, 3, 2, 4, 5]
    queries = [(3, 4, 3), (2, 4, 1)]
    print(closestNodeToPath(n, edges, values, queries))  # Output: [3, 2]

    # Example 2
    n = 3
    edges = [[0, 1], [1, 2]]
    values = [10, 20, 30]
    queries = [(0, 2, 25), (1, 2, 15)]
    print(closestNodeToPath(n, edges, values, queries))  # Output: [2, 1]

"""
Time Complexity:
- Precomputing parent, depth, and LCA: O(n * log(n))
- Answering each query: O(q * p), where p is the average path length.
  In the worst case, p = O(n), so the total complexity is O(q * n).
- Overall: O(n * log(n) + q * n)

Space Complexity:
- Tree representation: O(n)
- Parent, depth, and LCA tables: O(n * log(n))
- Path storage for each query: O(p), where p is the average path length.
- Overall: O(n * log(n))

Topic: Trees, Lowest Common Ancestor (LCA), Graphs
"""