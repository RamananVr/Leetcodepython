"""
LeetCode Problem #652: Find Duplicate Subtrees

Problem Statement:
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
- The number of the nodes in the tree will be in the range [1, 5000].
- -200 <= Node.val <= 200
"""

from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Dictionary to store serialized subtree and its frequency
        subtree_map = defaultdict(int)
        duplicates = []

        def serialize(node):
            if not node:
                return "#"
            # Serialize the subtree rooted at the current node
            subtree = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            # Count the occurrence of this serialized subtree
            subtree_map[subtree] += 1
            # If this is the second time we've seen this subtree, add it to duplicates
            if subtree_map[subtree] == 2:
                duplicates.append(node)
            return subtree

        serialize(root)
        return duplicates

# Example Test Cases
def test_findDuplicateSubtrees():
    # Helper function to build a tree from a list
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
    root1 = build_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    solution = Solution()
    result1 = solution.findDuplicateSubtrees(root1)
    assert len(result1) == 2  # Expected: [[2,4],[4]]

    # Test Case 2
    root2 = build_tree([2, 1, 1])
    result2 = solution.findDuplicateSubtrees(root2)
    assert len(result2) == 1  # Expected: [[1]]

    # Test Case 3
    root3 = build_tree([2, 2, 2, 3, None, 3, None])
    result3 = solution.findDuplicateSubtrees(root3)
    assert len(result3) == 2  # Expected: [[2,3],[3]]

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node in the tree is visited once, and the serialization of each subtree takes O(h), where h is the height of the tree.
- In the worst case, the height of the tree is O(n), so the time complexity is O(n^2) in the worst case.
- However, for balanced trees, the height is O(log n), making the average time complexity O(n log n).

Space Complexity:
- The space complexity is O(n) for the dictionary storing the serialized subtrees and the recursion stack.

Overall, the time complexity is O(n^2) in the worst case and O(n log n) on average, while the space complexity is O(n).
"""

# Topic: Binary Tree

if __name__ == "__main__":
    test_findDuplicateSubtrees()