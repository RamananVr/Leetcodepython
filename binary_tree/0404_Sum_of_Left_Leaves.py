"""
LeetCode Problem #404: Sum of Left Leaves

Problem Statement:
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of its parent.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 24
    Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
    Input: root = [1]
    Output: 0

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    """
    This function calculates the sum of all left leaves in a binary tree.
    """
    if not root:
        return 0

    def is_leaf(node):
        return node and not node.left and not node.right

    total_sum = 0
    if is_leaf(root.left):
        total_sum += root.left.val
    else:
        total_sum += sumOfLeftLeaves(root.left)

    total_sum += sumOfLeftLeaves(root.right)

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(sumOfLeftLeaves(root1))  # Output: 24

    # Test Case 2
    root2 = build_tree([1])
    print(sumOfLeftLeaves(root2))  # Output: 0

    # Test Case 3
    root3 = build_tree([1, 2, 3, 4, 5])
    print(sumOfLeftLeaves(root3))  # Output: 4

    # Test Case 4
    root4 = build_tree([1, None, 2, None, 3])
    print(sumOfLeftLeaves(root4))  # Output: 0

"""
Time Complexity:
- The function visits each node of the binary tree exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack.
- In the worst case (skewed tree), the recursion stack can go up to O(n).
- In the best case (balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""