"""
LeetCode Problem #1373: Maximum Sum BST in Binary Tree

Problem Statement:
Given a binary tree root, the task is to return the maximum sum of all keys of any subtree which is a Binary Search Tree (BST).

A Binary Search Tree (BST) is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

If no subtree is a BST, return 0.

Constraints:
- The number of nodes in the tree is in the range [1, 4 * 10^4].
- -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        """
        Returns the maximum sum of all keys of any subtree which is a Binary Search Tree (BST).
        """
        self.max_sum = 0

        def dfs(node):
            # Base case: if the node is None, return a valid BST with sum 0
            if not node:
                return (True, float('inf'), float('-inf'), 0)

            # Recursively check left and right subtrees
            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)

            # Check if the current subtree is a BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                # Current subtree is a BST
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                return (True, min(left_min, node.val), max(right_max, node.val), current_sum)
            else:
                # Current subtree is not a BST
                return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6])
    print(Solution().maxSumBST(root1))  # Output: 20

    # Test Case 2
    root2 = build_tree([4, 3, None, 1, 2])
    print(Solution().maxSumBST(root2))  # Output: 2

    # Test Case 3
    root3 = build_tree([-4, -2, -5])
    print(Solution().maxSumBST(root3))  # Output: 0

    # Test Case 4
    root4 = build_tree([5, 4, 8, 3, None, 6, 3])
    print(Solution().maxSumBST(root4))  # Output: 7

"""
Time Complexity Analysis:
- Each node in the tree is visited exactly once during the DFS traversal.
- At each node, we perform constant-time operations to check BST conditions and calculate sums.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack, which can go as deep as the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(n).
- In the best case (balanced tree), the height of the tree is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree, Depth-First Search (DFS)
"""