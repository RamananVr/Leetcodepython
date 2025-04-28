"""
LeetCode Question #1120: Maximum Average Subtree

Problem Statement:
Given the root of a binary tree, return the maximum average value of any subtree of that tree. 
A subtree of a tree is any node of that tree plus all its descendants. 
The average value of a subtree is the sum of its values, divided by the number of nodes.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^5

Note:
- You may assume that the tree is non-empty.
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_average = 0  # Initialize the maximum average
        
        def dfs(node):
            if not node:
                return (0, 0)  # Return (sum, count) for an empty subtree
            
            # Recursively calculate sum and count for left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current subtree's sum and count
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Update the maximum average
            self.max_average = max(self.max_average, current_sum / current_count)
            
            return (current_sum, current_count)
        
        dfs(root)  # Start DFS traversal from the root
        return self.max_average

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(5)
    root1.left = TreeNode(6)
    root1.right = TreeNode(1)
    print(Solution().maximumAverageSubtree(root1))  # Output: 6.0

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    print(Solution().maximumAverageSubtree(root2))  # Output: 4.0

    # Example 3
    root3 = TreeNode(10)
    root3.left = TreeNode(20)
    root3.right = TreeNode(30)
    root3.left.left = TreeNode(40)
    root3.left.right = TreeNode(50)
    print(Solution().maximumAverageSubtree(root3))  # Output: 40.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a DFS traversal of the binary tree, visiting each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack during DFS traversal.
- In the worst case (a completely unbalanced tree), the recursion stack can go up to O(n).
- In the best case (a balanced tree), the recursion stack depth is O(log n).
- Thus, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""