"""
LeetCode Question #549: Binary Tree Longest Consecutive Sequence II

Problem Statement:
Given the root of a binary tree, return the length of the longest consecutive sequence path. 
The path refers to any sequence of nodes from some starting node to any node in the tree along 
the parent-child connections. The longest consecutive path needs to be from parent to child 
(cannot be the reverse).

A consecutive sequence is defined as a sequence of numbers where each number is exactly one 
greater or one less than its predecessor.

Example 1:
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].

Example 2:
Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -3 * 10^4 <= Node.val <= 3 * 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        Returns the length of the longest consecutive sequence path in the binary tree.
        """
        self.max_length = 0

        def dfs(node):
            if not node:
                return (0, 0)  # (increasing_length, decreasing_length)

            inc, dec = 1, 1  # Start with the current node as a sequence of length 1

            if node.left:
                left_inc, left_dec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = max(dec, left_dec + 1)
                elif node.val == node.left.val - 1:
                    inc = max(inc, left_inc + 1)

            if node.right:
                right_inc, right_dec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, right_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, right_inc + 1)

            # Update the global maximum length
            self.max_length = max(self.max_length, inc + dec - 1)

            return (inc, dec)

        dfs(root)
        return self.max_length

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
    root2 = build_tree([2, 1, 3])
    print(Solution().longestConsecutive(root2))  # Output: 3

    # Test Case 3
    root3 = build_tree([1, None, 2, None, 3])
    print(Solution().longestConsecutive(root3))  # Output: 3

    # Test Case 4
    root4 = build_tree([3, 2, 4, 1, None, None, 5])
    print(Solution().longestConsecutive(root4))  # Output: 3

"""
Time Complexity:
- Each node in the binary tree is visited once, so the time complexity is O(n), 
  where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the 
  recursive call stack.

Topic: Binary Tree
"""