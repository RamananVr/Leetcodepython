"""
LeetCode Problem #95: Unique Binary Search Trees II

Problem Statement:
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
- 1 <= n <= 8
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                # Combine each left and right subtree with the current root i
                for left in left_trees:
                    for right in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = left
                        current_tree.right = right
                        all_trees.append(current_tree)
            
            return all_trees
        
        return build_trees(1, n)

# Helper function to serialize the tree into a list for easier comparison
def serialize(root):
    """Encodes a tree to a single list."""
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n = 3
    result = solution.generateTrees(n)
    serialized_result = [serialize(tree) for tree in result]
    print(f"Unique BSTs for n = {n}: {serialized_result}")
    
    # Test Case 2
    n = 1
    result = solution.generateTrees(n)
    serialized_result = [serialize(tree) for tree in result]
    print(f"Unique BSTs for n = {n}: {serialized_result}")

"""
Time Complexity:
- The time complexity of this solution is Catalan number C(n), which is approximately O(4^n / sqrt(n)).
  This is because the number of unique BSTs for n nodes is the nth Catalan number.

Space Complexity:
- The space complexity is O(n) for the recursion stack, where n is the number of nodes.

Topic: Binary Tree, Dynamic Programming, Recursion
"""