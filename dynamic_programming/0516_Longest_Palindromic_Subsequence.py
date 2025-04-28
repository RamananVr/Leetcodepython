"""
LeetCode Problem #516: Longest Palindromic Subsequence

Problem Statement:
Given a string `s`, find the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""

# Solution
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    # dp[i][j] will store the length of the longest palindromic subsequence in s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single character substrings are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the dp table for substrings of length 2 to n
    for length in range(2, n + 1):  # length is the length of the substring
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the substring
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is the length of the longest palindromic subsequence in the entire string
    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bbbab"
    print(f"Input: {s1}, Output: {longestPalindromeSubseq(s1)}")  # Expected: 4

    # Test Case 2
    s2 = "cbbd"
    print(f"Input: {s2}, Output: {longestPalindromeSubseq(s2)}")  # Expected: 2

    # Test Case 3
    s3 = "a"
    print(f"Input: {s3}, Output: {longestPalindromeSubseq(s3)}")  # Expected: 1

    # Test Case 4
    s4 = "abcde"
    print(f"Input: {s4}, Output: {longestPalindromeSubseq(s4)}")  # Expected: 1

    # Test Case 5
    s5 = "agbdba"
    print(f"Input: {s5}, Output: {longestPalindromeSubseq(s5)}")  # Expected: 5

# Time and Space Complexity Analysis
# Time Complexity: O(n^2)
# - The outer loop iterates over substring lengths (from 2 to n), and the inner loop iterates over all possible starting indices for substrings of that length.
# - Filling each dp[i][j] takes O(1) time, so the total time complexity is O(n^2).

# Space Complexity: O(n^2)
# - We use a 2D dp table of size n x n to store the results of subproblems.

# Topic: Dynamic Programming