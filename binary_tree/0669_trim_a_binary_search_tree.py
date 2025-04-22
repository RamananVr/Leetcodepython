"""
LeetCode Question #669: Trim a Binary Search Tree

Problem Statement:
Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lie in [low, high]. Trimming the tree should not change 
the relative structure of the elements that will remain in the tree (i.e., any node's descendant 
should remain a descendant). It can be guaranteed that the given tree is a binary search tree.

Return the root of the trimmed binary search tree. Note that the root may change depending on 
the given bounds.

Constraints:
- The number of nodes in the tree in the range [1, 10^4].
- 0 <= Node.val <= 10^4
- The value of each node in the tree is unique.
- root is guaranteed to be a valid binary search tree.
- 0 <= low <= high <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    """
    Trims the binary search tree so that all its elements lie in the range [low, high].
    """
    if not root:
        return None

    # If the current node's value is less than low, trim the left subtree
    if root.val < low:
        return trimBST(root.right, low, high)

    # If the current node's value is greater than high, trim the right subtree
    if root.val > high:
        return trimBST(root.left, low, high)

    # Otherwise, recursively trim both subtrees
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    return root

# Example Test Cases
def print_inorder(root):
    """Helper function to print the tree in inorder traversal."""
    if not root:
        return []
    return print_inorder(root.left) + [root.val] + print_inorder(root.right)

if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(0)
    root1.right = TreeNode(2)
    low1, high1 = 1, 2
    trimmed1 = trimBST(root1, low1, high1)
    print("Example 1:", print_inorder(trimmed1))  # Output: [1, 2]

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(0)
    root2.right = TreeNode(4)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(1)
    low2, high2 = 1, 3
    trimmed2 = trimBST(root2, low2, high2)
    print("Example 2:", print_inorder(trimmed2))  # Output: [1, 2, 3]

    # Example 3
    root3 = TreeNode(1)
    low3, high3 = 1, 2
    trimmed3 = trimBST(root3, low3, high3)
    print("Example 3:", print_inorder(trimmed3))  # Output: [1]

"""
Time Complexity:
- Each node in the tree is visited once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack.

Topic: Binary Tree
"""