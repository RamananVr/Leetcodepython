"""
LeetCode Problem #124: Binary Tree Maximum Path Sum

Problem Statement:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        This function calculates the maximum path sum in a binary tree.
        """
        self.max_sum = float('-inf')  # Initialize the maximum path sum as negative infinity

        def dfs(node):
            if not node:
                return 0  # Base case: return 0 for null nodes
            
            # Recursively calculate the maximum path sum for the left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore negative paths by taking max with 0
            right_max = max(dfs(node.right), 0)  # Ignore negative paths by taking max with 0
            
            # Calculate the maximum path sum passing through the current node
            current_path_sum = node.val + left_max + right_max
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum path sum including the current node and one of its subtrees
            return node.val + max(left_max, right_max)
        
        dfs(root)  # Start DFS traversal from the root
        return self.max_sum

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
    print(Solution().maxPathSum(root1))  # Output: 6 (path: 2 -> 1 -> 3)

    # Test Case 2
    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    print(Solution().maxPathSum(root2))  # Output: 42 (path: 15 -> 20 -> 7)

    # Test Case 3
    root3 = build_tree([2, -1])
    print(Solution().maxPathSum(root3))  # Output: 2 (path: 2)

    # Test Case 4
    root4 = build_tree([-3])
    print(Solution().maxPathSum(root4))  # Output: -3 (path: -3)

"""
Time Complexity Analysis:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack, which depends on the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(N), leading to O(N) space complexity.
- In the best case (balanced tree), the height of the tree is O(log N), leading to O(log N) space complexity.

Topic: Binary Tree
"""