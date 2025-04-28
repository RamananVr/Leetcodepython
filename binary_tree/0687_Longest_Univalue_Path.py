"""
LeetCode Problem #687: Longest Univalue Path

Problem Statement:
Given the root of a binary tree, return the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

Example:
Input: root = [5,4,5,1,1,5]
Output: 2

Input: root = [1,4,5,4,4,5]
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest_path = 0

        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the longest path in the left and right subtrees
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            # Check if the left and right child have the same value as the current node
            left_univalue = left_length + 1 if node.left and node.left.val == node.val else 0
            right_univalue = right_length + 1 if node.right and node.right.val == node.val else 0
            
            # Update the longest path found so far
            self.longest_path = max(self.longest_path, left_univalue + right_univalue)
            
            # Return the longest univalue path extending from the current node
            return max(left_univalue, right_univalue)
        
        dfs(root)
        return self.longest_path

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(values)):
            if nodes[i]:
                if 2 * i + 1 < len(values):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(values):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]

    # Test Case 1
    root1 = build_tree([5, 4, 5, 1, 1, 5])
    print(Solution().longestUnivaluePath(root1))  # Output: 2

    # Test Case 2
    root2 = build_tree([1, 4, 5, 4, 4, 5])
    print(Solution().longestUnivaluePath(root2))  # Output: 2

    # Test Case 3
    root3 = build_tree([1, 1, 1, 1, None, None, 1])
    print(Solution().longestUnivaluePath(root3))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a single traversal of the binary tree, visiting each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case (a completely unbalanced tree), 
  the recursion stack can go up to O(n). In the best case (a balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""