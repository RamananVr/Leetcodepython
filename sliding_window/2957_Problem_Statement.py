"""
LeetCode Problem #2957: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2957 does not exist. 
For the purpose of this task, I will create a hypothetical problem statement and solution.)

Problem Statement:
You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of size `k`.

Write a function `max_sum_subarray(nums: List[int], k: int) -> int` that returns the maximum sum of any subarray of size `k`. 
If the array has fewer than `k` elements, return 0.

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
    int: The maximum sum of any subarray of size k.
    """
    if len(nums) < k:
        return 0

    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_subarray(nums1, k1))  # Expected Output: 9 (subarray [4, 5])

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Expected Output: 9 (subarray [5, 1, 3])

    # Test Case 3
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    print(max_sum_subarray(nums3, k3))  # Expected Output: -3 (subarray [-1, -2])

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 1
    print(max_sum_subarray(nums4, k4))  # Expected Output: 50 (subarray [50])

    # Test Case 5
    nums5 = [1, 2, 3]
    k5 = 4
    print(max_sum_subarray(nums5, k5))  # Expected Output: 0 (array has fewer than k elements)

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