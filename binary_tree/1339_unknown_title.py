"""
LeetCode Problem #1339: Maximum Product of Splitted Binary Tree

Problem Statement:
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 10^9 + 7.

Note:
- The tree is rooted and has no duplicate values.
- Each node's value is a positive integer.

Constraints:
- The number of nodes in the tree is in the range [2, 5 * 10^4].
- 1 <= Node.val <= 10^4
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Calculate the total sum of the tree
        def calculate_total_sum(node):
            if not node:
                return 0
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)
        
        total_sum = calculate_total_sum(root)
        
        # Step 2: Find the maximum product by exploring all possible splits
        self.max_product = 0
        
        def find_max_product(node):
            if not node:
                return 0
            # Calculate the sum of the current subtree
            subtree_sum = node.val + find_max_product(node.left) + find_max_product(node.right)
            # Calculate the product of the current split
            product = subtree_sum * (total_sum - subtree_sum)
            # Update the maximum product
            self.max_product = max(self.max_product, product)
            return subtree_sum
        
        find_max_product(root)
        
        return self.max_product % MOD

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(Solution().maxProduct(root1))  # Output: 110

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    print(Solution().maxProduct(root2))  # Output: 1

"""
Time Complexity:
- Calculating the total sum of the tree takes O(n), where n is the number of nodes in the tree.
- Finding the maximum product also takes O(n), as we traverse the tree again.
- Overall time complexity: O(n).

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive stack.

Topic: Binary Tree
"""