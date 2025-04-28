"""
LeetCode Problem #2538: Difference Between Maximum and Minimum Price Sum

Problem Statement:
There is a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

Each node has a price. You are given a 0-indexed integer array `price` of length `n` where `price[i]` is the price of the `i-th` node.

The price sum of a given path is the sum of the prices of the nodes lying on that path.

Additionally, you are given a 2D integer array `edges` of size `n - 1` where `edges[i] = [u_i, v_i]` indicates that there is an undirected edge connecting nodes `u_i` and `v_i`.

The difference between the maximum and minimum price sum among all paths in the tree is defined as:
    max_price_sum - min_price_sum

Return the difference between the maximum and minimum price sum among all paths in the tree.

Constraints:
- `1 <= n <= 10^5`
- `price.length == n`
- `1 <= price[i] <= 10^4`
- `edges.length == n - 1`
- `0 <= u_i, v_i <= n - 1`
- `edges` represents a valid tree.

"""

from collections import defaultdict
import sys

def max_min_price_difference(n, price, edges):
    """
    Function to calculate the difference between the maximum and minimum price sum among all paths in the tree.

    :param n: int - Number of nodes in the tree
    :param price: List[int] - Price of each node
    :param edges: List[List[int]] - Edges of the tree
    :return: int - Difference between maximum and minimum price sum
    """
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Initialize variables to store the maximum and minimum price sums
    max_price_sum = -sys.maxsize
    min_price_sum = sys.maxsize

    # Helper function for DFS traversal
    def dfs(node, parent):
        nonlocal max_price_sum, min_price_sum
        # Start with the price of the current node
        current_sum = price[node]

        # Traverse all children
        for neighbor in tree[node]:
            if neighbor != parent:  # Avoid revisiting the parent node
                child_sum = dfs(neighbor, node)
                current_sum += max(0, child_sum)  # Only add positive contributions

        # Update the maximum and minimum price sums
        max_price_sum = max(max_price_sum, current_sum)
        min_price_sum = min(min_price_sum, current_sum)

        return current_sum

    # Start DFS from any node (e.g., node 0)
    dfs(0, -1)

    # Return the difference between the maximum and minimum price sums
    return max_price_sum - min_price_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    price1 = [1, 2, 3, 4]
    edges1 = [[0, 1], [1, 2], [1, 3]]
    print(max_min_price_difference(n1, price1, edges1))  # Expected Output: 9

    # Test Case 2
    n2 = 3
    price2 = [5, 3, 2]
    edges2 = [[0, 1], [1, 2]]
    print(max_min_price_difference(n2, price2, edges2))  # Expected Output: 8

    # Test Case 3
    n3 = 5
    price3 = [10, 20, 30, 40, 50]
    edges3 = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(max_min_price_difference(n3, price3, edges3))  # Expected Output: 140


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n) time since there are n-1 edges.
- The DFS traversal visits each node and edge exactly once, so it also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list requires O(n) space to store the tree structure.
- The recursion stack for DFS can go up to O(n) in the worst case (e.g., a skewed tree).
- Overall space complexity: O(n).

Topic: Tree, Depth-First Search (DFS)
"""