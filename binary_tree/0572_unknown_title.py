"""
LeetCode Problem #572: Subtree of Another Tree

Problem Statement:
Given the roots of two binary trees `root` and `subRoot`, return `True` if there is a subtree of `root` with the same structure and node values of `subRoot` and `False` otherwise.

A subtree of a binary tree `root` is a tree that consists of a node in `root` and all of this node's descendants. The tree `root` could also be considered as a subtree of itself.

Constraints:
- The number of nodes in the tree `root` is in the range [1, 2000].
- The number of nodes in the tree `subRoot` is in the range [1, 1000].
- -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Determines if subRoot is a subtree of root.
    """
    if not subRoot:
        return True  # An empty tree is always a subtree
    if not root:
        return False  # A non-empty tree cannot be a subtree of an empty tree

    def isSameTree(s: TreeNode, t: TreeNode) -> bool:
        """
        Helper function to check if two trees are identical.
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

    # Check if the current trees are identical or if subRoot is a subtree of either child
    return isSameTree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    print(isSubtree(root, subRoot))  # Output: True

    # Example 2
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    print(isSubtree(root, subRoot))  # Output: False

    # Example 3
    root = TreeNode(1)
    subRoot = TreeNode(1)
    print(isSubtree(root, subRoot))  # Output: True

"""
Time Complexity:
- Let `n` be the number of nodes in `root` and `m` be the number of nodes in `subRoot`.
- The `isSameTree` function takes O(min(n, m)) time in the worst case.
- In the worst case, we call `isSameTree` for every node in `root`, leading to a time complexity of O(n * m).

Space Complexity:
- The space complexity is O(h), where `h` is the height of the tree `root`, due to the recursion stack.

Topic: Binary Tree
"""