"""
LeetCode Problem #654: Maximum Binary Tree

Problem Statement:
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

1. Create a root node whose value is the maximum value in nums.
2. Recursively build the left subtree on the subarray to the left of the maximum value.
3. Recursively build the right subtree on the subarray to the right of the maximum value.

Return the root node of the maximum binary tree.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^3
"""

# Solution
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find the index of the maximum value in the array
        max_index = nums.index(max(nums))
        
        # Create the root node with the maximum value
        root = TreeNode(nums[max_index])
        
        # Recursively construct the left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        
        return root

# Example Test Cases
def print_tree(root: Optional[TreeNode]):
    """Helper function to print the tree in pre-order traversal."""
    if not root:
        return []
    return [root.val] + print_tree(root.left) + print_tree(root.right)

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 1, 6, 0, 5]
    root1 = solution.constructMaximumBinaryTree(nums1)
    print("Test Case 1:", print_tree(root1))  # Expected Output: [6, 3, 2, 1, 5, 0]
    
    # Test Case 2
    nums2 = [1, 2, 3]
    root2 = solution.constructMaximumBinaryTree(nums2)
    print("Test Case 2:", print_tree(root2))  # Expected Output: [3, 2, 1]
    
    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    root3 = solution.constructMaximumBinaryTree(nums3)
    print("Test Case 3:", print_tree(root3))  # Expected Output: [5, 4, 3, 2, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm finds the maximum value in the array, which takes O(n) time.
- It then recursively constructs the left and right subtrees. In the worst case (e.g., sorted array), the recursion depth is O(n), and each level processes a smaller subarray.
- Overall, the time complexity is O(n^2) in the worst case.

Space Complexity:
- The space complexity is dominated by the recursion stack. In the worst case (e.g., sorted array), the recursion depth is O(n).
- Additionally, the tree nodes themselves require O(n) space.
- Overall, the space complexity is O(n).
"""

# Topic: Binary Tree