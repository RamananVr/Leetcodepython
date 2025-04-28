"""
LeetCode Problem #1305: All Elements in Two Binary Search Trees

Problem Statement:
Given two binary search trees, root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:
1. The number of nodes in each tree is in the range [0, 5000].
2. -10^5 <= Node.val <= 10^5
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # Helper function to perform in-order traversal
        def in_order_traversal(root: Optional[TreeNode], result: List[int]):
            if not root:
                return
            in_order_traversal(root.left, result)
            result.append(root.val)
            in_order_traversal(root.right, result)
        
        # Perform in-order traversal on both trees
        list1, list2 = [], []
        in_order_traversal(root1, list1)
        in_order_traversal(root2, list2)
        
        # Merge the two sorted lists
        merged_list = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        
        # Add any remaining elements from list1 or list2
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1
        
        return merged_list

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
    root1 = build_tree([2, 1, 4])
    root2 = build_tree([1, 0, 3])
    print(Solution().getAllElements(root1, root2))  # Output: [0, 1, 1, 2, 3, 4]

    # Test Case 2
    root1 = build_tree([1, None, 8])
    root2 = build_tree([8, 1])
    print(Solution().getAllElements(root1, root2))  # Output: [1, 1, 8, 8]

    # Test Case 3
    root1 = build_tree([])
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().getAllElements(root1, root2))  # Output: [1, 2, 3, 4, 5, 6]

    # Test Case 4
    root1 = build_tree([0, -10, 10])
    root2 = build_tree([5, 1, 7, 0, 2])
    print(Solution().getAllElements(root1, root2))  # Output: [-10, 0, 0, 1, 2, 5, 7, 10]

"""
Time Complexity:
1. In-order traversal of both trees takes O(n1 + n2), where n1 and n2 are the number of nodes in root1 and root2, respectively.
2. Merging two sorted lists takes O(n1 + n2).
Overall time complexity: O(n1 + n2).

Space Complexity:
1. The space required for the in-order traversal is O(h1 + h2), where h1 and h2 are the heights of the two trees (due to recursion stack).
2. The space required to store the result is O(n1 + n2).
Overall space complexity: O(n1 + n2).

Topic: Binary Tree
"""