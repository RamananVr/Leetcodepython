"""
LeetCode Question #33: Search in Rotated Sorted Array

Problem Statement:
You are given an integer array `nums` sorted in ascending order (with distinct values), and an integer `target`.

Suppose that `nums` is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are tasked to search for `target` in `nums`. If `target` exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of `nums` are unique.
- `nums` is guaranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4
"""

def search(nums, target):
    """
    Searches for the target in a rotated sorted array using binary search.

    Args:
    nums (List[int]): The rotated sorted array.
    target (int): The target value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the mid element is the target
        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the left sorted part
                right = mid - 1
            else:  # Target is in the right part
                left = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right sorted part
                left = mid + 1
            else:  # Target is in the left part
                right = mid - 1

    # Target not found
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target is in the array
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(search(nums1, target1))  # Output: 4

    # Test Case 2: Target is not in the array
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(search(nums2, target2))  # Output: -1

    # Test Case 3: Array with one element, target is present
    nums3 = [1]
    target3 = 1
    print(search(nums3, target3))  # Output: 0

    # Test Case 4: Array with one element, target is absent
    nums4 = [1]
    target4 = 0
    print(search(nums4, target4))  # Output: -1

    # Test Case 5: Target is in the rotated part
    nums5 = [6, 7, 8, 1, 2, 3, 4, 5]
    target5 = 3
    print(search(nums5, target5))  # Output: 5

"""
Time Complexity:
- The algorithm uses binary search, which divides the search space in half at each step.
- Therefore, the time complexity is O(log n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few variables for indices and comparisons).
- Therefore, the space complexity is O(1).

Topic: Arrays, Binary Search
"""