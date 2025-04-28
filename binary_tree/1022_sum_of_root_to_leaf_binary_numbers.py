"""
LeetCode Question #1022: Sum of Root To Leaf Binary Numbers

Problem Statement:
You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit. For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

Return the sum of all the numbers represented by root-to-leaf paths in the tree.

A leaf is a node with no children.

Constraints:
- The number of nodes in the tree is in the range `[1, 1000]`.
- `Node.val` is `0` or `1`.

Example:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100 + 101 + 110 = 4 + 5 + 13 = 22)
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_value):
            if not node:
                return 0
            
            # Update the current binary value
            current_value = (current_value << 1) | node.val
            
            # If it's a leaf node, return the current value
            if not node.left and not node.right:
                return current_value
            
            # Recursively calculate the sum for left and right subtrees
            return dfs(node.left, current_value) + dfs(node.right, current_value)
        
        return dfs(root, 0)

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
    root1 = build_tree([1, 0, 1, 0, 1, 0, 1])
    print(Solution().sumRootToLeaf(root1))  # Output: 22

    # Test Case 2
    root2 = build_tree([0, 1, 1])
    print(Solution().sumRootToLeaf(root2))  # Output: 6

    # Test Case 3
    root3 = build_tree([1])
    print(Solution().sumRootToLeaf(root3))  # Output: 1

    # Test Case 4
    root4 = build_tree([1, None, 0, None, 1])
    print(Solution().sumRootToLeaf(root4))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack used during DFS.
- In the worst case, the tree is completely unbalanced (e.g., a linked list), and the recursion stack will contain all n nodes. Thus, the space complexity is O(n).
- In the best case, the tree is balanced, and the height of the tree is log(n). Thus, the space complexity is O(log(n)).

Topic: Binary Tree
"""