"""
LeetCode Question #101: Symmetric Tree

Problem Statement:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Helper function to check symmetry between two subtrees
        def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and 
                    is_mirror(t1.left, t2.right) and 
                    is_mirror(t1.right, t2.left))
        
        # Start the recursion with the left and right subtrees of the root
        return is_mirror(root.left, root.right)

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
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(Solution().isSymmetric(root1))  # Output: True

    # Test Case 2
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(Solution().isSymmetric(root2))  # Output: False

    # Test Case 3
    root3 = build_tree([1])
    print(Solution().isSymmetric(root3))  # Output: True

    # Test Case 4
    root4 = build_tree([1, 2, 2, None, None, None, None])
    print(Solution().isSymmetric(root4))  # Output: True

"""
Time Complexity Analysis:
- The helper function `is_mirror` is called recursively for each node in the tree.
- In the worst case, we visit all nodes once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack. In the worst case (a completely unbalanced tree), the recursion stack can go as deep as the height of the tree, which is O(h), where h is the height of the tree.
- For a balanced tree, the height is O(log n), so the space complexity is O(log n) in this case.

Topic: Binary Tree
"""