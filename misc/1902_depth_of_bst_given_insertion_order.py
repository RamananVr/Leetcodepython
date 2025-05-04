"""
LeetCode Problem #1902: Depth of BST Given Insertion Order

Problem Statement:
You are given a 0-indexed integer array `order` of length `n` that represents the order in which elements are inserted into a binary search tree (BST). Specifically, `order[i]` is the value being inserted into the BST in step `i`.

You are tasked with finding the depth of the BST after all the elements have been inserted. The depth of a BST is defined as the number of edges in the longest path from the root to any leaf.

Return the depth of the BST.

Constraints:
- 1 <= order.length <= 10^4
- 1 <= order[i] <= 10^4
- All the values of `order` are unique.
"""

# Solution
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepthBST(self, order):
        def insert(node, val):
            if not node:
                return TreeNode(val), 1
            if val < node.val:
                node.left, left_depth = insert(node.left, val)
                return node, max(left_depth + 1, depth)
            else:
                node.right, right_depth = insert(node.right, val)
                return node, max(right_depth + 1, depth)
        depth=