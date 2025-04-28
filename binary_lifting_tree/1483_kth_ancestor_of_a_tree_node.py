"""
LeetCode Question #1483: Kth Ancestor of a Tree Node

Problem Statement:
You are given a tree with `n` nodes numbered from `0` to `n-1` in the form of a parent array `parent` where `parent[i]` is the parent of node `i`. The root node is `0`, so `parent[0] = -1` since it has no parent. You are also given `m` queries, where each query is represented as `(node, k)`.

For each query, you need to return the `k`th ancestor of the given `node`. If there is no such ancestor, return `-1`.

The `k`th ancestor of a node is defined as the node that is `k` steps above it in the tree. For example, if `node = 3` and `k = 1`, the `1`st ancestor of node `3` is its parent. If `k = 2`, the `2`nd ancestor is the parent of its parent, and so on.

Constraints:
- `1 <= n <= 5 * 10^4`
- `1 <= m <= 10^4`
- `0 <= node <= n-1`
- `0 <= k <= n-1`
- `parent[0] == -1` (indicating that node `0` is the root)

Follow-up:
Can you solve the problem efficiently with `O(log(n))` time per query?

---

Solution:
We will use Binary Lifting, a technique that preprocesses the tree to allow efficient computation of ancestors in logarithmic time for each query. The idea is to precompute ancestors at powers of two for each node, enabling us to jump upwards in the tree efficiently.

---

Python Solution:
"""

class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        # Binary lifting table
        self.max_power = 16  # log2(5 * 10^4) < 16
        self.dp = [[-1] * self.max_power for _ in range(n)]
        
        # Initialize the first ancestor (parent)
        for i in range(n):
            self.dp[i][0] = parent[i]
        
        # Precompute ancestors at powers of two
        for j in range(1, self.max_power):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        # Traverse upwards using binary lifting
        for j in range(self.max_power):
            if k & (1 << j):  # Check if the j-th bit in k is set
                node = self.dp[node][j]
                if node == -1:  # No ancestor exists
                    return -1
        return node

"""
Example Test Cases:
"""

if __name__ == "__main__":
    # Example 1
    n = 7
    parent = [-1, 0, 0, 1, 1, 2, 2]
    treeAncestor = TreeAncestor(n, parent)
    print(treeAncestor.getKthAncestor(3, 1))  # Output: 1
    print(treeAncestor.getKthAncestor(5, 2))  # Output: 0
    print(treeAncestor.getKthAncestor(6, 3))  # Output: -1

    # Example 2
    n = 5
    parent = [-1, 0, 0, 1, 1]
    treeAncestor = TreeAncestor(n, parent)
    print(treeAncestor.getKthAncestor(4, 2))  # Output: 0
    print(treeAncestor.getKthAncestor(4, 3))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Preprocessing: O(n * log(n)), where `log(n)` is the number of powers of two we compute for each node.
- Query: O(log(n)) per query, as we traverse upwards using binary lifting.

Space Complexity:
- O(n * log(n)) for the binary lifting table `dp`.

Topic: Binary Lifting, Tree
"""