"""
LeetCode Question #272: Closest Binary Search Tree Value II

Problem Statement:
Given the `root` of a binary search tree, a target value `target`, and an integer `k`, return the `k` values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of `k` values in the BST that are closest to the target.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9
- 1 <= k <= n

Example:
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]

Follow-up:
Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n is the total number of nodes)?
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        Finds the k values in the BST that are closest to the target.
        """
        # Helper function to perform an in-order traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform in-order traversal to get sorted values
        sorted_values = inorder(root)
        
        # Sort the values by their absolute difference from the target
        sorted_values.sort(key=lambda x: abs(x - target))
        
        # Return the first k values
        return sorted_values[:k]

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
    root = build_tree([4, 2, 5, 1, 3])
    target = 3.714286
    k = 2
    solution = Solution()
    print(solution.closestKValues(root, target, k))  # Output: [4, 3]

    # Test Case 2
    root = build_tree([1])
    target = 0.0
    k = 1
    print(solution.closestKValues(root, target, k))  # Output: [1]

    # Test Case 3
    root = build_tree([7, 4, 10, 2, 6, 8, 12])
    target = 5.5
    k = 3
    print(solution.closestKValues(root, target, k))  # Output: [6, 4, 7]

"""
Time Complexity:
- The in-order traversal takes O(n), where n is the number of nodes in the BST.
- Sorting the values by their absolute difference from the target takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The in-order traversal stores all the node values in a list, which takes O(n) space.
- Overall space complexity: O(n).

Topic: Binary Search Tree (BST), Sorting, In-Order Traversal
"""