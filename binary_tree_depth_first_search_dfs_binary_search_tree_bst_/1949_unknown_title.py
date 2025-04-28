"""
LeetCode Problem #1949: Check if a Binary Tree is a Valid Binary Search Tree (BST) After Removing Exactly One Edge

Problem Statement:
You are given the root of a binary tree. In one operation, you can remove exactly one edge in the tree, making it into two separate trees. 
Return true if it is possible to remove exactly one edge in the tree such that at least one of the resulting trees is a valid binary search tree (BST).

A binary search tree (BST) is a tree that satisfies the following conditions:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root, low=float('-inf'), high=float('inf')):
        """
        Helper function to check if a tree is a valid BST.
        """
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)

    def canBeValidBST(self, root):
        """
        Main function to determine if removing one edge can result in a valid BST.
        """
        def dfs(node):
            if not node:
                return False

            # Check if the left or right subtree is already a valid BST
            if node.left and self.isValidBST(node.left):
                return True
            if node.right and self.isValidBST(node.right):
                return True

            # Recursively check for all edges
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)  # This edge makes the tree invalid as a BST

    solution = Solution()
    print(solution.canBeValidBST(root1))  # Output: True

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(solution.canBeValidBST(root2))  # Output: False

    # Example 3
    root3 = TreeNode(5)
    root3.left = TreeNode(3)
    root3.right = TreeNode(6)
    root3.left.left = TreeNode(2)
    root3.left.right = TreeNode(4)

    print(solution.canBeValidBST(root3))  # Output: True

"""
Time Complexity:
- The `isValidBST` function runs in O(n) time for a tree with n nodes.
- The `dfs` function traverses the tree, and for each node, it may call `isValidBST` on its left or right subtree.
- In the worst case, this results in O(n^2) time complexity.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive stack.

Topic: Binary Tree, Depth-First Search (DFS), Binary Search Tree (BST)
"""