"""
LeetCode Problem #2236: Root Equals Sum of Children

Problem Statement:
You are given a binary tree that has the following structure:
- The tree consists of exactly three nodes: the root, its left child, and its right child.
- The value of each node is an integer.

Return `True` if the value of the root is equal to the sum of the values of its two children, otherwise return `False`.

Example 1:
Input: root = [10, 4, 6]
Output: True
Explanation: The root node's value is 10, and the sum of its children is 4 + 6 = 10.

Example 2:
Input: root = [5, 3, 1]
Output: False
Explanation: The root node's value is 5, and the sum of its children is 3 + 1 = 4.

Constraints:
- The tree has exactly three nodes: the root, its left child, and its right child.
- The value of each node is an integer in the range [1, 100].

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root: TreeNode) -> bool:
    """
    Function to check if the value of the root node is equal to the sum of its two children.

    :param root: TreeNode, the root of the binary tree
    :return: bool, True if root.val == root.left.val + root.right.val, otherwise False
    """
    return root.val == (root.left.val + root.right.val)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(10, TreeNode(4), TreeNode(6))
    print(checkTree(root1))  # Output: True

    # Test Case 2
    root2 = TreeNode(5, TreeNode(3), TreeNode(1))
    print(checkTree(root2))  # Output: False

    # Test Case 3
    root3 = TreeNode(15, TreeNode(7), TreeNode(8))
    print(checkTree(root3))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a constant amount of work: accessing the values of the root, left child, and right child.
- Therefore, the time complexity is O(1).

Space Complexity:
- The function does not use any additional space apart from the input tree structure.
- Therefore, the space complexity is O(1).

Topic: Binary Tree
"""