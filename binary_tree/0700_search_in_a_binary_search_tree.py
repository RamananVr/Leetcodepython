"""
LeetCode Question #700: Search in a Binary Search Tree

Problem Statement:
You are given the root of a binary search tree (BST) and an integer `val`.
Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node.
If such a node does not exist, return `None`.

A binary search tree is a binary tree where for every node:
- The left subtree of the node contains only nodes with values less than the node's value.
- The right subtree of the node contains only nodes with values greater than the node's value.

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a valid binary search tree.
- 1 <= val <= 10^7
"""

# Python Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Search for a node with the given value in a binary search tree.

        :param root: TreeNode, the root of the binary search tree
        :param val: int, the value to search for
        :return: TreeNode, the subtree rooted at the node with the given value, or None if not found
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Example Test Cases
def test_searchBST():
    # Example 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    val = 2
    result = Solution().searchBST(root, val)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3

    # Example 2
    val = 5
    result = Solution().searchBST(root, val)
    assert result is None

    # Example 3
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    val = 10
    result = Solution().searchBST(root, val)
    assert result.val == 10
    assert result.right.val == 14

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- In the worst case, we traverse the height of the tree. For a balanced binary search tree, the height is O(log n),
  where n is the number of nodes. In the worst case (completely unbalanced tree), the height is O(n).
- Therefore, the time complexity is O(h), where h is the height of the tree.

Space Complexity:
- The space complexity is O(h) due to the recursive call stack, where h is the height of the tree.
- In the worst case (completely unbalanced tree), the space complexity is O(n).
- In the best case (balanced tree), the space complexity is O(log n).
"""

# Topic: Binary Tree

if __name__ == "__main__":
    test_searchBST()