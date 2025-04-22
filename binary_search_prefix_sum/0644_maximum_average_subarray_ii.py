"""
LeetCode Question #644: Maximum Average Subarray II

Problem Statement:
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.
Find the contiguous subarray of length greater than or equal to `k` that has the maximum average value.
You need to output the maximum average value as a floating-point number up to 5 decimal places.

Constraints:
1. `n == nums.length`
2. `1 <= k <= n <= 10^4`
3. `-10^4 <= nums[i] <= 10^4`

Note:
- The result is guaranteed to be within the range `[-10^4, 10^4]`.
- The answer with the calculation error less than `10^-5` will be accepted.
"""

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    """
    Finds the maximum average of a subarray with length >= k using binary search.
    """
    def can_find_larger_average(mid: float) -> bool:
        """
        Helper function to check if there exists a subarray with an average >= mid.
        """
        prefix_sum = 0
        min_prefix_sum = 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i] - mid
            if i >= k - 1:
                if current_sum >= min_prefix_sum:
                    return True
                prefix_sum += nums[i - k + 1] - mid
                min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return False

    left, right = min(nums), max(nums)
    precision = 1e-5

    while right - left > precision:
        mid = (left + right) / 2
        if can_find_larger_average(mid):
            left = mid
        else:
            right = mid

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    print(f"Test Case 1: {findMaxAverage(nums1, k1):.5f}")  # Expected Output: 12.75000

    # Test Case 2
    nums2 = [5, 5, 5, 5, 5]
    k2 = 1
    print(f"Test Case 2: {findMaxAverage(nums2, k2):.5f}")  # Expected Output: 5.00000

    # Test Case 3
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    print(f"Test Case 3: {findMaxAverage(nums3, k3):.5f}")  # Expected Output: -1.50000

    # Test Case 4
    nums4 = [7, 4, 3, 2, 1, 6, 8]
    k4 = 3
    print(f"Test Case 4: {findMaxAverage(nums4, k4):.5f}")  # Expected Output: 6.33333

"""
Time Complexity:
- The binary search runs for O(log(max(nums) - min(nums)) / precision) iterations.
- For each iteration, the helper function `can_find_larger_average` runs in O(n) time.
- Therefore, the overall time complexity is O(n * log(max(nums) - min(nums)) / precision).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search, Prefix Sum
"""