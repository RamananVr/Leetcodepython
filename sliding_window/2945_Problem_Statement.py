"""
LeetCode Problem #2945: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2945 does not exist. 
For the sake of this exercise, I will create a hypothetical problem statement.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subarray of size `k`.

A subarray is a contiguous part of an array. If the array has fewer than `k` elements, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Example:
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.
"""

# Python Solution
def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of a subarray of size k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of the subarray.
    :return: int - The maximum sum of a subarray of size k.
    """
    if len(nums) < k:
        return 0

    # Calculate the sum of the first window of size k
    window_sum = sum(nums[:k])
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
    print(max_sum_subarray(nums1, k1))  # Output: 39

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Output: 9

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1, 1]
    k3 = 2
    print(max_sum_subarray(nums3, k3))  # Output: 2

    # Test Case 4
    nums4 = [5, -1, -2, 10, 3]
    k4 = 2
    print(max_sum_subarray(nums4, k4))  # Output: 11

    # Test Case 5
    nums5 = [1]
    k5 = 1
    print(max_sum_subarray(nums5, k5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).
"""

# Topic: Sliding Window