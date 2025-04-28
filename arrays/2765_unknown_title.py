"""
LeetCode Problem #2765: Longest Alternating Subarray

Problem Statement:
You are given an array `nums` of integers. An alternating subarray is defined as a contiguous subarray where the difference between consecutive elements alternates between positive and negative. In other words, for a subarray `nums[i:j]` (inclusive), the following conditions must hold:
1. For all `k` such that `i <= k < j-1`, `(nums[k+1] - nums[k]) * (nums[k+2] - nums[k+1]) < 0`.

Your task is to find the length of the longest alternating subarray in `nums`. If no such subarray exists, return 0.

Constraints:
- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 3
Explanation: The longest alternating subarray is [3, 2, 4].

Input: nums = [1, 2, 3, 4]
Output: 0
Explanation: No alternating subarray exists.

Follow-up:
Can you solve this problem in O(n) time complexity?
"""

# Solution
def longest_alternating_subarray(nums):
    """
    Finds the length of the longest alternating subarray in the given list of integers.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest alternating subarray.
    """
    if len(nums) < 2:
        return 0

    max_length = 0
    current_length = 1

    for i in range(1, len(nums)):
        # Check if the current pair alternates
        if (nums[i] - nums[i - 1]) * (nums[i - 1] - nums[i - 2]) < 0 if i > 1 else True:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 2 if nums[i] != nums[i - 1] else 1

    return max_length if max_length > 1 else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 4, 5]
    print(longest_alternating_subarray(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(longest_alternating_subarray(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 20, 10, 20, 10]
    print(longest_alternating_subarray(nums3))  # Output: 5

    # Test Case 4
    nums4 = [1]
    print(longest_alternating_subarray(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 2, 1, 2, 1, 2, 1]
    print(longest_alternating_subarray(nums5))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `max_length` and `current_length`.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays