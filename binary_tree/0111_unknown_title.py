"""
LeetCode Problem #111: Minimum Depth of Binary Tree

Problem Statement:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    """
    Function to calculate the minimum depth of a binary tree.
    """
    if not root:
        return 0

    # Use a queue for BFS
    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # If we encounter a leaf node, return its depth
        if not node.left and not node.right:
            return depth

        # Add children to the queue with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(minDepth(root1))  # Output: 2

    # Example 2
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    print(minDepth(root2))  # Output: 5

    # Example 3: Empty tree
    root3 = None
    print(minDepth(root3))  # Output: 0

    # Example 4: Single node tree
    root4 = TreeNode(1)
    print(minDepth(root4))  # Output: 1

"""
Time Complexity:
- Each node is visited once in the BFS traversal, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(n) in the worst case, which occurs when the tree is completely unbalanced (e.g., a linked list).
  In the best case (a balanced tree), the space complexity is O(log n) due to the height of the tree.

Topic: Binary Tree
"""