"""
LeetCode Problem #1749: Maximum Absolute Sum of Any Subarray

Problem Statement:
You are given an integer array `nums`. The absolute sum of a subarray `[nums[l], nums[l+1], ..., nums[r-1], nums[r]]` 
is defined as `abs(nums[l] + nums[l+1] + ... + nums[r-1] + nums[r])`.

Return the maximum absolute sum of any (possibly empty) subarray of `nums`.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maxAbsoluteSum(nums):
    """
    This function calculates the maximum absolute sum of any subarray in the given array `nums`.
    """
    max_sum, min_sum = 0, 0
    current_max, current_min = 0, 0

    for num in nums:
        # Update the current maximum subarray sum
        current_max = max(0, current_max + num)
        max_sum = max(max_sum, current_max)

        # Update the current minimum subarray sum
        current_min = min(0, current_min + num)
        min_sum = min(min_sum, current_min)

    # The result is the maximum of the absolute values of max_sum and min_sum
    return max(max_sum, abs(min_sum))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, -3, 2, 3, -4]
    print(maxAbsoluteSum(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [2, -5, 1, -4, 3, -2]
    print(maxAbsoluteSum(nums2))  # Expected Output: 8

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(maxAbsoluteSum(nums3))  # Expected Output: 15

    # Test Case 4
    nums4 = [-1, -2, -3, -4, -5]
    print(maxAbsoluteSum(nums4))  # Expected Output: 15

    # Test Case 5
    nums5 = [0]
    print(maxAbsoluteSum(nums5))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (max_sum, min_sum, current_max, current_min).
- Therefore, the space complexity is O(1).

Topic: Arrays, Kadane's Algorithm
"""