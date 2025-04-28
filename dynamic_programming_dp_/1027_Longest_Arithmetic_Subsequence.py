"""
LeetCode Problem #1027: Longest Arithmetic Subsequence

Problem Statement:
Given an array `nums` of integers, return the length of the longest arithmetic subsequence in `nums`.

Recall that a subsequence of an array is a list `nums[i1], nums[i2], ..., nums[ik]` with `0 <= i1 < i2 < ... < ik <= nums.length - 1`, and that a sequence `seq` is arithmetic if `seq[i+1] - seq[i]` are all the same value (for `0 <= i < seq.length - 1`).

Constraints:
- 2 <= nums.length <= 1000
- 0 <= nums[i] <= 500

Example 1:
Input: nums = [3, 6, 9, 12]
Output: 4
Explanation: The whole array is an arithmetic sequence with a common difference of 3.

Example 2:
Input: nums = [9, 4, 7, 2, 10]
Output: 3
Explanation: The longest arithmetic subsequence is [4, 7, 10].

Example 3:
Input: nums = [20, 1, 15, 3, 10, 5, 8]
Output: 4
Explanation: The longest arithmetic subsequence is [20, 15, 10, 5].

"""

def longestArithSeqLength(nums):
    """
    Function to find the length of the longest arithmetic subsequence in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest arithmetic subsequence.
    """
    n = len(nums)
    if n <= 1:
        return n

    # dp[i][diff] will store the length of the longest arithmetic subsequence
    # ending at index i with a common difference of `diff`.
    dp = [{} for _ in range(n)]
    max_length = 0

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            # If the difference `diff` exists in dp[j], extend the subsequence
            # Otherwise, start a new subsequence of length 2
            dp[i][diff] = dp[j].get(diff, 1) + 1
            max_length = max(max_length, dp[i][diff])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 6, 9, 12]
    print("Test Case 1 Output:", longestArithSeqLength(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [9, 4, 7, 2, 10]
    print("Test Case 2 Output:", longestArithSeqLength(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [20, 1, 15, 3, 10, 5, 8]
    print("Test Case 3 Output:", longestArithSeqLength(nums3))  # Expected Output: 4

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print("Test Case 4 Output:", longestArithSeqLength(nums4))  # Expected Output: 5

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print("Test Case 5 Output:", longestArithSeqLength(nums5))  # Expected Output: 4

"""
Time Complexity:
- The outer loop runs for each element in the array, i.e., O(n).
- The inner loop runs for all previous elements for each element, i.e., O(n).
- Inside the inner loop, dictionary operations (get and set) are O(1).
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- We use a list of dictionaries `dp` of size n, where each dictionary stores differences.
- In the worst case, each dictionary can store up to O(n) differences.
- Therefore, the space complexity is O(n^2).

Topic: Dynamic Programming (DP)
"""