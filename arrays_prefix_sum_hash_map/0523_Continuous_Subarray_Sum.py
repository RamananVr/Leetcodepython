"""
LeetCode Problem #523: Continuous Subarray Sum

Problem Statement:
Given an integer array `nums` and an integer `k`, return `true` if `nums` has a continuous subarray of size at least two 
whose elements sum up to a multiple of `k`, or `false` otherwise.

A continuous subarray is a subarray that can be obtained by deleting some elements (possibly none) from the beginning 
and some elements (possibly none) from the end of the array.

An integer `x` is a multiple of `k` if `x = n * k` where `n` is an integer.

You may assume that the input array contains at least two elements.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= k <= 2^31 - 1
"""

# Solution
def checkSubarraySum(nums, k):
    """
    Determines if the array contains a continuous subarray of size at least two
    whose sum is a multiple of k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The integer to check multiples of.
    :return: bool - True if such a subarray exists, False otherwise.
    """
    # Dictionary to store remainder and its index
    remainder_map = {0: -1}  # Initialize with remainder 0 at index -1
    cumulative_sum = 0

    for i, num in enumerate(nums):
        cumulative_sum += num
        if k != 0:  # Avoid division by zero
            remainder = cumulative_sum % k
        else:
            remainder = cumulative_sum

        # If the remainder has been seen before
        if remainder in remainder_map:
            # Check if the subarray size is at least 2
            if i - remainder_map[remainder] > 1:
                return True
        else:
            # Store the first occurrence of this remainder
            remainder_map[remainder] = i

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Subarray exists
    nums1 = [23, 2, 4, 6, 7]
    k1 = 6
    print(checkSubarraySum(nums1, k1))  # Expected output: True

    # Test Case 2: Subarray does not exist
    nums2 = [23, 2, 6, 4, 7]
    k2 = 13
    print(checkSubarraySum(nums2, k2))  # Expected output: False

    # Test Case 3: k is zero
    nums3 = [0, 0]
    k3 = 0
    print(checkSubarraySum(nums3, k3))  # Expected output: True

    # Test Case 4: Large k value
    nums4 = [1, 2, 3]
    k4 = 5
    print(checkSubarraySum(nums4, k4))  # Expected output: False

    # Test Case 5: Subarray with multiple of k
    nums5 = [5, 0, 0, 0]
    k5 = 5
    print(checkSubarraySum(nums5, k5))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(min(n, k)) due to the storage of remainders in the dictionary. In the worst case, 
  the dictionary could store all unique remainders modulo k.
- If k = 0, the dictionary size is bounded by the number of elements in the array, so the space complexity is O(n).
"""

# Topic: Arrays, Prefix Sum, Hash Map