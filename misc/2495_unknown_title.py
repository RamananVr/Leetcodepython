"""
LeetCode Problem #2495: Number of Subarrays Having Even Product

Problem Statement:
Given an integer array `nums`, return the number of contiguous subarrays where the product of all the elements in the subarray is even.

A product is even if at least one of the numbers in the subarray is even.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def numOfSubarraysWithEvenProduct(nums):
    """
    Function to calculate the number of subarrays with an even product.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The number of subarrays with an even product.
    """
    n = len(nums)
    count_even = 0
    count_odd = 0
    result = 0

    for num in nums:
        if num % 2 == 0:  # If the current number is even
            count_even += 1
            result+=