"""
LeetCode Question #298: Binary Tree Longest Consecutive Sequence

Problem Statement:
Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is defined as a path where the values of the nodes along the path are incrementing by 1. 
This path can be either from parent to child or from any ancestor to descendant, but it must be downward (parent to child).

Example 1:
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive sequence is [1,2] or [2,3].

Example 2:
Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: The longest consecutive sequence is [2,3].

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node, parent_val, length):
            if not node:
                return length
            # Check if the current node is consecutive
            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1
            # Recur for left and right children
            left_length = dfs(node.left, node.val, length)
            right_length = dfs(node.right, node.val, length)
            # Return the maximum length found
            return max(length, left_length, right_length)
        
        if not root:
            return 0
        return dfs(root, root.val - 1, 0)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([1, 2, 3])
    print(Solution().longestConsecutive(root1))  # Output: 2

    # Test Case 2
    root2 = build_tree([2, None, 3, 2, None, 1])
    print(Solution().longestConsecutive(root2))  # Output: 2

    # Test Case 3
    root3 = build_tree([1, None, 2, None, 3, None, 4])
    print(Solution().longestConsecutive(root3))  # Output: 4

    # Test Case 4
    root4 = build_tree([10, 5, 11, None, 6, None, 12])
    print(Solution().longestConsecutive(root4))  # Output: 2

"""
Time Complexity:
- Each node is visited once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.

Topic: Binary Tree
"""