"""
LeetCode Problem #501: Find Mode in Binary Search Tree

Problem Statement:
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently 
occuring element) in the BST. If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Follow up: Could you do that without using any extra space? (Assume the implicit stack space used by recursion does not count).
"""

from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root: Optional[TreeNode]) -> List[int]:
    """
    Finds the mode(s) in a binary search tree.
    """
    if not root:
        return []

    # Dictionary to store frequency of each value
    freq = defaultdict(int)

    # Helper function to perform in-order traversal
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        freq[node.val] += 1
        inorder(node.right)

    # Perform in-order traversal to populate frequency dictionary
    inorder(root)

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Collect all values with the maximum frequency
    modes = [key for key, value in freq.items() if value == max_freq]

    return modes

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(2)
    print(findMode(root1))  # Output: [2]

    # Test Case 2
    root2 = TreeNode(1)
    print(findMode(root2))  # Output: [1]

    # Test Case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.right = TreeNode(2)
    print(findMode(root3))  # Output: [1, 2]

    # Test Case 4
    root4 = TreeNode(1)
    root4.left = TreeNode(1)
    root4.right = TreeNode(1)
    print(findMode(root4))  # Output: [1]

"""
Time Complexity Analysis:
- The in-order traversal visits each node exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.
- Constructing the frequency dictionary and finding the maximum frequency also takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The space complexity is O(h) for the recursion stack, where h is the height of the tree.
- Additionally, the frequency dictionary requires O(k) space, where k is the number of unique values in the tree.
- Overall space complexity: O(h + k).

Topic: Binary Tree
"""