"""
LeetCode Question #865: Smallest Subtree with all the Deepest Nodes

Problem Statement:
Given the root of a binary tree, the subtree with the deepest nodes is the smallest 
subtree that contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the 
entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants 
of that node.

Return the smallest subtree that contains all the deepest nodes. If there are multiple 
deepest nodes, the result should be the smallest subtree that contains them all.

Note: The depth of the root node is 0.

Constraints:
- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 500
- The values of the nodes in the tree are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)  # (depth, subtree)
            
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_depth + 1, left_subtree)
            elif right_depth > left_depth:
                return (right_depth + 1, right_subtree)
            else:
                return (left_depth + 1, node)
        
        return dfs(root)[1]

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    
    solution = Solution()
    result1 = solution.subtreeWithAllDeepest(root1)
    print(result1.val)  # Output: 2

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    
    result2 = solution.subtreeWithAllDeepest(root2)
    print(result2.val)  # Output: 4

    # Example 3
    root3 = TreeNode(1)
    
    result3 = solution.subtreeWithAllDeepest(root3)
    print(result3.val)  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
The function performs a depth-first search (DFS) on the binary tree. Since each node is 
visited once, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
The space complexity is O(h), where h is the height of the tree. This is due to the 
recursive call stack during DFS. In the worst case (a skewed tree), h can be equal to n, 
so the space complexity is O(n). In the best case (a balanced tree), h is log(n), so the 
space complexity is O(log(n)).
"""

# Topic: Binary Tree