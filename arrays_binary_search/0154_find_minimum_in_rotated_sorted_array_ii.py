"""
LeetCode Question #154: Find Minimum in Rotated Sorted Array II

Problem Statement:
Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. 
For example, the array nums = [0,1,4,4,5,6,7] might become:
- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 0 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is sorted and rotated between 1 and n times.

Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0

Follow up:
This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. 
Would this affect the runtime complexity? How and why?
"""

# Python Solution
def findMin(nums):
    """
    Finds the minimum element in a rotated sorted array that may contain duplicates.

    :param nums: List[int] - The rotated sorted array
    :return: int - The minimum element in the array
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare mid with the rightmost element
        if nums[mid] > nums[right]:
            # Minimum must be in the right half
            left = mid + 1
        elif nums[mid] < nums[right]:
            # Minimum must be in the left half
            right = mid
        else:
            # nums[mid] == nums[right], reduce the search space
            right -= 1

    return nums[left]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5]
    print(findMin(nums1))  # Output: 1

    # Test Case 2
    nums2 = [2, 2, 2, 0, 1]
    print(findMin(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 1, 10, 10, 10]
    print(findMin(nums3))  # Output: 1

    # Test Case 4
    nums4 = [3, 3, 3, 3, 3, 1, 3]
    print(findMin(nums4))  # Output: 1

    # Test Case 5
    nums5 = [2, 2, 2, 2, 2]
    print(findMin(nums5))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- In the worst case, where all elements are duplicates except one, the algorithm may need to reduce the search space one element at a time.
- This results in O(n) time complexity in the worst case.
- In the average case, the algorithm performs binary search, resulting in O(log n) time complexity.

Space Complexity:
- The algorithm uses constant space, so the space complexity is O(1).

Topic: Arrays, Binary Search
"""