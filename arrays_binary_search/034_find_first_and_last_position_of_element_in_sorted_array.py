"""
LeetCode Question #34: Find First and Last Position of Element in Sorted Array

Problem Statement:
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`
"""

def searchRange(nums, target):
    """
    Finds the first and last position of the target in a sorted array.

    Args:
    nums (List[int]): A list of integers sorted in non-decreasing order.
    target (int): The target value to search for.

    Returns:
    List[int]: A list containing the starting and ending positions of the target, or [-1, -1] if the target is not found.
    """
    def binarySearch(left):
        """Helper function to perform binary search."""
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target or (left and nums[mid] == target):
                low = mid + 1
            else:
                high = mid
        return low

    start = binarySearch(True)
    end = binarySearch(False) - 1

    if start <= end and end < len(nums) and nums[start] == target and nums[end] == target:
        return [start, end]
    return [-1, -1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(searchRange(nums1, target1))  # Output: [3, 4]

    # Test Case 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(searchRange(nums2, target2))  # Output: [-1, -1]

    # Test Case 3
    nums3 = []
    target3 = 0
    print(searchRange(nums3, target3))  # Output: [-1, -1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target4 = 5
    print(searchRange(nums4, target4))  # Output: [4, 4]

    # Test Case 5
    nums5 = [2, 2, 2, 2, 2]
    target5 = 2
    print(searchRange(nums5, target5))  # Output: [0, 4]

# Topic: Arrays, Binary Search