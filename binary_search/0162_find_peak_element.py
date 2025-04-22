"""
LeetCode Question #162: Find Peak Element

Problem Statement:
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = -∞` and `nums[n] = -∞` for the purpose of comparison.

You must write an algorithm that runs in O(log n) time.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- `nums[i] != nums[i + 1]` for all valid `i`.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and its index is 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 1 where the peak element is 2, or index 5 where the peak element is 6.

Follow-up:
Could you implement a solution with O(log n) complexity?
"""

def findPeakElement(nums):
    """
    Finds a peak element in the array and returns its index.

    :param nums: List[int] - The input array
    :return: int - Index of a peak element
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        # Compare mid with its neighbor
        if nums[mid] > nums[mid + 1]:
            # Peak is on the left side (including mid)
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(findPeakElement(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums2))  # Output: 5

    # Test Case 3
    nums3 = [1]
    print(findPeakElement(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2]
    print(findPeakElement(nums4))  # Output: 1

    # Test Case 5
    nums5 = [2, 1]
    print(findPeakElement(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm uses binary search, which divides the search space in half at each step.
Thus, the time complexity is O(log n), where n is the length of the input array.

Space Complexity:
The algorithm uses a constant amount of space for variables (left, right, mid).
Thus, the space complexity is O(1).

Topic: Binary Search
"""