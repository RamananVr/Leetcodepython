"""
LeetCode Problem #1740: Find Distance in a Binary Tree

Problem Statement:
Given the root of a binary tree and two integers `p` and `q`, return the distance between the nodes of value `p` and `q`.
The distance between two nodes is the number of edges on the path from one to the other.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- All `Node.val` are unique.
- `p` and `q` are values that exist in the tree.

Example:
Input: root = [1, 2, 3, 4], p = 2, q = 3
Output: 2
Explanation: The tree is:
       1
      / \
     2   3
    /
   4
The distance between 2 and 3 is 2.

Input: root = [1, 2, 3, 4, 5], p = 4, q = 5
Output: 2
Explanation: The tree is:
       1
      / \
     2   3
    / \
   4   5
The distance between 4 and 5 is 2.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # Helper function to find the Lowest Common Ancestor (LCA) of two nodes
        def findLCA(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        # Helper function to find the distance from a given node to a target value
        def findDistanceFromNode(node, target, distance):
            if not node:
                return -1
            if node.val == target:
                return distance
            left = findDistanceFromNode(node.left, target, distance + 1)
            if left != -1:
                return left
            return findDistanceFromNode(node.right, target, distance + 1)

        # Find the LCA of p and q
        lca = findLCA(root, p, q)

        # Find the distance from the LCA to p and q
        distance_p = findDistanceFromNode(lca, p, 0)
        distance_q = findDistanceFromNode(lca, q, 0)

        # Return the total distance
        return distance_p + distance_q

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
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    # Test Case 1
    root1 = build_tree([1, 2, 3, 4])
    p1, q1 = 2, 3
    print(Solution().findDistance(root1, p1, q1))  # Output: 2

    # Test Case 2
    root2 = build_tree([1, 2, 3, 4, 5])
    p2, q2 = 4, 5
    print(Solution().findDistance(root2, p2, q2))  # Output: 2

    # Test Case 3
    root3 = build_tree([1, 2, 3, None, 4, None, 5])
    p3, q3 = 4, 5
    print(Solution().findDistance(root3, p3, q3))  # Output: 4

"""
Time Complexity:
- Finding the LCA: O(N), where N is the number of nodes in the tree.
- Finding the distance from the LCA to p and q: O(N) in the worst case.
- Overall: O(N).

Space Complexity:
- The recursion stack for the LCA and distance functions can go as deep as the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(N).
- Overall: O(N).

Topic: Binary Tree
"""