"""
LeetCode Problem #2683: Neighboring Bitwise XOR

Problem Statement:
You are given a 0-indexed integer array nums. Find the maximum value of nums[i] XOR nums[i + 1] for all 0 <= i < nums.length - 1.

Return the maximum value.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: 7
Explanation: The maximum value is obtained when nums[2] XOR nums[3] = 3 XOR 4 = 7.

Example 2:
Input: nums = [0, 1, 2, 3]
Output: 3
Explanation: The maximum value is obtained when nums[2] XOR nums[3] = 2 XOR 3 = 3.

Constraints:
- 2 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

# Python Solution
def maximum_xor(nums):
    """
    Finds the maximum value of nums[i] XOR nums[i + 1] for all 0 <= i < nums.length - 1.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum XOR value.
    """
    max_xor = 0
    for i in range(len(nums) - 1):
        max_xor = max(max_xor, nums[i] ^ nums[i + 1])
    return max_xor

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(maximum_xor(nums1))  # Output: 7

    # Test Case 2
    nums2 = [0, 1, 2, 3]
    print(maximum_xor(nums2))  # Output: 3

    # Test Case 3
    nums3 = [5, 10, 15, 20]
    print(maximum_xor(nums3))  # Output: 25

    # Test Case 4
    nums4 = [8, 1, 2, 12]
    print(maximum_xor(nums4))  # Output: 14

    # Test Case 5
    nums5 = [0, 0, 0, 0]
    print(maximum_xor(nums5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the array once, performing a constant-time XOR operation and comparison for each pair of neighboring elements.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The function uses a constant amount of extra space to store the max_xor variable and loop index.
Thus, the space complexity is O(1).
"""

# Topic: Bit Manipulation