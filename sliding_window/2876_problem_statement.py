"""
LeetCode Question #2876: Problem Statement

You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of size `k`.

A subarray is a contiguous part of the array. If the array has fewer than `k` elements, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Example:
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.

Input: nums = [2, 3], k = 3
Output: 0
Explanation: The array has fewer than `k` elements, so the result is 0.
"""

# Python Solution
def max_sum_subarray_of_size_k(nums, k):
    """
    Finds the maximum sum of any subarray of size k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of the subarray.
    :return: int - The maximum sum of any subarray of size k, or 0 if the array has fewer than k elements.
    """
    if len(nums) < k:
        return 0

    # Initialize the sum of the first window and the maximum sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k1 = 4
    print(max_sum_subarray_of_size_k(nums1, k1))  # Output: 39

    # Test Case 2
    nums2 = [2, 3]
    k2 = 3
    print(max_sum_subarray_of_size_k(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [5, -1, 3, 2, 8, 6, -2, 4]
    k3 = 3
    print(max_sum_subarray_of_size_k(nums3, k3))  # Output: 16

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 2
    print(max_sum_subarray_of_size_k(nums4, k4))  # Output: 90

    # Test Case 5
    nums5 = [-5, -2, -1, -8, -3]
    k5 = 2
    print(max_sum_subarray_of_size_k(nums5, k5))  # Output: -3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, sliding the window across the array.
- Calculating the sum of the first window takes O(k), and sliding the window takes O(n - k).
- Overall, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (window_sum, max_sum).
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""