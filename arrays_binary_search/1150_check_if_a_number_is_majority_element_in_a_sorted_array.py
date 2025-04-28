"""
LeetCode Question #1150: Check If a Number Is Majority Element in a Sorted Array

Problem Statement:
Given an integer array `nums` sorted in non-decreasing order and an integer `target`, 
return `true` if `target` is a majority element, or `false` otherwise.

A majority element in an array is an element that appears more than `n / 2` times in the array, 
where `n` is the size of the array.

Example 1:
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the size of the array is 9. 
Thus, 5 is a majority element because 5 > 9/2 is true.

Example 2:
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: The value 101 appears 2 times and the size of the array is 4. 
Thus, 101 is not a majority element because 2 > 4/2 is false.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
- nums is sorted in non-decreasing order.
- 1 <= target <= 10^9
"""

# Solution
from bisect import bisect_left, bisect_right

def isMajorityElement(nums, target):
    """
    Determines if the target is a majority element in the sorted array nums.

    Args:
    nums (List[int]): A sorted list of integers.
    target (int): The integer to check for majority element status.

    Returns:
    bool: True if target is a majority element, False otherwise.
    """
    n = len(nums)
    # Find the first and last occurrence of target using binary search
    left = bisect_left(nums, target)
    right = bisect_right(nums, target)
    
    # Count the occurrences of target
    count = right - left
    
    # Check if count is greater than n / 2
    return count > n // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 5, 5, 5, 5, 5, 6, 6]
    target1 = 5
    print(isMajorityElement(nums1, target1))  # Output: True

    # Test Case 2
    nums2 = [10, 100, 101, 101]
    target2 = 101
    print(isMajorityElement(nums2, target2))  # Output: False

    # Test Case 3
    nums3 = [1, 1, 1, 2, 2, 2, 2]
    target3 = 2
    print(isMajorityElement(nums3, target3))  # Output: False

    # Test Case 4
    nums4 = [1, 1, 1, 1, 2, 2, 2]
    target4 = 1
    print(isMajorityElement(nums4, target4))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The bisect_left and bisect_right functions each run in O(log n) time, where n is the length of the array.
- Calculating the count and comparing it to n / 2 is O(1).
- Overall, the time complexity is O(log n).

Space Complexity:
- The algorithm uses O(1) additional space since no extra data structures are used.
- The space complexity is O(1).
"""

# Topic: Arrays, Binary Search