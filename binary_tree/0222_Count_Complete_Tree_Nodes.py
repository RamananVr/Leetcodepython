"""
LeetCode Problem #222: Count Complete Tree Nodes

Problem Statement:
Given the root of a complete binary tree, return the number of the nodes in the tree.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at 
the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Constraints:
- The number of nodes in the tree is in the range [0, 5 * 10^4].
- 0 <= Node.val <= 10^5
- The tree is complete.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    """
    Function to count the number of nodes in a complete binary tree.
    """
    def get_tree_depth(node):
        """
        Helper function to calculate the depth of the leftmost path in the tree.
        """
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    if not root:
        return 0

    left_depth = get_tree_depth(root.left)
    right_depth = get_tree_depth(root.right)

    if left_depth == right_depth:
        # Left subtree is a perfect binary tree
        return (1 << left_depth) + countNodes(root.right)
    else:
        # Right subtree is a perfect binary tree
        return (1 << right_depth) + countNodes(root.left)

# Example Test Cases
if __name__ == "__main__":
    # Example 1:
    # Input: [1, 2, 3, 4, 5, 6]
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    / \   /
    #   4   5 6
    # Output: 6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(countNodes(root1))  # Output: 6

    # Example 2:
    # Input: []
    # Output: 0
    root2 = None
    print(countNodes(root2))  # Output: 0

    # Example 3:
    # Input: [1]
    # Tree structure:
    #        1
    # Output: 1
    root3 = TreeNode(1)
    print(countNodes(root3))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm calculates the depth of the leftmost and rightmost paths in the tree, which takes O(log n) time.
- For each recursive call, the algorithm either processes the left or right subtree, effectively halving the problem size.
- Therefore, the overall time complexity is O(log^2 n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(log n) due to the recursive stack depth, which corresponds to the height of the tree.

Topic: Binary Tree
"""