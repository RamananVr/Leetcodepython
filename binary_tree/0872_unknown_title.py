"""
LeetCode Problem #872: Leaf-Similar Trees

Problem Statement:
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree below:
        3
       / \
      5   1
     / \ / \
    6  2 9  8
      / \
     7   4

The leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:
- The number of nodes in each tree will be in the range [1, 200].
- The values of each node will be in the range [0, 200].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    """
    Determines if two binary trees are leaf-similar.
    """
    def get_leaves(root):
        # Helper function to collect leaf values in a list
        leaves = []
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:  # It's a leaf
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return leaves

    # Get leaf sequences for both trees
    leaves1 = get_leaves(root1)
    leaves2 = get_leaves(root2)

    # Compare the two leaf sequences
    return leaves1 == leaves2

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    print(leafSimilar(root1, root2))  # Output: True

    # Example 2
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    print(leafSimilar(root1, root2))  # Output: False

"""
Time Complexity:
- The `get_leaves` function performs a depth-first search (DFS) on each tree.
- For a tree with `n` nodes, the DFS visits each node once, so the time complexity is O(n).
- Since we perform this operation for both trees, the overall time complexity is O(n1 + n2), 
  where `n1` and `n2` are the number of nodes in the two trees.

Space Complexity:
- The space complexity is determined by the recursion stack used in the DFS.
- In the worst case (for a completely unbalanced tree), the recursion stack can go as deep as the number of nodes in the tree, O(n).
- Additionally, we store the leaf values in a list, which can also take O(n) space.
- Thus, the overall space complexity is O(n1 + n2), where `n1` and `n2` are the number of nodes in the two trees.

Topic: Binary Tree
"""