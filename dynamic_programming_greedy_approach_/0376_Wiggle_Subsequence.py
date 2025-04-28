"""
LeetCode Problem #376: Wiggle Subsequence

Problem Statement:
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example:
- [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
- [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array `nums`, return the length of the longest wiggle subsequence of `nums`.

Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

def wiggleMaxLength(nums):
    """
    Function to find the length of the longest wiggle subsequence.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest wiggle subsequence.
    """
    if len(nums) < 2:
        return len(nums)
    
    # Initialize counters for up and down sequences
    up = 1
    down = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    
    return max(up, down)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 7, 4, 9, 2, 5]
    print(wiggleMaxLength(nums1))  # Output: 6

    # Test Case 2
    nums2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    print(wiggleMaxLength(nums2))  # Output: 7

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(wiggleMaxLength(nums3))  # Output: 2

    # Test Case 4
    nums4 = [0]
    print(wiggleMaxLength(nums4))  # Output: 1

    # Test Case 5
    nums5 = [3, 3, 3, 2, 5]
    print(wiggleMaxLength(nums5))  # Output: 3

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (two variables: `up` and `down`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (Greedy Approach)
"""