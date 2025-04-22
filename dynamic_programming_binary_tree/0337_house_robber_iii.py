"""
LeetCode Question #337: House Robber III

Problem Statement:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in 
this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on 
the same night.

Given the `root` of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4
"""

# Solution
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Base case: if the node is None, return (0, 0)
            if not node:
                return (0, 0)
            
            # Recursively calculate for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            rob_current = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose to rob or not rob its children
            skip_current = max(left) + max(right)
            
            # Return the tuple (rob_current, skip_current)
            return (rob_current, skip_current)
        
        # Start DFS from the root and return the maximum of robbing or skipping the root
        return max(dfs(root))

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(1)
    print(Solution().rob(root1))  # Output: 7

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(1)
    print(Solution().rob(root2))  # Output: 9

    # Example 3
    root3 = TreeNode(3)
    print(Solution().rob(root3))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack used during DFS.
- In the worst case (a skewed tree), the recursion stack can go up to O(n).
- In the best case (a balanced tree), the recursion stack depth is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Dynamic Programming, Binary Tree
"""