"""
LeetCode Problem #2986: Problem Statement

You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subarray of size `k`.

A subarray is a contiguous part of an array. If the array has fewer than `k` elements, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

Write a function `maxSumSubarray(nums: List[int], k: int) -> int` that returns the maximum sum of a subarray of size `k`.
"""

from typing import List

def maxSumSubarray(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of a subarray of size k.

    Args:
    nums (List[int]): The list of integers.
    k (int): The size of the subarray.

    Returns:
    int: The maximum sum of a subarray of size k.
    """
    if len(nums) < k:
        return 0

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use sliding window to find the maximum sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(maxSumSubarray(nums1, k1))  # Expected Output: 9 (subarray [4, 5])

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(maxSumSubarray(nums2, k2))  # Expected Output: 9 (subarray [5, 1, 3])

    # Test Case 3
    nums3 = [4, -1, 2, 1, -7, 8, 3]
    k3 = 4
    print(maxSumSubarray(nums3, k3))  # Expected Output: 8 (subarray [2, 1, -7, 8])

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = 5
    print(maxSumSubarray(nums4, k4))  # Expected Output: 5 (subarray [1, 1, 1, 1, 1])

    # Test Case 5
    nums5 = [10, -10, 10, -10, 10]
    k5 = 1
    print(maxSumSubarray(nums5, k5))  # Expected Output: 10 (subarray [10])

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once to calculate the sum of the first window (O(k)).
- Then, it iterates through the rest of the array using a sliding window approach (O(n - k)).
- Overall, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (O(1)) for variables like `current_sum` and `max_sum`.
- Therefore, the space complexity is O(1).
"""

# Topic: Sliding Window