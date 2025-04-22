"""
LeetCode Problem #623: Add One Row to Tree

Problem Statement:
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

- Note that the root node is at depth 1.
- The adding rule is:
  - Given the depth depth, for each not null tree node cur at depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
  - cur's original left subtree should be the left subtree of the new left subtree root.
  - cur's original right subtree should be the right subtree of the new right subtree root.
- If depth == 1, that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- The depth of the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
- -10^5 <= val <= 10^5
- 1 <= depth <= the depth of the tree + 1
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    """
    Adds a row of nodes with value `val` at the given depth `depth`.
    """
    if depth == 1:
        # If depth is 1, create a new root with the original tree as its left child
        return TreeNode(val, left=root)
    
    def dfs(node, current_depth):
        if not node:
            return
        if current_depth == depth - 1:
            # Add new nodes at the required depth
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        else:
            # Continue traversing the tree
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)
    
    dfs(root, 1)
    return root

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree level by level."""
    if not root:
        return "[]"
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            if node:
                level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level.append(None)
        if any(x is not None for x in level):
            result.extend(level)
        queue = next_queue
    return result

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(3), TreeNode(1))
    root.right = TreeNode(6, TreeNode(5))
    val, depth = 1, 2
    new_root = addOneRow(root, val, depth)
    print(print_tree(new_root))  # Expected: [4, 1, 1, 2, None, None, 6, 3, 1, 5]

    # Test Case 2
    root = TreeNode(4)
    val, depth = 1, 1
    new_root = addOneRow(root, val, depth)
    print(print_tree(new_root))  # Expected: [1, 4]

    # Test Case 3
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    val, depth = 5, 4
    new_root = addOneRow(root, val, depth)
    print(print_tree(new_root))  # Expected: [1, 2, 3, 4, None, None, None, 5, None]

"""
Time Complexity:
- The function traverses the tree up to depth `depth - 1`. In the worst case, this involves visiting all nodes in the tree.
- Let `n` be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case (skewed tree), the recursion stack can go up to O(n).
- In a balanced tree, the recursion stack depth is O(log n).
- Thus, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""