"""
LeetCode Problem #918: Maximum Sum Circular Subarray

Problem Statement:
Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array wraps around to the beginning. Formally, the next element of `nums[n-1]` is `nums[0]`, and the previous element of `nums[0]` is `nums[n-1]`.

A subarray may only include each element of the fixed buffer `nums` at most once. For example, for `nums = [1,2,3,4]`, the subarray `[3,4,1]` is a valid subarray, but `[3,4,1,2]` is not valid.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- -10^4 <= nums[i] <= 10^4
"""

# Solution
def maxSubarraySumCircular(nums):
    """
    Finds the maximum sum of a circular subarray in the given array.

    :param nums: List[int] - The input array
    :return: int - The maximum sum of a circular subarray
    """
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Case 1: Maximum sum subarray without wrapping
    max_kadane = kadane(nums)

    # Case 2: Maximum sum subarray with wrapping
    total_sum = sum(nums)
    # Invert the array to find the minimum subarray sum
    inverted_nums = [-num for num in nums]
    max_inverted_kadane = kadane(inverted_nums)
    max_wrap = total_sum + max_inverted_kadane  # Equivalent to total_sum - min_subarray_sum

    # If all elements are negative, max_wrap will be 0, so we return max_kadane
    if max_wrap == 0:
        return max_kadane

    return max(max_kadane, max_wrap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, -2, 3, -2]
    print(maxSubarraySumCircular(nums1))  # Output: 3

    # Test Case 2
    nums2 = [5, -3, 5]
    print(maxSubarraySumCircular(nums2))  # Output: 10

    # Test Case 3
    nums3 = [-3, -2, -3]
    print(maxSubarraySumCircular(nums3))  # Output: -2

    # Test Case 4
    nums4 = [10, -10, 10, -10, 10]
    print(maxSubarraySumCircular(nums4))  # Output: 30

    # Test Case 5
    nums5 = [8, -1, -3, 8]
    print(maxSubarraySumCircular(nums5))  # Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- The Kadane's algorithm runs in O(n) time, and we use it twice (once for the normal array and once for the inverted array).
- Summing the array also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- We use O(n) space for the inverted array, but this can be optimized to O(1) by modifying the array in-place.
- Overall space complexity: O(n) (or O(1) if optimized).

Topic: Arrays, Dynamic Programming
"""