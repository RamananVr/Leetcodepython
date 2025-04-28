"""
LeetCode Problem #437: Path Sum III

Problem Statement:
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values 
along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent 
nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
"""

# Clean, Correct Python Solution
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Count paths ending at the current node
            current_sum += node.val
            path_count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Update prefix_sums for the current path
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Explore left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # Backtrack: remove the current node's sum from prefix_sums
            prefix_sums[current_sum] -= 1
            
            return path_count
        
        prefix_sums = {0: 1}  # Initialize prefix_sums with base case
        return dfs(root, 0)

# Example Test Cases
def test_solution():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(values)):
            if nodes[i] is not None:
                if 2 * i + 1 < len(values):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(values):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]

    solution = Solution()

    # Test Case 1
    root1 = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum1 = 8
    assert solution.pathSum(root1, targetSum1) == 3

    # Test Case 2
    root2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    targetSum2 = 22
    assert solution.pathSum(root2, targetSum2) == 3

    # Test Case 3
    root3 = build_tree([])
    targetSum3 = 0
    assert solution.pathSum(root3, targetSum3) == 0

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node is visited once, and for each node, we perform constant-time operations to update and query the prefix_sums dictionary.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h + n), where h is the height of the tree and n is the number of unique prefix sums stored in the dictionary.
- In the worst case, h = n (for a skewed tree), and the prefix_sums dictionary can store up to n entries.

Overall, the space complexity is O(n).
"""

# Primary Topic
# Topic: Binary Tree

# Run the test cases
if __name__ == "__main__":
    test_solution()