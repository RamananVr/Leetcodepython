"""
LeetCode Question #110: Balanced Binary Tree

Problem Statement:
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true
    Explanation: The tree is balanced because:
                 - The left subtree has a height of 1 (node 9).
                 - The right subtree has a height of 2 (nodes 20 -> 15/7).
                 - The difference in height is 1, which is <= 1.

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
    Explanation: The tree is not balanced because:
                 - The left subtree has a height of 3 (nodes 1 -> 2 -> 3 -> 4).
                 - The right subtree has a height of 1 (node 2).
                 - The difference in height is 2, which is > 1.

Example 3:
    Input: root = []
    Output: true
    Explanation: An empty tree is balanced.

Constraints:
    - The number of nodes in the tree is in the range [0, 5000].
    - -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Determines if a binary tree is height-balanced.
        """
        def check_balance(node):
            # Base case: an empty tree is balanced and has height -1
            if not node:
                return 0, True
            
            # Recursively check the left and right subtrees
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            # Current node is balanced if:
            # 1. Left and right subtrees are balanced
            # 2. The height difference between left and right subtrees is <= 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            # Height of the current node is 1 + max(left_height, right_height)
            height = 1 + max(left_height, right_height)
            
            return height, balanced
        
        # Start the recursive check from the root
        _, is_balanced = check_balance(root)
        return is_balanced

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
    print(Solution().isBalanced(root1))  # Output: True

    # Test Case 2
    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(Solution().isBalanced(root2))  # Output: False

    # Test Case 3
    root3 = build_tree([])
    print(Solution().isBalanced(root3))  # Output: True

"""
Time Complexity:
- The function performs a post-order traversal of the tree, visiting each node once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is O(h), where h is the height of the tree.
- This is due to the recursive call stack, which can go as deep as the height of the tree.

Topic: Binary Tree
"""