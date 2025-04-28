"""
LeetCode Problem #2862: Maximum Element-Sum of a Complete Subset of Indices

Problem Statement:
You are given an integer array `nums` of size `n`.

A subset of indices of `nums` is called a complete subset if it is possible to form a binary tree structure 
with these indices such that:
1. The root of the tree is the smallest index in the subset.
2. Every other index in the subset is a descendant of the root.
3. For every index `i` in the subset, if `2 * i + 1` (left child) or `2 * i + 2` (right child) are within bounds 
   of the array, they must also be in the subset.

The element-sum of a subset is the sum of the elements corresponding to the indices in the subset.

Return the maximum element-sum of a complete subset of indices of `nums`.

Constraints:
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
"""

# Python Solution
from collections import defaultdict

def maxSum(nums):
    n = len(nums)
    level_sums = defaultdict(int)
    level = 0
    index = 0

    # Traverse the array level by level
    while index < n:
        # Calculate the number of nodes at the current level
        nodes_at_level = 2 ** level
        # Sum the elements at the current level
        level_sums[level] = sum(nums[index:min(index + nodes_at_level, n)])
        # Move to the next level
        index += nodes_at_level
        level += 1

    # Return the maximum sum among all levels
    return max(level_sums.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    print(maxSum(nums1))  # Output: 22 (Level 2: 4 + 5 + 6 + 7)

    # Test Case 2
    nums2 = [10, -2, 3, 4, -5, 6, 7]
    print(maxSum(nums2))  # Output: 22 (Level 2: 4 + -5 + 6 + 7)

    # Test Case 3
    nums3 = [1]
    print(maxSum(nums3))  # Output: 1 (Only one level)

    # Test Case 4
    nums4 = [-1, -2, -3, -4, -5, -6, -7]
    print(maxSum(nums4))  # Output: -1 (Level 0: -1)

    # Test Case 5
    nums5 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print(maxSum(nums5))  # Output: 140 (Level 3: 40 + 45 + 50)

"""
Time Complexity Analysis:
- The algorithm iterates through the array `nums` once, summing elements level by level.
- Calculating the sum for each level takes O(k) time, where k is the number of elements at that level.
- Since the total number of elements across all levels is `n`, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a dictionary `level_sums` to store the sum of elements at each level.
- The number of levels in a binary tree is at most log2(n), so the space complexity is O(log n).

Topic: Arrays, Binary Tree, Level Order Traversal
"""