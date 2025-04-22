"""
LeetCode Question #250: Count Univalue Subtrees

Problem Statement:
Given the root of a binary tree, return the number of uni-value (universal value) subtrees.
A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [5,5,5,5,5,null,5]
Output: 6

Constraints:
- The number of the node in the tree will be in the range [0, 1000].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """
        Counts the number of uni-value subtrees in the binary tree.
        """
        self.count = 0

        def is_unival(node, parent_val):
            if not node:
                return True
            
            # Recursively check left and right subtrees
            left_is_unival = is_unival(node.left, node.val)
            right_is_unival = is_unival(node.right, node.val)
            
            # If both left and right subtrees are unival and match the current node's value
            if left_is_unival and right_is_unival:
                self.count += 1
                return node.val == parent_val
            
            return False

        is_unival(root, None)
        return self.count

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

    solution = Solution()

    # Test Case 1
    root1 = build_tree([5, 1, 5, 5, 5, None, 5])
    print(solution.countUnivalSubtrees(root1))  # Output: 4

    # Test Case 2
    root2 = build_tree([])
    print(solution.countUnivalSubtrees(root2))  # Output: 0

    # Test Case 3
    root3 = build_tree([5, 5, 5, 5, 5, None, 5])
    print(solution.countUnivalSubtrees(root3))  # Output: 6

"""
Time Complexity:
- Each node in the tree is visited exactly once, so the time complexity is O(n), 
  where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.

Topic: Binary Tree
"""