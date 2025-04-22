"""
LeetCode Question #145: Binary Tree Postorder Traversal

Problem Statement:
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Postorder traversal is defined as:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root.

Example:
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow-up:
Recursive solution is straightforward, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Clean and Correct Python Solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        # Recursive solution
        def postorder(node):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]
        
        return postorder(root)

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
    root1 = build_tree([1, None, 2, 3])
    print(Solution().postorderTraversal(root1))  # Output: [3, 2, 1]

    # Test Case 2
    root2 = build_tree([])
    print(Solution().postorderTraversal(root2))  # Output: []

    # Test Case 3
    root3 = build_tree([1])
    print(Solution().postorderTraversal(root3))  # Output: [1]

    # Test Case 4
    root4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(Solution().postorderTraversal(root4))  # Output: [4, 5, 2, 6, 7, 3, 1]

    # Test Case 5
    root5 = build_tree([1, None, 2, None, 3])
    print(Solution().postorderTraversal(root5))  # Output: [3, 2, 1]

"""
Time Complexity Analysis:
- The function visits each node exactly once, performing O(1) work per node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- In the worst case (a completely unbalanced tree), the recursion stack can go as deep as the height of the tree, which is O(n) in the worst case.
- In the best case (a completely balanced tree), the height of the tree is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""