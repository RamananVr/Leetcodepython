"""
LeetCode Problem #2401: Longest Nice Subarray

Problem Statement:
You are given an array `nums` consisting of positive integers.

We call a subarray of `nums` nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [8,48,10]. 
- The bitwise AND of 8 and 48 is 0.
- The bitwise AND of 8 and 10 is 0.
- The bitwise AND of 48 and 10 is 0.
No longer subarray of length 4 or more is nice.

Example 2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The subarray [3] is the longest nice subarray, as the bitwise AND of any two elements is not 0.
Hence, the answer is 1.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def longestNiceSubarray(nums):
    """
    Finds the length of the longest nice subarray.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The length of the longest nice subarray.
    """
    n = len(nums)
    max_length = 0
    current_and = 0
    left = 0

    for right in range(n):
        # Add the current number to the AND mask
        while (current_and & nums[right]) != 0:
            # If there's a conflict, remove the leftmost number
            current_and ^= nums[left]
            left += 1
        # Add the current number to the AND mask
        current_and |= nums[right]
        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 8, 48, 10]
    print(longestNiceSubarray(nums1))  # Output: 3

    # Test Case 2
    nums2 = [3, 1, 5, 11, 13]
    print(longestNiceSubarray(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 4, 8, 16]
    print(longestNiceSubarray(nums3))  # Output: 5

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(longestNiceSubarray(nums4))  # Output: 2

    # Test Case 5
    nums5 = [0]
    print(longestNiceSubarray(nums5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach. Each element is added to or removed from the AND mask at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables like `current_and`, `left`, and `right`.
- Therefore, the space complexity is O(1).

Topic: Sliding Window, Bit Manipulation
"""