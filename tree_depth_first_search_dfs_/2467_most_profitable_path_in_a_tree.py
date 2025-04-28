"""
LeetCode Question #2467: Most Profitable Path in a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. The root of the tree is node `0`, and each node has a value associated with it, representing the profit you can collect if you visit that node.

You are also given an array `edges` where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i`, and an array `amount` where `amount[i]` is the profit associated with node `i`.

You are tasked to find the most profitable path in the tree from the root node `0` to any leaf node. A leaf node is a node that has no children other than its parent.

Return the maximum profit you can collect on such a path.

Constraints:
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= u_i, v_i < n`
- `amount.length == n`
- `-10^4 <= amount[i] <= 10^4`

"""

from collections import defaultdict, deque

def mostProfitablePath(edges, amount):
    """
    Finds the most profitable path in a tree from the root node to any leaf node.

    :param edges: List[List[int]] - List of edges in the tree.
    :param amount: List[int] - List of profits associated with each node.
    :return: int - Maximum profit that can be collected.
    """
    # Step 1: Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: Perform a DFS to calculate the maximum profit
    def dfs(node, parent):
        max_profit = float('-inf')
        is_leaf = True
        for neighbor in tree[node]:
            if neighbor != parent:
                is_leaf = False
                max_profit = max(max_profit, dfs(neighbor, node))
        return amount[node] + (max_profit if not is_leaf else 0)

    # Start DFS from the root node (0)
    return dfs(0, -1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[0, 1], [1, 2], [1, 3]]
    amount1 = [3, 2, 1, 4]
    print(mostProfitablePath(edges1, amount1))  # Output: 9 (Path: 0 -> 1 -> 3)

    # Test Case 2
    edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]
    amount2 = [5, 3, 6, 2, 1, 4]
    print(mostProfitablePath(edges2, amount2))  # Output: 14 (Path: 0 -> 2 -> 5)

    # Test Case 3
    edges3 = [[0, 1], [1, 2], [1, 3], [3, 4]]
    amount3 = [1, 2, 3, 4, 5]
    print(mostProfitablePath(edges3, amount3))  # Output: 12 (Path: 0 -> 1 -> 3 -> 4)

"""
Time Complexity:
- Building the adjacency list takes O(n) time, where n is the number of nodes.
- The DFS traversal visits each node once, so it also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The recursion stack in the DFS can go as deep as the height of the tree, which is O(n) in the worst case for a skewed tree.
- Overall space complexity: O(n).

Topic: Tree, Depth-First Search (DFS)
"""