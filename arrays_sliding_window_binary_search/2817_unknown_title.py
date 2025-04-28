"""
LeetCode Problem #2817: Minimum Absolute Difference Between Elements With Constraint

Problem Statement:
You are given an integer array `nums` and an integer `x`. Find the minimum absolute difference 
between two elements in the array such that their indices differ by at least `x`.

In other words, find the minimum value of `|nums[i] - nums[j]|` where `|i - j| >= x` and `0 <= i, j < len(nums)`.

Return the minimum absolute difference found.

Example 1:
Input: nums = [4, 3, 2, 4], x = 2
Output: 0
Explanation: We can select nums[0] = 4 and nums[3] = 4. Their absolute difference is |4 - 4| = 0, 
and their indices differ by 3 >= 2.

Example 2:
Input: nums = [5, 3, 2, 10, 15], x = 1
Output: 1
Explanation: The minimum absolute difference is |3 - 2| = 1, with indices 1 and 2.

Example 3:
Input: nums = [1, 2, 3, 4], x = 3
Output: 3
Explanation: The minimum absolute difference is |1 - 4| = 3, with indices 0 and 3.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= x < nums.length
"""

from sortedcontainers import SortedList

def min_absolute_difference(nums, x):
    """
    Finds the minimum absolute difference between two elements in the array such that their indices differ by at least x.

    :param nums: List[int] - The input array of integers.
    :param x: int - The minimum index difference constraint.
    :return: int - The minimum absolute difference satisfying the constraint.
    """
    sorted_list = SortedList()
    min_diff = float('inf')

    for i in range(x, len(nums)):
        # Add the element nums[i - x] to the sorted list
        sorted_list.add(nums[i - x])

        # Find the closest elements to nums[i] in the sorted list
        pos = sorted_list.bisect_left(nums[i])

        # Check the element at pos (if it exists)
        if pos < len(sorted_list):
            min_diff = min(min_diff, abs(nums[i] - sorted_list[pos]))

        # Check the element at pos - 1 (if it exists)
        if pos > 0:
            min_diff = min(min_diff, abs(nums[i] - sorted_list[pos - 1]))

    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 4]
    x1 = 2
    print(min_absolute_difference(nums1, x1))  # Output: 0

    # Test Case 2
    nums2 = [5, 3, 2, 10, 15]
    x2 = 1
    print(min_absolute_difference(nums2, x2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    x3 = 3
    print(min_absolute_difference(nums3, x3))  # Output: 3

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    x4 = 2
    print(min_absolute_difference(nums4, x4))  # Output: 10

    # Test Case 5
    nums5 = [1, 1000000000]
    x5 = 1
    print(min_absolute_difference(nums5, x5))  # Output: 999999999

"""
Time Complexity:
- The loop iterates through the array once, so it runs in O(n).
- For each iteration, adding to the SortedList and finding the closest elements both take O(log(x)).
- Since x < n, the overall time complexity is O(n * log(x)).

Space Complexity:
- The SortedList stores up to x elements, so the space complexity is O(x).

Topic: Arrays, Sliding Window, Binary Search
"""