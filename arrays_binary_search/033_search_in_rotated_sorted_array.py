"""
LeetCode Question #33: Search in Rotated Sorted Array

Problem Statement:
You are given an integer array `nums` sorted in ascending order (with distinct values), and an integer `target`.
The array is rotated at an unknown pivot index `k` (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
[0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array `nums` after the rotation and an integer `target`, return the index of `target` if it is in `nums`, 
or -1 if it is not in `nums`.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of `nums` are unique.
- `nums` is guaranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

def search(nums, target):
    """
    Searches for the target in a rotated sorted array using binary search.

    Args:
    nums (List[int]): Rotated sorted array.
    target (int): Target value to search for.

    Returns:
    int: Index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is the target
        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the left sorted portion
                right = mid - 1
            else:  # Target is in the right portion
                left = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right sorted portion
                left = mid + 1
            else:  # Target is in the left portion
                right = mid - 1

    return -1  # Target not found

# Example test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(search(nums1, target1))  # Output: 4

    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(search(nums2, target2))  # Output: -1

    # Test case 3
    nums3 = [1]
    target3 = 0
    print(search(nums3, target3))  # Output: -1

    # Test case 4
    nums4 = [6, 7, 8, 1, 2, 3, 4, 5]
    target4 = 3
    print(search(nums4, target4))  # Output: 5

    # Test case 5
    nums5 = [1, 3]
    target5 = 3
    print(search(nums5, target5))  # Output: 1

# Topic: Arrays, Binary Search