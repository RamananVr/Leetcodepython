"""
LeetCode Question #100: Same Tree

Problem Statement:
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
    - The number of nodes in both trees is in the range [0, 100].
    - -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    Determines if two binary trees are the same.
    """
    # Base case: if both nodes are None, they are the same
    if not p and not q:
        return True
    # If one of the nodes is None or their values are different, they are not the same
    if not p or not q or p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a binary tree from a list
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
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(isSameTree(p1, q1))  # Output: True

    # Test Case 2
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print(isSameTree(p2, q2))  # Output: False

    # Test Case 3
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(isSameTree(p3, q3))  # Output: False

    # Test Case 4
    p4 = build_tree([])
    q4 = build_tree([])
    print(isSameTree(p4, q4))  # Output: True

    # Test Case 5
    p5 = build_tree([1])
    q5 = build_tree([1])
    print(isSameTree(p5, q5))  # Output: True

# Time Complexity Analysis:
# The function visits each node in both trees exactly once. 
# Let n be the number of nodes in tree `p` and m be the number of nodes in tree `q`.
# In the worst case, we visit all nodes in both trees, so the time complexity is O(min(n, m)).

# Space Complexity Analysis:
# The space complexity is determined by the recursion stack. In the worst case, the recursion depth
# is equal to the height of the tree. For a balanced tree, the height is O(log(min(n, m))), and for
# a skewed tree, the height is O(min(n, m)). Thus, the space complexity is O(min(n, m)).

# Topic: Binary Tree