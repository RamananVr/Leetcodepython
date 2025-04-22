"""
LeetCode Question #805: Split Array With Same Average

Problem Statement:
You are given an integer array `nums`. You want to split the array into two subsets `A` and `B` such that:

1. The average of `A` is equal to the average of `B`.
2. Both `A` and `B` are non-empty.
3. `A` and `B` together cover all the elements of the array.

Return `true` if it is possible to achieve such a split, or `false` otherwise.

Note:
- The average of a set of `k` elements is equal to the sum of the elements divided by `k`.
- The array can contain up to 30 elements, and each element will be between 0 and 10,000.

Example 1:
Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], both of which have the same average.

Example 2:
Input: nums = [3,1]
Output: false

Constraints:
- 1 <= nums.length <= 30
- 0 <= nums[i] <= 10^4
"""

from typing import List
from functools import lru_cache

def splitArraySameAverage(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    
    # If it's not possible to split into two subsets with the same average, return False early
    for size in range(1, n // 2 + 1):
        if (total_sum * size) % n == 0:
            break
    else:
        return False

    # Use dynamic programming with memoization
    @lru_cache(None)
    def dfs(index: int, subset_size: int, subset_sum: int) -> bool:
        if subset_size == 0:
            return subset_sum == 0
        if index == n or subset_size < 0 or subset_sum < 0:
            return False
        # Include nums[index] in the subset or skip it
        return dfs(index + 1, subset_size - 1, subset_sum - nums[index]) or dfs(index + 1, subset_size, subset_sum)

    # Try all possible subset sizes
    for size in range(1, n // 2 + 1):
        if (total_sum * size) % n == 0:
            target_sum = (total_sum * size) // n
            if dfs(0, size, target_sum):
                return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(splitArraySameAverage(nums1))  # Output: True

    # Test Case 2
    nums2 = [3, 1]
    print(splitArraySameAverage(nums2))  # Output: False

    # Test Case 3
    nums3 = [18, 10, 5, 3]
    print(splitArraySameAverage(nums3))  # Output: False

    # Test Case 4
    nums4 = [6, 8, 18, 3, 1]
    print(splitArraySameAverage(nums4))  # Output: True

"""
Time Complexity:
- The time complexity is O(n * sum(nums) * n/2), where `n` is the length of the array. This is because we are iterating over all possible subset sizes and using memoization to avoid redundant calculations.

Space Complexity:
- The space complexity is O(n * sum(nums) * n/2) due to the memoization table and the recursion stack.

Topic: Dynamic Programming
"""