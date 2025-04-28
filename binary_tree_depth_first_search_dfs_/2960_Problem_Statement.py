"""
LeetCode Problem #2960: Problem Statement

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root.

Write a function `maxPathSum` that takes the root of a binary tree as input and returns the maximum path sum.

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

def maxPathSum(root: TreeNode) -> int:
    """
    Function to calculate the maximum path sum in a binary tree.
    """
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Recursively calculate the maximum path sum for left and right subtrees
        left_max = max(dfs(node.left), 0)  # Ignore negative paths
        right_max = max(dfs(node.right), 0)  # Ignore negative paths
        
        # Update the global maximum path sum
        max_sum = max(max_sum, left_max + right_max + node.val)
        
        # Return the maximum path sum including the current node
        return node.val + max(left_max, right_max)
    
    max_sum = float('-inf')
    dfs(root)
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(maxPathSum(root1))  # Output: 6 (2 -> 1 -> 3)

    # Example 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(maxPathSum(root2))  # Output: 42 (15 -> 20 -> 7)

    # Example 3
    root3 = TreeNode(-3)
    print(maxPathSum(root3))  # Output: -3 (single node)

    # Example 4
    root4 = TreeNode(2)
    root4.left = TreeNode(-1)
    print(maxPathSum(root4))  # Output: 2 (single node)

    # Example 5
    root5 = TreeNode(10)
    root5.left = TreeNode(2)
    root5.right = TreeNode(10)
    root5.left.left = TreeNode(20)
    root5.left.right = TreeNode(1)
    root5.right.right = TreeNode(-25)
    root5.right.right.left = TreeNode(3)
    root5.right.right.right = TreeNode(4)
    print(maxPathSum(root5))  # Output: 42 (20 -> 2 -> 10 -> 10)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the depth-first search.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack used in the depth-first search.
- In the worst case (skewed tree), the recursion stack can go up to O(n).
- In the best case (balanced tree), the recursion stack will be O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree, Depth-First Search (DFS)
"""