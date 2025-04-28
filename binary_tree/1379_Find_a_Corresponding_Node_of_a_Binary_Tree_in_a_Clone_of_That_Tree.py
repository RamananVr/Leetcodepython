"""
LeetCode Problem #1379: Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Problem Statement:
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to modify any of the two trees or the target node, and the answer must be a reference to a node in the cloned tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- The values of the nodes of the tree are unique.
- target is a node from the original tree and is not null.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    """
    This function finds the corresponding node in the cloned tree that matches the target node in the original tree.
    """
    if not original or not cloned:
        return None

    # If the current node in the original tree matches the target, return the corresponding node in the cloned tree
    if original == target:
        return cloned

    # Recursively search in the left subtree
    left_result = getTargetCopy(original.left, cloned.left, target)
    if left_result:
        return left_result

    # Recursively search in the right subtree
    return getTargetCopy(original.right, cloned.right, target)

# Example Test Cases
if __name__ == "__main__":
    # Example 1:
    # Input: original = [7,4,3,null,null,6,19], cloned = [7,4,3,null,null,6,19], target = 3
    # Output: Reference to node with value 3 in the cloned tree
    original = TreeNode(7)
    original.left = TreeNode(4)
    original.right = TreeNode(3)
    original.right.left = TreeNode(6)
    original.right.right = TreeNode(19)

    cloned = TreeNode(7)
    cloned.left = TreeNode(4)
    cloned.right = TreeNode(3)
    cloned.right.left = TreeNode(6)
    cloned.right.right = TreeNode(19)

    target = original.right  # Node with value 3

    result = getTargetCopy(original, cloned, target)
    print(result.val)  # Expected Output: 3

    # Example 2:
    # Input: original = [1,2,3], cloned = [1,2,3], target = 2
    # Output: Reference to node with value 2 in the cloned tree
    original = TreeNode(1)
    original.left = TreeNode(2)
    original.right = TreeNode(3)

    cloned = TreeNode(1)
    cloned.left = TreeNode(2)
    cloned.right = TreeNode(3)

    target = original.left  # Node with value 2

    result = getTargetCopy(original, cloned, target)
    print(result.val)  # Expected Output: 2

# Time Complexity Analysis:
# The function performs a depth-first search (DFS) on both the original and cloned trees.
# In the worst case, we may need to traverse all nodes in the tree.
# Let n be the number of nodes in the tree.
# - Time Complexity: O(n), where n is the number of nodes in the tree.
# - Space Complexity: O(h), where h is the height of the tree (due to the recursion stack). In the worst case, h = O(n) for a skewed tree.

# Topic: Binary Tree