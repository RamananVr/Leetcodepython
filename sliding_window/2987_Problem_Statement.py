"""
LeetCode Problem #2987: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2987 does not exist. 
For the purpose of this task, I will create a fictional problem statement and solve it.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of length `k`.

Write a function `max_sum_of_subarray(nums: List[int], k: int) -> int` that returns the maximum sum of any subarray of length `k`. 
If the array has fewer than `k` elements, return 0.

Constraints:
- 1 <= k <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List

def max_sum_of_subarray(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of any subarray of length k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The length of the subarray.

    Returns:
    int: The maximum sum of any subarray of length k.
    """
    if len(nums) < k:
        return 0

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use sliding window to calculate the sum of subsequent windows
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_of_subarray(nums1, k1))  # Expected Output: 9 (subarray [4, 5])

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_of_subarray(nums2, k2))  # Expected Output: 9 (subarray [5, 1, 3])

    # Test Case 3
    nums3 = [4, -1, 2, 1, -7, 8, 3]
    k3 = 4
    print(max_sum_of_subarray(nums3, k3))  # Expected Output: 12 (subarray [2, 1, -7, 8])

    # Test Case 4
    nums4 = [1, 2, 3]
    k4 = 4
    print(max_sum_of_subarray(nums4, k4))  # Expected Output: 0 (array length < k)

    # Test Case 5
    nums5 = [-1, -2, -3, -4]
    k5 = 2
    print(max_sum_of_subarray(nums5, k5))  # Expected Output: -3 (subarray [-1, -2])

"""
Time Complexity Analysis:
- Calculating the sum of the first window takes O(k).
- Sliding the window across the array takes O(n - k), where n is the length of the array.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Sliding Window
"""