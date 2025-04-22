"""
LeetCode Problem #137: Single Number II

Problem Statement:
Given an integer array `nums` where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each element in nums appears exactly three times except for one element which appears once.
"""

# Solution
def singleNumber(nums):
    """
    Finds the single number in the array where every other number appears three times.

    Args:
    nums (List[int]): List of integers.

    Returns:
    int: The single number that appears exactly once.
    """
    # Initialize two variables to track bits appearing once and twice
    ones, twos = 0, 0

    for num in nums:
        # Update `ones` to include bits that appear once but not in `twos`
        ones = (ones ^ num) & ~twos
        # Update `twos` to include bits that appear twice but not in `ones`
        twos = (twos ^ num) & ~ones

    return ones

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 3, 2]
    print(singleNumber(nums1))  # Output: 3

    # Test Case 2
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    print(singleNumber(nums2))  # Output: 99

    # Test Case 3
    nums3 = [30000, 500, 100, 30000, 100, 30000, 100]
    print(singleNumber(nums3))  # Output: 500

    # Test Case 4
    nums4 = [-2, -2, -2, -3]
    print(singleNumber(nums4))  # Output: -3

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The algorithm uses only constant extra space (two integer variables `ones` and `twos`).
Thus, the space complexity is O(1).
"""

# Topic: Bit Manipulation