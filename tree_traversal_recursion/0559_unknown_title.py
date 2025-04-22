"""
LeetCode Problem #559: Maximum Depth of N-ary Tree

Problem Statement:
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Constraints:
- The depth of the n-ary tree is less than or equal to 1000.
- The total number of nodes is between [0, 10^4].

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11]
Output: 4
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Solution
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build an N-ary tree from a nested list
    def build_tree(data):
        if not data:
            return None
        root = Node(data[0])
        queue = [root]
        i = 2
        while i < len(data):
            parent = queue.pop(0)
            while i < len(data) and data[i] is not None:
                child = Node(data[i])
                parent.children.append(child)
                queue.append(child)
                i += 1
            i += 1  # Skip the None separator
        return root

    # Test Case 1
    root1 = build_tree([1, None, 3, 2, 4, None, 5, 6])
    print(Solution().maxDepth(root1))  # Output: 3

    # Test Case 2
    root2 = build_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11])
    print(Solution().maxDepth(root2))  # Output: 4

    # Test Case 3 (Edge Case: Empty Tree)
    root3 = build_tree([])
    print(Solution().maxDepth(root3))  # Output: 0

    # Test Case 4 (Single Node Tree)
    root4 = build_tree([1])
    print(Solution().maxDepth(root4))  # Output: 1

# Time Complexity Analysis:
# The function visits each node exactly once, and for each node, it computes the maximum depth of its children.
# Let n be the total number of nodes in the tree.
# Time Complexity: O(n)

# Space Complexity Analysis:
# The space complexity is determined by the recursion stack. In the worst case, the recursion stack can go as deep as the height of the tree.
# Let h be the height of the tree.
# Space Complexity: O(h)

# Topic: Tree Traversal, Recursion