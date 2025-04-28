"""
LeetCode Question #2973: Full Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of size `k`.

A subarray is a contiguous part of the array. You need to return the maximum sum of all subarrays of size `k`.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= k <= len(nums)
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.

Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Input: nums = [1, 1, 1, 1, 1, 1], k = 2
Output: 2
Explanation: The subarray [1, 1] has the maximum sum of 2.
"""

# Python Solution
def max_sum_subarray_of_size_k(nums, k):
    """
    Finds the maximum sum of any subarray of size k.

    :param nums: List[int] - List of integers
    :param k: int - Size of the subarray
    :return: int - Maximum sum of any subarray of size k
    """
    # Edge case: If k is greater than the length of nums, return 0
    if k > len(nums):
        return 0

    # Initialize the window sum and the maximum sum
    window_sum = sum(nums[:k])  # Sum of the first k elements
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Update the window sum by adding the next element and removing the first element of the previous window
        window_sum += nums[i] - nums[i - k]
        # Update the maximum sum
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k1 = 4
    print(max_sum_subarray_of_size_k(nums1, k1))  # Output: 39

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_subarray_of_size_k(nums2, k2))  # Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1, 1]
    k3 = 2
    print(max_sum_subarray_of_size_k(nums3, k3))  # Output: 2

    # Test Case 4 (Edge Case: k equals the length of nums)
    nums4 = [5, 5, 5, 5]
    k4 = 4
    print(max_sum_subarray_of_size_k(nums4, k4))  # Output: 20

    # Test Case 5 (Edge Case: Negative numbers)
    nums5 = [-1, -2, -3, -4, -5]
    k5 = 2
    print(max_sum_subarray_of_size_k(nums5, k5))  # Output: -3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach, where we iterate through the array once.
- Calculating the initial sum of the first k elements takes O(k).
- Sliding the window across the array takes O(n - k), where n is the length of nums.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (window_sum, max_sum).
- No additional data structures are used.
- Overall space complexity: O(1).
"""

# Topic: Sliding Window