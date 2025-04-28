"""
LeetCode Problem #540: Single Element in a Sorted Array

Problem Statement:
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Your solution must run in O(log n) time and use O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- nums is sorted in non-decreasing order.
"""

def singleNonDuplicate(nums):
    """
    Finds the single element in a sorted array where every other element appears twice.

    :param nums: List[int] - A sorted list of integers
    :return: int - The single element that appears only once
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is even or odd and adjust the comparison accordingly
        if mid % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            if nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid

    return nums[left]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(singleNonDuplicate(nums1))  # Output: 2

    # Test Case 2
    nums2 = [3, 3, 7, 7, 10, 11, 11]
    print(singleNonDuplicate(nums2))  # Output: 10

    # Test Case 3
    nums3 = [1, 1, 2]
    print(singleNonDuplicate(nums3))  # Output: 2

    # Test Case 4
    nums4 = [0, 1, 1]
    print(singleNonDuplicate(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1]
    print(singleNonDuplicate(nums5))  # Output: 1

"""
Time Complexity Analysis:
The algorithm uses binary search, which divides the search space in half at each step. 
Thus, the time complexity is O(log n), where n is the length of the input array.

Space Complexity Analysis:
The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Binary Search
"""