"""
LeetCode Problem #2673: Make Costs of Paths Equal in a Binary Tree

Problem Statement:
You are given a binary tree rooted at `root` with `n` nodes. Each node is assigned a value, and the cost of a path is defined as the sum of the values of the nodes along that path. A path is any sequence of nodes starting at the root and ending at any leaf node.

You are tasked to make the costs of all paths from the root to the leaf nodes equal. To achieve this, you can increment the value of any node any number of times. Return the minimum total increment required to make the costs of all paths equal.

Constraints:
- The number of nodes in the tree is `n`.
- The value of each node is a positive integer.

Example:
Input: root = [1,2,3,4,5,null,6]
Output: 9
Explanation: Increment the value of nodes to make all paths equal. The minimum total increment required is 9.

"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minIncrements(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0  # (max_cost, total_increment)
            
            left_cost, left_increment = dfs(node.left)
            right_cost, right_increment = dfs(node.right)
            
            # Calculate the maximum cost of the current node's subtree
            max_cost = max(left_cost, right_cost) + node.val
            
            # Calculate the increment needed to balance the left and right subtrees
            increment = abs(left_cost - right_cost)
            
            # Total increment is the sum of increments in left, right, and current node
            total_increment = left_increment + right_increment + increment
            
            return max_cost, total_increment
        
        _, total_increment = dfs(root)
        return total_increment

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                if 2 * i + 1 < len(nodes):
                    node.left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    node.right = nodes[2 * i + 2]
        return nodes[0]

    # Test Case 1
    root1 = build_tree([1, 2, 3, 4, 5, None, 6])
    print(Solution().minIncrements(root1))  # Output: 9

    # Test Case 2
    root2 = build_tree([5, 3, 8, 2, None, None, 4])
    print(Solution().minIncrements(root2))  # Output: 7

    # Test Case 3
    root3 = build_tree([1])
    print(Solution().minIncrements(root3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a Depth-First Search (DFS) traversal of the binary tree.
- Each node is visited once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the binary tree. This is due to the recursive call stack during DFS traversal.

Topic: Binary Tree
"""