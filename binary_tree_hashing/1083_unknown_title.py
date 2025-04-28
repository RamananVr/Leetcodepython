"""
LeetCode Problem #1083: Find Duplicate Subtrees

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

from collections import defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[TreeNode]:
        """
        Finds all duplicate subtrees in a binary tree.
        """
        def serialize(node):
            if not node:
                return "#"
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[serial] += 1
            if count[serial] == 2:  # Add to result only the first time we encounter a duplicate
                result.append(node)
            return serial

        count = defaultdict(int)
        result = []
        serialize(root)
        return result

# Example Test Cases
def build_tree(values):
    """
    Helper function to build a binary tree from a list of values.
    """
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

def print_tree(root):
    """
    Helper function to print a tree in level-order for verification.
    """
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # Test Case 1
    root1 = build_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
    solution = Solution()
    duplicates1 = solution.findDuplicateSubtrees(root1)
    print([print_tree(node) for node in duplicates1])  # Expected Output: [[2, 4], [4]]

    # Test Case 2
    root2 = build_tree([2, 1, 1])
    duplicates2 = solution.findDuplicateSubtrees(root2)
    print([print_tree(node) for node in duplicates2])  # Expected Output: [[1]]

    # Test Case 3
    root3 = build_tree([2, 2, 2, 3, None, 3, None])
    duplicates3 = solution.findDuplicateSubtrees(root3)
    print([print_tree(node) for node in duplicates3])  # Expected Output: [[2, 3], [3]]

"""
Time Complexity:
- Each node is visited once, and the serialization of each subtree takes O(h) time, where h is the height of the tree.
- In the worst case, the height of the tree is O(n), so the serialization takes O(n) per node.
- Thus, the overall time complexity is O(n^2) in the worst case.

Space Complexity:
- The space complexity is O(n) for the recursion stack in the worst case (skewed tree) and O(n) for the hash map storing the serialized subtrees.
- Therefore, the total space complexity is O(n).

Topic: Binary Tree, Hashing
"""