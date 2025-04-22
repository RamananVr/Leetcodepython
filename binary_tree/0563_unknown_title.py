"""
LeetCode Problem #563: Binary Tree Tilt

Problem Statement:
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is considered to be 0. The rule is similar if there is no right child.

Example 1:
Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2: |0-0| = 0 (no children)
Tilt of node 3: |0-0| = 0 (no children)
Tilt of node 1: |2-3| = 1 (left subtree sum is 2, right subtree sum is 3)
Sum of tilts = 0 + 0 + 1 = 1

Example 2:
Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3: |0-0| = 0
Tilt of node 5: |0-0| = 0
Tilt of node 7: |0-0| = 0
Tilt of node 2: |3-5| = 2
Tilt of node 9: |0-7| = 7
Tilt of node 4: |10-16| = 6
Sum of tilts = 0 + 0 + 0 + 2 + 7 + 6 = 15

Example 3:
Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0
            # Recursively calculate the sum of left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            # Calculate the tilt for the current node
            self.total_tilt += abs(left_sum - right_sum)
            # Return the sum of the subtree rooted at this node
            return node.val + left_sum + right_sum

        dfs(root)
        return self.total_tilt

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
    root1 = build_tree([1, 2, 3])
    print(Solution().findTilt(root1))  # Output: 1

    # Test Case 2
    root2 = build_tree([4, 2, 9, 3, 5, None, 7])
    print(Solution().findTilt(root2))  # Output: 15

    # Test Case 3
    root3 = build_tree([21, 7, 14, 1, 1, 2, 2, 3, 3])
    print(Solution().findTilt(root3))  # Output: 9

    # Test Case 4 (Edge Case: Empty Tree)
    root4 = build_tree([])
    print(Solution().findTilt(root4))  # Output: 0

    # Test Case 5 (Single Node Tree)
    root5 = build_tree([5])
    print(Solution().findTilt(root5))  # Output: 0

"""
Time Complexity:
- Each node in the tree is visited exactly once during the depth-first search.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case (skewed tree), the recursion stack can go up to O(n). In the best case (balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""