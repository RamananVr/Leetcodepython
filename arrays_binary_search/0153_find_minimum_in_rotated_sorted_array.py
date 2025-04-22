"""
LeetCode Question #153: Find Minimum in Rotated Sorted Array

Problem Statement:
Suppose an array of length `n` sorted in ascending order is rotated at some pivot unknown to you beforehand 
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given the rotated sorted array `nums` of unique elements, and you must return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is guaranteed to be rotated at some pivot.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated at index 3.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] rotated at index 4.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and was not rotated.

Follow-up:
Can you solve the problem in O(log n) time?
"""

# Python Solution
def findMin(nums):
    """
    Finds the minimum element in a rotated sorted array.

    :param nums: List[int] - Rotated sorted array
    :return: int - Minimum element in the array
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If mid element is greater than the rightmost element, the minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is in the left half (including mid)
            right = mid

    # At the end of the loop, left == right and points to the minimum element
    return nums[left]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 5, 1, 2]
    print(findMin(nums1))  # Output: 1

    # Test Case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(nums2))  # Output: 0

    # Test Case 3
    nums3 = [11, 13, 15, 17]
    print(findMin(nums3))  # Output: 11

    # Test Case 4
    nums4 = [2, 1]
    print(findMin(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1]
    print(findMin(nums5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm uses binary search, which divides the search space in half at each step. 
Thus, the time complexity is O(log n), where n is the length of the input array.

Space Complexity:
The algorithm uses a constant amount of extra space (two pointers: left and right). 
Thus, the space complexity is O(1).
"""

# Topic: Arrays, Binary Search