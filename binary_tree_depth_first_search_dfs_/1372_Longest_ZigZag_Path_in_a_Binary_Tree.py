"""
LeetCode Problem #1372: Longest ZigZag Path in a Binary Tree

Problem Statement:
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follows:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you cannot move in the tree.

The ZigZag length of a path is the number of edges in the path.

Return the longest ZigZag path contained in that tree.

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node, direction, length):
            if not node:
                return
            # Update the maximum ZigZag length
            self.max_length = max(self.max_length, length)
            if direction == "left":
                # If the current direction is left, go left and reset length, or go right and increment length
                dfs(node.left, "left", 1)
                dfs(node.right, "right", length + 1)
            elif direction == "right":
                # If the current direction is right, go right and reset length, or go left and increment length
                dfs(node.right, "right", 1)
                dfs(node.left, "left", length + 1)

        # Start DFS from the root node in both directions
        dfs(root, "left", 0)
        dfs(root, "right", 0)

        return self.max_length

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(1)
    root1.right.left.right = TreeNode(1)
    root1.right.left.right.right = TreeNode(1)
    root1.right.left.right.right.right = TreeNode(1)
    print(Solution().longestZigZag(root1))  # Output: 3

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.left.right = TreeNode(1)
    root2.left.right.left = TreeNode(1)
    root2.left.right.left.right = TreeNode(1)
    print(Solution().longestZigZag(root2))  # Output: 4

    # Example 3
    root3 = TreeNode(1)
    print(Solution().longestZigZag(root3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack during the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(h), where h is the height of the tree.
- In the average case (for a balanced tree), the recursion stack will be O(log n).

Primary Topic: Binary Tree, Depth-First Search (DFS)
"""