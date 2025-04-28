"""
LeetCode Problem #979: Distribute Coins in Binary Tree

Problem Statement:
You are given the root of a binary tree with `N` nodes, where each node in the tree has `node.val` coins. 
There are `N` coins in total across all nodes, and the goal is to distribute the coins such that every node 
has exactly one coin. You can move a coin from one node to its parent, or from a parent to one of its children. 
The number of moves is defined as the number of coin transfers you make.

Return the minimum number of moves required to achieve this distribution.

Constraints:
- The number of nodes in the tree is `N`.
- 1 <= N <= 1000
- 0 <= node.val <= 1000
- The sum of all `node.val` is equal to `N`.

Example:
Input: [3, 0, 0]
Output: 2
Explanation: From the root of the tree, you move one coin to its left child and one coin to its right child.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            
            # Recursively calculate excess coins for left and right subtrees
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # Update the total moves required
            self.moves += abs(left_excess) + abs(right_excess)
            
            # Return the excess coins for the current node
            return node.val - 1 + left_excess + right_excess

        dfs(root)
        return self.moves

# Example Test Cases
def test_distribute_coins():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                if 2 * i + 1 < len(nodes):
                    node.left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    node.right = nodes[2 * i + 2]
        return nodes[0]

    # Test Case 1
    root1 = build_tree([3, 0, 0])
    assert Solution().distributeCoins(root1) == 2

    # Test Case 2
    root2 = build_tree([0, 3, 0])
    assert Solution().distributeCoins(root2) == 3

    # Test Case 3
    root3 = build_tree([1, 0, 2])
    assert Solution().distributeCoins(root3) == 2

    # Test Case 4
    root4 = build_tree([0, 0, 0, 4])
    assert Solution().distributeCoins(root4) == 6

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_distribute_coins()

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution performs a single DFS traversal of the binary tree.
- Each node is visited once, so the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(H), where H is the height of the binary tree, due to the recursive call stack.
- In the worst case (skewed tree), H can be equal to N, so the space complexity is O(N).
- In the best case (balanced tree), H is log(N), so the space complexity is O(log(N)).

Topic: Binary Tree
"""