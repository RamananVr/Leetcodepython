"""
LeetCode Question #545: Boundary of Binary Tree

Problem Statement:
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from the root. 
The boundary includes the left boundary, leaves, and the right boundary in order without duplicate nodes.

- The left boundary is defined as the path from the root to the left-most node. 
  The right boundary is defined as the path from the root to the right-most node.
- If the root doesn't have a left child, then the left boundary is empty.
- If the root doesn't have a right child, then the right boundary is empty.
- The leaves are defined as all the leaf nodes in the tree. 
  The leaf nodes form the bottom-most boundary of the binary tree.

Note:
- The root is always part of the boundary.
- The order of nodes in the boundary is important.

Example 1:
Input:
    1
     \
      2
     / \
    3   4

Output: [1, 3, 4, 2]

Example 2:
Input:
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8

Output: [1, 2, 4, 7, 8, 6, 3]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        def is_leaf(node):
            return node and not node.left and not node.right

        def add_left_boundary(node, boundary):
            while node:
                if not is_leaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right

        def add_leaves(node, boundary):
            if not node:
                return
            if is_leaf(node):
                boundary.append(node.val)
            add_leaves(node.left, boundary)
            add_leaves(node.right, boundary)

        def add_right_boundary(node, boundary):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                node = node.right if node.right else node.left
            while stack:
                boundary.append(stack.pop())

        boundary = [root.val] if not is_leaf(root) else []
        add_left_boundary(root.left, boundary)
        add_leaves(root, boundary)
        add_right_boundary(root.right, boundary)

        return boundary

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(4)
    print(Solution().boundaryOfBinaryTree(root1))  # Output: [1, 3, 4, 2]

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(8)
    print(Solution().boundaryOfBinaryTree(root2))  # Output: [1, 2, 4, 7, 8, 6, 3]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Traversing the left boundary takes O(H), where H is the height of the tree.
   - Collecting the leaf nodes takes O(N), where N is the number of nodes in the tree.
   - Traversing the right boundary takes O(H).
   - Overall, the time complexity is O(N), as we visit each node at most once.

2. Space Complexity:
   - The space complexity is O(H) due to the recursion stack for collecting leaves and traversing boundaries.
   - In the worst case (skewed tree), H = N, so the space complexity is O(N).
   - In a balanced tree, H = log(N), so the space complexity is O(log(N)).

Topic: Binary Tree
"""