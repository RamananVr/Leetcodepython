"""
LeetCode Problem #896: Monotonic Array

Problem Statement:
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

# Solution
def isMonotonic(nums):
    """
    Determines if the given array is monotonic.

    :param nums: List[int] - The input array
    :return: bool - True if the array is monotonic, False otherwise
    """
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Monotone increasing
    nums1 = [1, 2, 2, 3]
    print(isMonotonic(nums1))  # Expected output: True

    # Test Case 2: Monotone decreasing
    nums2 = [6, 5, 4, 4]
    print(isMonotonic(nums2))  # Expected output: True

    # Test Case 3: Not monotonic
    nums3 = [1, 3, 2]
    print(isMonotonic(nums3))  # Expected output: False

    # Test Case 4: Single element array
    nums4 = [1]
    print(isMonotonic(nums4))  # Expected output: True

    # Test Case 5: All elements are the same
    nums5 = [5, 5, 5, 5]
    print(isMonotonic(nums5))  # Expected output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the array once, performing constant-time comparisons at each step.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The function uses a constant amount of extra space (two boolean variables: `increasing` and `decreasing`).
Thus, the space complexity is O(1).
"""

# Topic: Arrays