"""
LeetCode Question #81: Search in Rotated Sorted Array II

Problem Statement:
There is an integer array `nums` sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, `nums` is rotated at an unknown pivot index `k` (0 <= k < nums.length) 
such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` 
(0-indexed). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index 5 and become 
`[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` after the rotation and an integer `target`, return `true` if `target` is in `nums`, 
or `false` if it is not in `nums`.

You must decrease the overall operation complexity compared to a linear search.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is guaranteed to be rotated at least once.
- -10^4 <= target <= 10^4
"""

# Clean, Correct Python Solution
def search(nums, target):
    """
    Searches for the target in a rotated sorted array that may contain duplicates.

    Args:
    nums (List[int]): Rotated sorted array.
    target (int): Target value to search for.

    Returns:
    bool: True if target is found, False otherwise.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return True

        # Handle duplicates: skip duplicates on the left and right
        while left < mid and nums[left] == nums[mid]:
            left += 1
        while right > mid and nums[right] == nums[mid]:
            right -= 1

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

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 6, 0, 0, 1, 2]
    target1 = 0
    print(search(nums1, target1))  # Output: True

    # Test Case 2
    nums2 = [2, 5, 6, 0, 0, 1, 2]
    target2 = 3
    print(search(nums2, target2))  # Output: False

    # Test Case 3
    nums3 = [1, 0, 1, 1, 1]
    target3 = 0
    print(search(nums3, target3))  # Output: True

    # Test Case 4
    nums4 = [1, 3, 1, 1, 1]
    target4 = 3
    print(search(nums4, target4))  # Output: True

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    target5 = 2
    print(search(nums5, target5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- In the worst case, the algorithm may need to skip over duplicate elements, which can degrade the performance to O(n).
- In the average case, the binary search approach ensures a time complexity of O(log n).

Space Complexity:
- The algorithm uses constant space, so the space complexity is O(1).

Overall, the time complexity is O(n) in the worst case and O(log n) in the average case, while the space complexity is O(1).
"""

# Topic: Arrays, Binary Search