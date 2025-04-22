"""
LeetCode Question #41: First Missing Positive

Problem Statement:
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
- 1 <= nums.length <= 5 * 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""

def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an unsorted array.

    :param nums: List[int] - The input array of integers.
    :return: int - The smallest missing positive integer.
    """
    n = len(nums)
    
    # Step 1: Replace all non-positive numbers and numbers greater than n with a placeholder (n + 1)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Use the array itself to mark the presence of numbers
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first index with a positive value
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If all indices are marked, the missing number is n + 1
    return n + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 0]
    print(firstMissingPositive(nums1))  # Output: 3

    # Test Case 2
    nums2 = [3, 4, -1, 1]
    print(firstMissingPositive(nums2))  # Output: 2

    # Test Case 3
    nums3 = [7, 8, 9, 11, 12]
    print(firstMissingPositive(nums3))  # Output: 1

    # Test Case 4
    nums4 = [2, 1]
    print(firstMissingPositive(nums4))  # Output: 3

    # Test Case 5
    nums5 = [1]
    print(firstMissingPositive(nums5))  # Output: 2

# Topic: Arrays