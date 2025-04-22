"""
LeetCode Problem #413: Arithmetic Slices

Problem Statement:
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example:
- [1, 3, 5, 7, 9], the difference between consecutive elements is 2, so the array is arithmetic.
- [7, 7, 7, 7], the difference between consecutive elements is 0, so the array is arithmetic.

A subarray is any contiguous part of an array. A subarray is called an arithmetic slice if it is an arithmetic array.

Given an integer array `nums`, return the number of arithmetic subarrays of `nums`.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: 3
Explanation: The 3 arithmetic slices are [1, 2, 3], [2, 3, 4], and [1, 2, 3, 4] itself.

Example 2:
Input: nums = [1]
Output: 0

Constraints:
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
"""

def numberOfArithmeticSlices(nums):
    """
    Function to calculate the number of arithmetic slices in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of arithmetic slices.
    """
    n = len(nums)
    if n < 3:
        return 0

    count = 0
    current = 0

    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            current += 1
            count += current
        else:
            current = 0

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1}, Output: {numberOfArithmeticSlices(nums1)}")  # Expected Output: 3

    # Test Case 2
    nums2 = [1]
    print(f"Input: {nums2}, Output: {numberOfArithmeticSlices(nums2)}")  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 3, 5, 7, 9]
    print(f"Input: {nums3}, Output: {numberOfArithmeticSlices(nums3)}")  # Expected Output: 6

    # Test Case 4
    nums4 = [7, 7, 7, 7]
    print(f"Input: {nums4}, Output: {numberOfArithmeticSlices(nums4)}")  # Expected Output: 3

    # Test Case 5
    nums5 = [1, 2, 3, 8, 9, 10]
    print(f"Input: {nums5}, Output: {numberOfArithmeticSlices(nums5)}")  # Expected Output: 2

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables like `count` and `current`.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""