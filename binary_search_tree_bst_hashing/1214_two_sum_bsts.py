"""
LeetCode Question #1214: Two Sum BSTs

Problem Statement:
Given two binary search trees, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example:
Input: 
    Tree 1: [2, 1, 4]
    Tree 2: [1, 0, 3]
    Target: 5
Output: true
Explanation: 2 (from Tree 1) + 3 (from Tree 2) = 5

Constraints:
- Each tree has at most 5000 nodes.
- -10^9 <= Node.val <= 10^9
- -10^9 <= target <= 10^9
"""

# Solution
def twoSumBSTs(root1, root2, target):
    def inorder_traversal(root):
        """Helper function to perform inorder traversal and return a sorted list of node values."""
        if not root:
            return []
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
    
    # Get sorted lists of values from both trees
    values1 = inorder_traversal(root1)
    values2 = inorder_traversal(root2)
    
    # Use a set to store values from the second tree for quick lookup
    values2_set = set(values2)
    
    # Check if there exists a pair of values that sum up to the target
    for val in values1:
        if target - val in values2_set:
            return True
    
    return False

# Example Test Cases
class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_test_cases():
    # Example 1
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    target = 5
    print(twoSumBSTs(root1, root2, target))  # Output: True

    # Example 2
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    target = 10
    print(twoSumBSTs(root1, root2, target))  # Output: False

    # Example 3
    root1 = TreeNode(5, TreeNode(3), TreeNode(7))
    root2 = TreeNode(10, TreeNode(8), TreeNode(12))
    target = 15
    print(twoSumBSTs(root1, root2, target))  # Output: True

example_test_cases()

# Time and Space Complexity Analysis
"""
Time Complexity:
- Inorder traversal of each tree takes O(n1) and O(n2), where n1 and n2 are the number of nodes in root1 and root2 respectively.
- Checking for the complement in the set takes O(1) for each value in values1, resulting in O(n1) for the loop.
- Overall time complexity: O(n1 + n2).

Space Complexity:
- The inorder traversal stores all node values in lists, which takes O(n1 + n2) space.
- Additionally, the set for values2 takes O(n2) space.
- Overall space complexity: O(n1 + n2).
"""

# Topic: Binary Search Tree (BST), Hashing