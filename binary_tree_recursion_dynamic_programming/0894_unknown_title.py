"""
LeetCode Problem #894: All Possible Full Binary Trees

Problem Statement:
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Given an integer n, return a list of all possible full binary trees with n nodes. 
Each node of each tree in the answer must have the value 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

If it is impossible to form a full binary tree with n nodes, return an empty list.

Constraints:
- 1 <= n <= 20
- The number of nodes n will always be odd.

Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]

Note:
- The output format of the trees is not unique. For example, the same full binary tree can be represented in multiple ways.
- You can return the output in any order.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Base case: If n is even, it's impossible to form a full binary tree
        if n % 2 == 0:
            return []
        
        # Memoization to store results for subproblems
        memo = {}

        def helper(n):
            # If the result for n is already computed, return it
            if n in memo:
                return memo[n]
            
            # Base case: A single node is a full binary tree
            if n == 1:
                return [TreeNode(0)]
            
            result = []
            # Iterate over all possible left and right subtree sizes
            for left_size in range(1, n, 2):  # Only odd sizes
                right_size = n - 1 - left_size
                left_trees = helper(left_size)
                right_trees = helper(right_size)
                
                # Combine left and right subtrees
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            
            # Store the result in memo and return it
            memo[n] = result
            return result
        
        return helper(n)

# Helper function to serialize a tree into a list for easier comparison
def serialize(root):
    """Serialize a binary tree into a list."""
    if not root:
        return []
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
    n = 7
    trees = solution.allPossibleFBT(n)
    print(f"Number of trees for n = {n}: {len(trees)}")
    for tree in trees:
        print(serialize(tree))
    
    # Test Case 2
    n = 3
    trees = solution.allPossibleFBT(n)
    print(f"Number of trees for n = {n}: {len(trees)}")
    for tree in trees:
        print(serialize(tree))

"""
Time Complexity:
- The time complexity is O(2^n), where n is the number of nodes. This is because for each odd number of nodes, 
  we recursively compute all possible left and right subtrees, leading to an exponential number of combinations.

Space Complexity:
- The space complexity is O(2^n) due to the memoization dictionary storing all possible trees for each odd number of nodes.

Topic: Binary Tree, Recursion, Dynamic Programming
"""