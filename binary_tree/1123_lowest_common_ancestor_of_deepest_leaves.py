"""
LeetCode Question #1123: Lowest Common Ancestor of Deepest Leaves

Problem Statement:
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

The lowest common ancestor is the farthest node from the root that is an ancestor of both of the deepest leaves.

A node is a leaf if it has no children. The depth of a node is the number of edges in the path from the root node to it.

Constraints:
- The number of nodes in the tree will be in the range [1, 1000].
- 0 <= Node.val <= 1000
- The values of the nodes in the tree are unique.

Example 1:
Input: root = [1, 2, 3]
Output: [1]
Explanation: The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.

Example 2:
Input: root = [1, 2, 3, 4]
Output: [4]
Explanation: The deepest leaf is the node with value 4, and the lowest common ancestor is itself.

Example 3:
Input: root = [1, 2, 3, 4, 5]
Output: [2]
Explanation: The deepest leaves are the nodes with values 4 and 5.
The lowest common ancestor of these leaves is the node with value 2.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to calculate depth and LCA simultaneously
        def dfs(node):
            if not node:
                return 0, None  # Depth, LCA
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            else:
                return left_depth + 1, node
        
        # Start DFS from the root
        return dfs(root)[1]

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
    print(Solution().lcaDeepestLeaves(root1).val)  # Output: 1

    # Test Case 2
    root2 = build_tree([1, 2, 3, 4])
    print(Solution().lcaDeepestLeaves(root2).val)  # Output: 4

    # Test Case 3
    root3 = build_tree([1, 2, 3, 4, 5])
    print(Solution().lcaDeepestLeaves(root3).val)  # Output: 2

"""
Time Complexity:
- The solution performs a single DFS traversal of the tree.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.

Topic: Binary Tree
"""