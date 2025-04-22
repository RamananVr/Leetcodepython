"""
LeetCode Question #951: Flip Equivalent Binary Trees

Problem Statement:
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

Constraints:
- The number of nodes in each tree is in the range [0, 100].
- Each tree will have unique node values in the range [0, 99].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    """
    Determines if two binary trees are flip equivalent.
    """
    # Base cases
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False

    # Check flip equivalence in both possible configurations
    return (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right)) or \
           (flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a binary tree from a list
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
    root1 = build_tree([1, 2, 3, 4, 5, None, None, None, None, 6, 7])
    root2 = build_tree([1, 3, 2, None, None, 4, 5, None, None, 7, 6])
    print(flipEquiv(root1, root2))  # Expected: True

    # Test Case 2
    root1 = build_tree([1, 2, 3])
    root2 = build_tree([1, 2, 3])
    print(flipEquiv(root1, root2))  # Expected: True

    # Test Case 3
    root1 = build_tree([1, 2, 3])
    root2 = build_tree([1, 3, 2])
    print(flipEquiv(root1, root2))  # Expected: True

    # Test Case 4
    root1 = build_tree([1, 2, 3])
    root2 = build_tree([1, 2, None])
    print(flipEquiv(root1, root2))  # Expected: False

"""
Time Complexity:
- Each node in the tree is visited once, and for each node, we perform a constant amount of work.
- Let n be the total number of nodes in the larger of the two trees. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the depth of the recursion stack is equal to the height of the tree.
- For a balanced binary tree, the height is O(log n). For a skewed tree, the height is O(n).
- Thus, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""