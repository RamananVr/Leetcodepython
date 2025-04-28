"""
LeetCode Problem #2560: House Robber IV

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the amount of money in the ith house is nums[i]. All houses at this place are arranged in a straight line.

You are given an integer k, which represents the maximum number of houses you can rob. Your goal is to minimize the maximum amount of money robbed from any single house while still robbing exactly k houses.

Return the minimum possible value of the maximum amount of money robbed from any single house.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

# Solution
from typing import List

def minCapability(nums: List[int], k: int) -> int:
    def can_rob_with_max(max_capability: int) -> bool:
        """Check if it's possible to rob k houses with the given max capability."""
        robbed = 0
        i = 0
        while i < len(nums):
            if nums[i] <= max_capability:
                robbed += 1
                i += 2  # Skip the next house to avoid adjacent robbery
            else:
                i += 1
            if robbed >= k:
                return True
        return False

    # Binary search for the minimum possible max capability
    left, right = min(nums), max(nums)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_rob_with_max(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 3, 5, 9]
    k = 2
    print(minCapability(nums, k))  # Expected Output: 5

    # Test Case 2
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(minCapability(nums, k))  # Expected Output: 3

    # Test Case 3
    nums = [10, 1, 10, 1, 10]
    k = 2
    print(minCapability(nums, k))  # Expected Output: 10

    # Test Case 4
    nums = [1, 1, 1, 1, 1]
    k = 3
    print(minCapability(nums, k))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max(nums) - min(nums))).
- For each binary search iteration, the `can_rob_with_max` function iterates through the `nums` array, which takes O(n).
- Therefore, the overall time complexity is O(n * log(max(nums) - min(nums))).

Space Complexity:
- The solution uses O(1) additional space, as no extra data structures are used.

Topic: Binary Search
"""