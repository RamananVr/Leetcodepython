"""
LeetCode Question #104: Maximum Depth of Binary Tree

Problem Statement:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """
    Function to calculate the maximum depth of a binary tree.
    :param root: TreeNode, the root of the binary tree
    :return: int, the maximum depth of the binary tree
    """
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(maxDepth(root1))  # Output: 3

    # Example 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(maxDepth(root2))  # Output: 2

    # Example 3: Empty tree
    root3 = None
    print(maxDepth(root3))  # Output: 0

    # Example 4: Single node tree
    root4 = TreeNode(42)
    print(maxDepth(root4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function visits each node of the binary tree exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack.
- In the worst case (when the tree is completely unbalanced), the recursion stack can go up to n levels deep, resulting in O(n) space complexity.
- In the best case (when the tree is completely balanced), the recursion stack depth is log(n), resulting in O(log(n)) space complexity.

Topic: Binary Tree
"""