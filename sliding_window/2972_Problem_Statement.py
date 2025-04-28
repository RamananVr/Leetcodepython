"""
LeetCode Problem #2972: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2972 does not exist. 
For the purpose of this task, I will create a fictional problem statement and solve it.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of size `k`.

Write a function `max_sum_subarray(nums: List[int], k: int) -> int` that returns the maximum sum of any subarray of size `k`.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Example:
Input: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.

Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Follow-up:
Can you solve this problem in O(n) time complexity?
"""

from typing import List

def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of size k using a sliding window approach.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the subarray.

    Returns:
    int: The maximum sum of any subarray of size k.
    """
    # Initialize the sum of the first window and the maximum sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Update the window sum by adding the next element and removing the first element of the previous window
        window_sum += nums[i] - nums[i - k]
        # Update the maximum sum if the current window sum is greater
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
    nums3 = [5, -1, -2, 10, 3, 7, -5, 6]
    k3 = 2
    print(max_sum_subarray(nums3, k3))  # Output: 13

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1, 1]
    k4 = 3
    print(max_sum_subarray(nums4, k4))  # Output: 3

    # Test Case 5
    nums5 = [-1, -2, -3, -4, -5]
    k5 = 2
    print(max_sum_subarray(nums5, k5))  # Output: -3

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where we iterate through the array once.
- Calculating the sum of the first window takes O(k), and sliding the window across the array takes O(n - k).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Overall space complexity: O(1).

Topic: Sliding Window
"""