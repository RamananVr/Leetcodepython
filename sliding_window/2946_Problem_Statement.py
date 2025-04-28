"""
LeetCode Problem #2946: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2946 does not exist. 
For the purpose of this task, I will create a fictional problem statement and solution.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of 
any subarray of size `k`. If the array has fewer than `k` elements, return -1.

Write a function `max_sum_subarray(nums: List[int], k: int) -> int` that returns the maximum sum of 
any subarray of size `k`.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)
"""

from typing import List

def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of size k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the subarray.

    Returns:
    int: The maximum sum of any subarray of size k, or -1 if the array has fewer than k elements.
    """
    if len(nums) < k:
        return -1

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use a sliding window to calculate the sum of subarrays of size k
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_subarray(nums1, k1))  # Expected Output: 9 (subarray [4, 5])

    # Test Case 2: Array with negative numbers
    nums2 = [-1, -2, -3, -4, -5]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Expected Output: -6 (subarray [-1, -2, -3])

    # Test Case 3: Single element subarray
    nums3 = [10, 20, 30, 40, 50]
    k3 = 1
    print(max_sum_subarray(nums3, k3))  # Expected Output: 50 (subarray [50])

    # Test Case 4: Array with fewer elements than k
    nums4 = [1, 2]
    k4 = 3
    print(max_sum_subarray(nums4, k4))  # Expected Output: -1

    # Test Case 5: Large array
    nums5 = [i for i in range(1, 10001)]  # Array from 1 to 10000
    k5 = 100
    print(max_sum_subarray(nums5, k5))  # Expected Output: 995050 (subarray [9901, ..., 10000])

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a sliding window approach, which involves iterating through the array once.
- Calculating the sum of the first window takes O(k), and updating the sum for the remaining windows takes O(n - k).
- Overall time complexity: O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space, as it only maintains variables for the current sum and maximum sum.
- Overall space complexity: O(1).

Topic: Sliding Window
"""