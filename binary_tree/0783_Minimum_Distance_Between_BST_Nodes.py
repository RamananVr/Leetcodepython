"""
LeetCode Problem #783: Minimum Distance Between BST Nodes

Problem Statement:
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Note:
- The BST is guaranteed to have at least two nodes.
- The difference between two nodes is defined as the absolute difference between their values.

Constraints:
- The number of nodes in the tree is in the range [2, 100].
- 0 <= Node.val <= 10^5

Example:
Input: root = [4,2,6,1,3]
Output: 1
Explanation: The minimum difference is between the nodes with values 2 and 3.

Input: root = [1,0,48,null,null,12,49]
Output: 1
Explanation: The minimum difference is between the nodes with values 48 and 49.
"""

# Clean, Correct Python Solution
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # In-order traversal of BST gives sorted values
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Get sorted values from the BST
        sorted_values = in_order_traversal(root)
        
        # Compute the minimum difference between consecutive values
        min_diff = float('inf')
        for i in range(1, len(sorted_values)):
            min_diff = min(min_diff, sorted_values[i] - sorted_values[i - 1])
        
        return min_diff

# Example Test Cases
def test_solution():
    sol = Solution()
    
    # Test Case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    assert sol.minDiffInBST(root1) == 1  # Minimum difference is between 2 and 3
    
    # Test Case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(49)
    assert sol.minDiffInBST(root2) == 1  # Minimum difference is between 48 and 49
    
    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- The in-order traversal visits each node exactly once, so the traversal takes O(n), where n is the number of nodes in the BST.
- Computing the minimum difference from the sorted values takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The in-order traversal uses O(n) space to store the sorted values.
- The recursion stack for the traversal takes O(h), where h is the height of the tree. In the worst case (skewed tree), h = n.
- Overall space complexity: O(n).
"""

# Topic: Binary Tree

# Run the test cases
if __name__ == "__main__":
    test_solution()