"""
LeetCode Question #2896: Problem Statement

Problem Title: "Find the Longest Subarray with Sum Divisible by K"

Given an integer array `nums` and an integer `k`, return the length of the longest subarray whose sum is divisible by `k`.

A subarray is a contiguous part of the array.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4

Example:
Input: nums = [2, -2, 2, -4], k = 6
Output: 4
Explanation: The entire array has a sum of 2 + (-2) + 2 + (-4) = -2, which is divisible by 6.

Input: nums = [1, 2, 3], k = 3
Output: 3
Explanation: The entire array has a sum of 1 + 2 + 3 = 6, which is divisible by 3.

Input: nums = [1, 2, 3], k = 5
Output: 0
Explanation: No subarray has a sum divisible by 5.
"""

def longest_subarray_divisible_by_k(nums, k):
    """
    Finds the length of the longest subarray whose sum is divisible by k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The divisor.
    :return: int - The length of the longest subarray.
    """
    remainder_map = {0: -1}  # Maps remainder to the earliest index where it occurs
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k

        # Handle negative remainders to ensure they are in the range [0, k-1]
        if remainder < 0:
            remainder += k

        if remainder in remainder_map:
            # Calculate the length of the subarray
            max_length = max(max_length, i - remainder_map[remainder])
        else:
            # Store the first occurrence of this remainder
            remainder_map[remainder] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, -2, 2, -4]
    k1 = 6
    print(longest_subarray_divisible_by_k(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [1, 2, 3]
    k2 = 3
    print(longest_subarray_divisible_by_k(nums2, k2))  # Output: 3

    # Test Case 3
    nums3 = [1, 2, 3]
    k3 = 5
    print(longest_subarray_divisible_by_k(nums3, k3))  # Output: 0

    # Test Case 4
    nums4 = [4, 5, 0, -2, -3, 1]
    k4 = 5
    print(longest_subarray_divisible_by_k(nums4, k4))  # Output: 5

    # Test Case 5
    nums5 = [7, 4, -10, 2, 3]
    k5 = 5
    print(longest_subarray_divisible_by_k(nums5, k5))  # Output: 4

"""
Time Complexity:
- O(n), where n is the length of the input array `nums`.
  We iterate through the array once, and all operations (e.g., dictionary lookups) are O(1).

Space Complexity:
- O(k), where k is the divisor.
  In the worst case, the `remainder_map` dictionary can store up to `k` unique remainders.

Topic: Hash Table, Prefix Sum
"""