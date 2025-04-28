"""
LeetCode Problem #2952: Problem Statement

Given a list of integers `nums` and an integer `k`, your task is to find the maximum sum of any subarray of size `k`.

A subarray is a contiguous part of an array. If the array has fewer than `k` elements, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Example:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 9
Explanation: The subarray [4, 5] has the maximum sum of 9.
"""

# Python Solution
def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any subarray of size k.

    :param nums: List[int] - The input list of integers.
    :param k: int - The size of the subarray.
    :return: int - The maximum sum of any subarray of size k.
    """
    if len(nums) < k:
        return 0

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use a sliding window to calculate the sum of subarrays of size k
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_subarray(nums1, k1))  # Output: 9

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Output: 9

    # Test Case 3
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    print(max_sum_subarray(nums3, k3))  # Output: -3

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 1
    print(max_sum_subarray(nums4, k4))  # Output: 50

    # Test Case 5
    nums5 = [1, 2, 3]
    k5 = 4
    print(max_sum_subarray(nums5, k5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).
"""

# Topic: Sliding Window