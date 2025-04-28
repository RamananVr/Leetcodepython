"""
LeetCode Question #1457: Pseudo-Palindromic Paths in a Binary Tree

Problem Statement:
Given a binary tree where node values are digits from 1 to 9, a path in the binary tree is said to be pseudo-palindromic 
if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example:
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure below shows the two pseudo-palindromic paths:
- Path [2,3,3] can be rearranged as [3,2,3] (a palindrome).
- Path [2,1,1] can be rearranged as [1,2,1] (a palindrome).

Constraints:
1. The number of nodes in the tree is in the range [1, 10^5].
2. 1 <= Node.val <= 9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
def pseudoPalindromicPaths(root: TreeNode) -> int:
    def dfs(node, path_count):
        if not node:
            return 0
        
        # Toggle the bit corresponding to the current node's value
        path_count ^= (1 << node.val)
        
        # If it's a leaf node, check if the path_count represents a pseudo-palindrome
        if not node.left and not node.right:
            # Check if at most one bit is set in path_count
            return int(path_count & (path_count - 1) == 0)
        
        # Continue DFS traversal
        return dfs(node.left, path_count) + dfs(node.right, path_count)
    
    return dfs(root, 0)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(2)
    root1.left = TreeNode(3)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(1)
    print(pseudoPalindromicPaths(root1))  # Output: 2

    # Example 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.left.right.right = TreeNode(1)
    print(pseudoPalindromicPaths(root2))  # Output: 1

    # Example 3
    root3 = TreeNode(9)
    print(pseudoPalindromicPaths(root3))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack during DFS traversal.
- In the worst case (a skewed tree), the recursion stack can go up to O(n).
- In the best case (a balanced tree), the recursion stack depth is O(log n).
- Additionally, we use a constant amount of space for the path_count variable, which is O(1).
- Overall space complexity: O(n) in the worst case.

Topic: Binary Tree
"""