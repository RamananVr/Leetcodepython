"""
LeetCode Problem #2932: Maximum Difference Between Increasing Elements

Problem Statement:
You are given a 0-indexed integer array nums of size n.

The maximum difference of nums is the maximum value of nums[j] - nums[i] over all 0 <= i < j < n, such that nums[j] > nums[i].
If no such i and j exist, return -1.

Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that nums[j] > nums[i].

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that nums[j] > nums[i].

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

Constraints:
- n == nums.length
- 2 <= n <= 1000
- 1 <= nums[i] <= 10^9
"""

# Python Solution
def maximumDifference(nums):
    """
    Finds the maximum difference between increasing elements in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum difference or -1 if no valid pair exists.
    """
    min_value = nums[0]
    max_diff = -1

    for i in range(1, len(nums)):
        if nums[i] > min_value:
            max_diff = max(max_diff, nums[i] - min_value)
        else:
            min_value = nums[i]

    return max_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 1, 5, 4]
    print(maximumDifference(nums1))  # Output: 4

    # Test Case 2
    nums2 = [9, 4, 3, 2]
    print(maximumDifference(nums2))  # Output: -1

    # Test Case 3
    nums3 = [1, 5, 2, 10]
    print(maximumDifference(nums3))  # Output: 9

    # Additional Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(maximumDifference(nums4))  # Output: 4

    # Additional Test Case 5
    nums5 = [10, 8, 6, 4, 2]
    print(maximumDifference(nums5))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, making it O(n), where n is the length of the array.

Space Complexity:
The algorithm uses a constant amount of extra space, making it O(1).
"""

# Topic: Arrays