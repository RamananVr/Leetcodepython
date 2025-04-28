"""
LeetCode Problem #2924: Problem Statement

You are given a 0-indexed integer array `nums` of length `n`. The array is circular, meaning the first element is adjacent to the last element. A subarray of `nums` is a contiguous segment of the array.

Your task is to find the maximum possible sum of a subarray of `nums` that is circular. In other words, the subarray can wrap around the end of the array and continue at the beginning.

Return the maximum possible sum of a circular subarray.

Constraints:
- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

Example:
Input: nums = [1, -2, 3, -2]
Output: 3
Explanation: Subarray [3] has the maximum sum of 3.

Input: nums = [5, -3, 5]
Output: 10
Explanation: Subarray [5, 5] has the maximum sum of 10.

Input: nums = [-3, -2, -3]
Output: -2
Explanation: Subarray [-2] has the maximum sum of -2.
"""

# Solution
def maxSubarraySumCircular(nums):
    """
    Function to find the maximum sum of a circular subarray.

    :param nums: List[int] - The input array
    :return: int - The maximum sum of a circular subarray
    """
    def kadane(arr):
        """Helper function to find the maximum subarray sum using Kadane's algorithm."""
        max_ending_here = max_so_far = arr[0]
        for num in arr[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Case 1: Maximum subarray sum without wrapping
    max_kadane = kadane(nums)

    # Case 2: Maximum subarray sum with wrapping
    total_sum = sum(nums)
    # Invert the array to find the minimum subarray sum
    inverted_nums = [-num for num in nums]
    max_wrap = total_sum + kadane(inverted_nums)  # Equivalent to total_sum - min_subarray_sum

    # If all numbers are negative, max_wrap will be 0, so we return max_kadane
    if max_wrap == 0:
        return max_kadane

    # Return the maximum of the two cases
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
    nums4 = [8, -1, -3, 8]
    print(maxSubarraySumCircular(nums4))  # Output: 16

    # Test Case 5
    nums5 = [10, -10, 10, -10, 10]
    print(maxSubarraySumCircular(nums5))  # Output: 30

# Time and Space Complexity Analysis
"""
Time Complexity:
- The Kadane's algorithm runs in O(n) time.
- We run Kadane's algorithm twice: once for the normal array and once for the inverted array.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.
"""

# Topic: Arrays