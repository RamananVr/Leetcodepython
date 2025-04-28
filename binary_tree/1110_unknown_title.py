"""
LeetCode Problem #1110: Delete Nodes And Return Forest

Problem Statement:
Given the root of a binary tree, each node in the tree has a distinct value. After deleting all the nodes with a value in the `to_delete` list, we are left with a forest (a disjoint union of trees). Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Constraints:
- The number of nodes in the given tree is at most 1000.
- Each node has a distinct value between 1 and 1000.
- `to_delete.length <= 1000`
- `to_delete` contains distinct values between 1 and 1000.

"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            # Check if the current node needs to be deleted
            node_deleted = node.val in to_delete_set
            if is_root and not node_deleted:
                forest.append(node)
            # Recursively process the left and right children
            node.left = helper(node.left, node_deleted)
            node.right = helper(node.right, node_deleted)
            return None if node_deleted else node

        helper(root, True)
        return forest

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

# Helper function to serialize a binary tree to a list
def serialize_tree(root):
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

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
    to_delete1 = [3, 5]
    result1 = solution.delNodes(root1, to_delete1)
    print([serialize_tree(tree) for tree in result1])  # Expected: [[1, 2, None, 4], [6], [7]]

    # Test Case 2
    root2 = build_tree([1, 2, 4, None, 3])
    to_delete2 = [3]
    result2 = solution.delNodes(root2, to_delete2)
    print([serialize_tree(tree) for tree in result2])  # Expected: [[1, 2, 4]]

"""
Time Complexity:
- Let `n` be the number of nodes in the tree.
- Each node is visited once, so the time complexity is O(n).
- The `to_delete` list is converted to a set for O(1) lookups, which takes O(m), where `m` is the size of `to_delete`.
- Overall time complexity: O(n + m).

Space Complexity:
- The recursion stack can go as deep as the height of the tree, which is O(h), where `h` is the height of the tree.
- The `forest` list stores the roots of the resulting trees, which can be at most O(n) in the worst case.
- The `to_delete_set` takes O(m) space.
- Overall space complexity: O(n + m).

Topic: Binary Tree
"""