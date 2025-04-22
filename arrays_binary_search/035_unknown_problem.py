"""
LeetCode Problem #35: Search Insert Position

Problem Statement:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""

def searchInsert(nums, target):
    """
    Finds the index of the target in a sorted array or the index where it should be inserted.

    Args:
    nums (List[int]): A sorted list of distinct integers.
    target (int): The target value to search for.

    Returns:
    int: The index of the target or the index where it should be inserted.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(searchInsert(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(searchInsert(nums2, target2))  # Output: 1

    # Test Case 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(searchInsert(nums3, target3))  # Output: 4

    # Test Case 4
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(searchInsert(nums4, target4))  # Output: 0

    # Test Case 5
    nums5 = [1]
    target5 = 1
    print(searchInsert(nums5, target5))  # Output: 0

# Topic: Arrays, Binary Search