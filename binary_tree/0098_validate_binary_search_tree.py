"""
LeetCode Question #98: Validate Binary Search Tree

Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # Check the current node's value against the allowed range
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(Solution().isValidBST(root1))  # Output: True

    # Test Case 2: Invalid BST (left child is greater than the root)
    root2 = TreeNode(5)
    root2.left = TreeNode(6)
    root2.right = TreeNode(7)
    print(Solution().isValidBST(root2))  # Output: False

    # Test Case 3: Invalid BST (right child is less than the root)
    root3 = TreeNode(10)
    root3.left = TreeNode(5)
    root3.right = TreeNode(8)
    print(Solution().isValidBST(root3))  # Output: False

    # Test Case 4: Single node tree (always valid)
    root4 = TreeNode(1)
    print(Solution().isValidBST(root4))  # Output: True

    # Test Case 5: Larger valid BST
    root5 = TreeNode(10)
    root5.left = TreeNode(5)
    root5.right = TreeNode(15)
    root5.left.left = TreeNode(3)
    root5.left.right = TreeNode(7)
    root5.right.left = TreeNode(12)
    root5.right.right = TreeNode(18)
    print(Solution().isValidBST(root5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the tree is visited exactly once, so the time complexity is O(n), 
  where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the 
  recursive call stack. In the worst case (a completely unbalanced tree), h = n, 
  so the space complexity is O(n). In the best case (a balanced tree), h = log(n), 
  so the space complexity is O(log(n)).

Topic: Binary Tree
"""