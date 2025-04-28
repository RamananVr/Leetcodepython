"""
LeetCode Problem #1026: Maximum Difference Between Node and Ancestor

Problem Statement:
Given the root of a binary tree, find the maximum value `v` for which there exist different nodes `a` and `b` 
such that `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b`, or any child of `a` is an ancestor of `b`.

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, one of the maximum is |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:
- The number of nodes in the tree is in the range [2, 5000].
- 0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        This function calculates the maximum difference between a node and its ancestor in a binary tree.
        """
        def dfs(node, current_min, current_max):
            if not node:
                return current_max - current_min
            
            # Update the current min and max values
            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)
            
            # Recur for left and right subtrees
            left_diff = dfs(node.left, current_min, current_max)
            right_diff = dfs(node.right, current_min, current_max)
            
            # Return the maximum difference found
            return max(left_diff, right_diff)
        
        # Start DFS with the root node
        return dfs(root, root.val, root.val)

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
    root1 = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    print(Solution().maxAncestorDiff(root1))  # Output: 7

    # Test Case 2
    root2 = build_tree([1, None, 2, None, 0, 3])
    print(Solution().maxAncestorDiff(root2))  # Output: 3

"""
Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack, which depends on the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(n), leading to O(n) space complexity.
- In the best case (balanced tree), the height of the tree is O(log n), leading to O(log n) space complexity.

Topic: Binary Tree
"""