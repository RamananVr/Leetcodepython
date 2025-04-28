"""
LeetCode Problem #2892: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Question #2892 does not exist. 
For the purpose of this task, I will create a hypothetical problem statement and provide a solution.)

Problem Statement:
You are given an integer array `nums` and an integer `k`. Your task is to find the maximum sum of any 
subarray of size `k`. If the array has fewer than `k` elements, return -1.

A subarray is a contiguous part of an array.

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Input: nums = [1, 2], k = 3
Output: -1
Explanation: The array has fewer than 3 elements, so the result is -1.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^5
"""

def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any subarray of size k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of the subarray.
    :return: int - The maximum sum of any subarray of size k, or -1 if the array has fewer than k elements.
    """
    # If the array has fewer than k elements, return -1
    if len(nums) < k:
        return -1

    # Initialize the sliding window sum and the maximum sum
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
    nums1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    print(max_sum_subarray(nums1, k1))  # Output: 9

    # Test Case 2
    nums2 = [1, 2]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Output: -1

    # Test Case 3
    nums3 = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k3 = 4
    print(max_sum_subarray(nums3, k3))  # Output: 18

    # Test Case 4
    nums4 = [5, 5, 5, 5, 5]
    k4 = 2
    print(max_sum_subarray(nums4, k4))  # Output: 10

    # Test Case 5
    nums5 = [10]
    k5 = 1
    print(max_sum_subarray(nums5, k5))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""