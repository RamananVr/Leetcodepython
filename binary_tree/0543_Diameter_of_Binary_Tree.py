"""
LeetCode Problem #543: Diameter of Binary Tree

Problem Statement:
Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            # Recursively find the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            # Update the diameter if the path through the current node is longer
            self.diameter = max(self.diameter, left_height + right_height)
            # Return the height of the current node
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root1))  # Output: 3

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(Solution().diameterOfBinaryTree(root2))  # Output: 1

    # Example 3
    root3 = TreeNode(1)
    print(Solution().diameterOfBinaryTree(root3))  # Output: 0

    # Example 4
    root4 = None
    print(Solution().diameterOfBinaryTree(root4))  # Output: 0

"""
Time Complexity Analysis:
- The function performs a depth-first search (DFS) traversal of the binary tree.
- Each node is visited exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack used during the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(n).
- In the best case (for a balanced tree), the recursion stack will be O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""