"""
LeetCode Problem #333: Largest BST Subtree

Problem Statement:
Given a binary tree, find the largest subtree that is a Binary Search Tree (BST), 
where the largest means the subtree with the largest number of nodes.

A subtree must include all of its descendants. Here's the definition of a BST:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Return the size of the largest BST subtree in the given binary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root: TreeNode) -> int:
    """
    Function to find the size of the largest BST subtree in a binary tree.
    """
    def helper(node):
        # Base case: An empty node is a valid BST with size 0
        if not node:
            return (True, 0, float('inf'), float('-inf'))  # (isBST, size, minVal, maxVal)

        # Recursively check left and right subtrees
        left_is_bst, left_size, left_min, left_max = helper(node.left)
        right_is_bst, right_size, right_min, right_max = helper(node.right)

        # Check if the current node forms a BST with its left and right subtrees
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            # Current subtree is a BST
            size = left_size + right_size + 1
            return (True, size, min(node.val, left_min), max(node.val, right_max))
        else:
            # Current subtree is not a BST
            return (False, max(left_size, right_size), 0, 0)

    # Start the recursion and return the size of the largest BST
    return helper(root)[1]

# Example Test Cases
if __name__ == "__main__":
    # Example 1:
    # Input: [10, 5, 15, 1, 8, None, 7]
    # Tree structure:
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    1   8     7
    # Output: 3 (The subtree [5, 1, 8] is the largest BST)
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(8)
    root1.right.right = TreeNode(7)
    print(largestBSTSubtree(root1))  # Output: 3

    # Example 2:
    # Input: [4, 2, 7, 2, 3, 5, None]
    # Tree structure:
    #        4
    #       / \
    #      2   7
    #     / \
    #    2   3
    #       /
    #      5
    # Output: 2 (The subtree [2, 3] is the largest BST)
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.left.right.left = TreeNode(5)
    print(largestBSTSubtree(root2))  # Output: 2

    # Example 3:
    # Input: []
    # Output: 0 (Empty tree has no BST)
    root3 = None
    print(largestBSTSubtree(root3))  # Output: 0

"""
Time Complexity:
- Each node in the tree is visited exactly once, and at each node, we perform constant-time operations.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.
- In the worst case (skewed tree), h = n, so the space complexity is O(n).
- In the best case (balanced tree), h = log(n), so the space complexity is O(log(n)).

Topic: Binary Tree
"""