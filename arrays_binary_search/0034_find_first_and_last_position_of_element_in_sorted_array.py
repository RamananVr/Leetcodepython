"""
LeetCode Question #34: Find First and Last Position of Element in Sorted Array

Problem Statement:
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

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

    :param nums: List[int] - The sorted array of integers.
    :param target: int - The target value to find.
    :return: List[int] - The starting and ending positions of the target, or [-1, -1] if not found.
    """
    def findBound(isFirst):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if isFirst:
                    right = mid - 1  # Narrow down to the left half
                else:
                    left = mid + 1  # Narrow down to the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    # Find the first and last positions using binary search
    first = findBound(isFirst=True)
    if first == -1:  # If the target is not found, return [-1, -1]
        return [-1, -1]
    last = findBound(isFirst=False)
    return [first, last]

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
    nums4 = [1, 2, 3, 4, 5, 5, 5, 6, 7]
    target4 = 5
    print(searchRange(nums4, target4))  # Output: [4, 6]

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    target5 = 1
    print(searchRange(nums5, target5))  # Output: [0, 4]

"""
Time Complexity:
- The `findBound` function performs a binary search, which has a time complexity of O(log n).
- Since we call `findBound` twice (once for the first position and once for the last position), the overall time complexity is O(log n).

Space Complexity:
- The algorithm uses O(1) additional space since it only uses a few variables for computation.

Topic: Arrays, Binary Search
"""