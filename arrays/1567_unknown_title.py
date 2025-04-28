"""
LeetCode Problem #1567: Maximum Length of Subarray With Positive Product

Problem Statement:
Given an array of integers `nums`, find the maximum length of a subarray where the product of all its elements is positive.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array [1,-2,-3,4] has a positive product of 24.

Example 2:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The array [-2,-3,-4] has a positive product of -24.
Note that the subarray [1] has a positive product, but its length is only 1.

Example 3:
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The array [-1,-2] has a positive product of 2.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

# Python Solution
def getMaxLen(nums):
    """
    Function to find the maximum length of a subarray with a positive product.

    :param nums: List[int] - Input array of integers
    :return: int - Maximum length of subarray with positive product
    """
    max_len = 0
    positive_len = 0
    negative_len = 0

    for num in nums:
        if num == 0:
            positive_len = 0
            negative_len = 0
        elif num > 0:
            positive_len += 1
            negative_len = negative_len + 1 if negative_len > 0 else 0
        else:  # num < 0
            temp = positive_len
            positive_len = negative_len + 1 if negative_len > 0 else 0
            negative_len = temp + 1
        max_len = max(max_len, positive_len)

    return max_len

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, -2, -3, 4]
    print(getMaxLen(nums1))  # Output: 4

    # Test Case 2
    nums2 = [0, 1, -2, -3, -4]
    print(getMaxLen(nums2))  # Output: 3

    # Test Case 3
    nums3 = [-1, -2, -3, 0, 1]
    print(getMaxLen(nums3))  # Output: 2

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(getMaxLen(nums4))  # Output: 4

    # Test Case 5
    nums5 = [0, 0, 0]
    print(getMaxLen(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The algorithm uses a constant amount of extra space to store variables like `positive_len`, `negative_len`, and `max_len`.
Thus, the space complexity is O(1).
"""

# Topic: Arrays