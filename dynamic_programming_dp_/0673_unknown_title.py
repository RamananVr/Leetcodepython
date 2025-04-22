"""
LeetCode Problem #673: Number of Longest Increasing Subsequence

Problem Statement:
Given an integer array `nums`, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 5, 7] and [1, 3, 4, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 subsequences of length 1.

Constraints:
- 1 <= nums.length <= 2000
- -10^6 <= nums[i] <= 10^6
"""

def findNumberOfLIS(nums):
    """
    Function to find the number of longest increasing subsequences in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of longest increasing subsequences.
    """
    n = len(nums)
    if n <= 1:
        return n

    # Initialize dp arrays
    lengths = [1] * n  # lengths[i] = length of the LIS ending at index i
    counts = [1] * n   # counts[i] = number of LIS ending at index i

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]

    # Find the length of the longest increasing subsequence
    max_length = max(lengths)

    # Count the number of subsequences with the maximum length
    return sum(c for l, c in zip(lengths, counts) if l == max_length)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 4, 7]
    print(findNumberOfLIS(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    print(findNumberOfLIS(nums2))  # Output: 5

    # Test Case 3
    nums3 = [1, 2, 4, 3, 5, 4, 7, 2]
    print(findNumberOfLIS(nums3))  # Output: 3

    # Test Case 4
    nums4 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(findNumberOfLIS(nums4))  # Output: 1

"""
Time Complexity Analysis:
- The outer loop runs for `n` iterations, where `n` is the length of the input array.
- The inner loop runs for up to `i` iterations for each `i` in the outer loop.
- Thus, the total time complexity is O(n^2).

Space Complexity Analysis:
- We use two arrays, `lengths` and `counts`, each of size `n`.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""