"""
LeetCode Problem #2954: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2954 does not exist. 
For the purpose of this task, I will create a hypothetical problem statement, solution, and analysis.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of 
any subarray of size `k`. If the array has fewer than `k` elements, return -1.

Write a function `max_sum_subarray(nums: List[int], k: int) -> int` that returns the maximum sum of 
any subarray of size `k`.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Example 1:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 9
Explanation: The subarray [4, 5] has the maximum sum of 9.

Example 2:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 6
Explanation: The subarray [5, -2, 3] has the maximum sum of 6.

Example 3:
Input: nums = [2, 1], k = 3
Output: -1
Explanation: The array has fewer than 3 elements, so the result is -1.
"""

from typing import List

def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of size k.
    If the array has fewer than k elements, returns -1.
    """
    n = len(nums)
    if n < k:
        return -1

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window across the array
    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_subarray(nums1, k1))  # Output: 9

    # Test Case 2
    nums2 = [1, -1, 5, -2, 3]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Output: 6

    # Test Case 3
    nums3 = [2, 1]
    k3 = 3
    print(max_sum_subarray(nums3, k3))  # Output: -1

    # Test Case 4
    nums4 = [-1, -2, -3, -4, -5]
    k4 = 2
    print(max_sum_subarray(nums4, k4))  # Output: -3

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    k5 = 5
    print(max_sum_subarray(nums5, k5))  # Output: 150

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where we iterate through the array once.
- Calculating the sum of the first window takes O(k), and sliding the window across the array takes O(n - k).
- Overall time complexity: O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Sliding Window
"""