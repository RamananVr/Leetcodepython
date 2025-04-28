"""
LeetCode Question #2893: Full Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of length `k` in the list. A subarray is a contiguous part of the array.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= k <= len(nums)
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.

Input: nums = [2, 3], k = 2
Output: 5
Explanation: The subarray [2, 3] has the maximum sum of 5.

Your task is to implement a function that solves this problem efficiently.
"""

# Solution
def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any subarray of length k.

    :param nums: List[int] - The list of integers.
    :param k: int - The length of the subarray.
    :return: int - The maximum sum of any subarray of length k.
    """
    # Edge case: If k is greater than the length of nums, return 0
    if k > len(nums):
        return 0

    # Initialize the sum of the first window and the maximum sum
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use the sliding window technique to calculate the sum of subarrays
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k1 = 4
    print(max_sum_subarray(nums1, k1))  # Expected Output: 39

    # Test Case 2
    nums2 = [2, 3]
    k2 = 2
    print(max_sum_subarray(nums2, k2))  # Expected Output: 5

    # Test Case 3
    nums3 = [5, -1, 3, 2, 8, -2, 4]
    k3 = 3
    print(max_sum_subarray(nums3, k3))  # Expected Output: 13

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = 2
    print(max_sum_subarray(nums4, k4))  # Expected Output: 2

    # Test Case 5
    nums5 = [-1, -2, -3, -4, -5]
    k5 = 2
    print(max_sum_subarray(nums5, k5))  # Expected Output: -3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses the sliding window technique, which involves iterating through the array once.
- Calculating the sum of the first window takes O(k), and sliding the window across the array takes O(n - k).
- Overall, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a constant amount of extra space (variables like `current_sum` and `max_sum`).
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""