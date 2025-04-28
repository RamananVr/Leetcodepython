"""
LeetCode Problem #2239: Find Closest Number to Zero

Problem Statement:
Given an integer array `nums` of size `n`, return the number in the array that is closest to zero.
If there are multiple answers, return the number with the larger value.

Example 1:
Input: nums = [-4, -2, 1, 4, 8]
Output: 1
Explanation: 1 is closest to zero.

Example 2:
Input: nums = [2, -1, 1]
Output: 1
Explanation: Both 1 and -1 are equally close to zero, but 1 is larger.

Constraints:
- 1 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
"""

# Python Solution
def findClosestNumber(nums):
    """
    Finds the number in the array closest to zero. If there are multiple numbers equally close,
    returns the larger number.

    :param nums: List[int] - List of integers
    :return: int - Number closest to zero
    """
    closest = nums[0]
    for num in nums:
        # Compare absolute values, and if equal, choose the larger number
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-4, -2, 1, 4, 8]
    print(findClosestNumber(nums1))  # Output: 1

    # Test Case 2
    nums2 = [2, -1, 1]
    print(findClosestNumber(nums2))  # Output: 1

    # Test Case 3
    nums3 = [-10, -5, 5, 10]
    print(findClosestNumber(nums3))  # Output: 5

    # Test Case 4
    nums4 = [0, -1, 1]
    print(findClosestNumber(nums4))  # Output: 0

    # Test Case 5
    nums5 = [-100000, 100000]
    print(findClosestNumber(nums5))  # Output: 100000

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the list of numbers once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the input list `nums`.

Space Complexity:
The function uses a constant amount of extra space to store the variable `closest`.
Thus, the space complexity is O(1).
"""

# Topic: Arrays