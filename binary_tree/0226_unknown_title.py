"""
LeetCode Problem #226: Invert Binary Tree

Problem Statement:
Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Explanation:
The input binary tree is:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

The inverted binary tree is:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    """
    Inverts a binary tree.

    Args:
    root (TreeNode): The root of the binary tree.

    Returns:
    TreeNode: The root of the inverted binary tree.
    """
    if not root:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree level by level."""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # Example 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original Tree:", print_tree(root))
    inverted_root = invertTree(root)
    print("Inverted Tree:", print_tree(inverted_root))

    # Example 2
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print("Original Tree:", print_tree(root))
    inverted_root = invertTree(root)
    print("Inverted Tree:", print_tree(inverted_root))

    # Example 3
    root = None
    print("Original Tree:", print_tree(root))
    inverted_root = invertTree(root)
    print("Inverted Tree:", print_tree(inverted_root))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity depends on the recursion stack.
- In the worst case (a completely unbalanced tree), the recursion stack can go up to O(n).
- In the best case (a completely balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""