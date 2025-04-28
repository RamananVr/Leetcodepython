"""
LeetCode Problem #270: Closest Binary Search Tree Value

Problem Statement:
Given the `root` of a binary search tree and a target value `target`, return the value in the BST that is closest to the target.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. 0 <= Node.val <= 10^9
3. -10^9 <= target <= 10^9

Note:
- A binary search tree (BST) is a binary tree in which each node has at most two children, and for each node:
  - The left subtree contains only nodes with values less than the node's value.
  - The right subtree contains only nodes with values greater than the node's value.
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: TreeNode, target: float) -> int:
    """
    Finds the value in the BST that is closest to the target.

    Args:
    root (TreeNode): The root of the binary search tree.
    target (float): The target value.

    Returns:
    int: The value in the BST that is closest to the target.
    """
    closest = root.val  # Initialize closest value to the root's value
    current = root

    while current:
        # Update closest if the current node's value is closer to the target
        if abs(current.val - target) < abs(closest - target):
            closest = current.val

        # Move left or right depending on the target's value
        if target < current.val:
            current = current.left
        else:
            current = current.right

    return closest

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a BST from a list
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Test Case 1
    root1 = None
    for val in [4, 2, 5, 1, 3]:
        root1 = insert_into_bst(root1, val)
    target1 = 3.714286
    print(closestValue(root1, target1))  # Output: 4

    # Test Case 2
    root2 = None
    for val in [1]:
        root2 = insert_into_bst(root2, val)
    target2 = 4.0
    print(closestValue(root2, target2))  # Output: 1

    # Test Case 3
    root3 = None
    for val in [8, 5, 10, 3, 6, 9, 12]:
        root3 = insert_into_bst(root3, val)
    target3 = 7.5
    print(closestValue(root3, target3))  # Output: 8

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm traverses the height of the BST, which is O(h), where h is the height of the tree.
- In the worst case, h = O(n) for a skewed tree, and in the best case (balanced tree), h = O(log n).
- Therefore, the time complexity is O(h), which is O(log n) for a balanced tree and O(n) for a skewed tree.

Space Complexity:
- The algorithm uses O(1) additional space since it does not use any auxiliary data structures.
- The space complexity is O(1).
"""

# Topic: Binary Search Tree