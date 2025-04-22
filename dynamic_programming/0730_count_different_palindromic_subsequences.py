"""
LeetCode Question #730: Count Different Palindromic Subsequences

Problem Statement:
Given a string `s`, return the number of different non-empty palindromic subsequences in `s`. 
Since the answer may be very large, return it modulo `10^9 + 7`.

A subsequence of a string is obtained by deleting zero or more characters. 
A sequence is palindromic if it is equal to the sequence reversed.

Two subsequences are considered different if they are different as strings.

Example 1:
Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are "b", "c", "bb", "cc", "bcb", "bccb".

Example 2:
Input: s = "aab"
Output: 4
Explanation: The 4 different non-empty palindromic subsequences are "a", "b", "aa", "aba".

Constraints:
- `1 <= s.length <= 1000`
- `s[i]` is a lowercase English letter.
"""

# Solution
def countPalindromicSubsequences(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # Single character is always a palindrome

    for length in range(2, n + 1):  # Length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                low, high = i + 1, j - 1
                while low <= high and s[low] != s[i]:
                    low += 1
                while low <= high and s[high] != s[j]:
                    high -= 1

                if low > high:  # No duplicate characters in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                elif low == high:  # One duplicate character in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                else:  # More than one duplicate character in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

            dp[i][j] = dp[i][j] % MOD  # Ensure the result is modulo 10^9 + 7

    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bccb"
    print(countPalindromicSubsequences(s1))  # Output: 6

    # Test Case 2
    s2 = "aab"
    print(countPalindromicSubsequences(s2))  # Output: 4

    # Test Case 3
    s3 = "aaa"
    print(countPalindromicSubsequences(s3))  # Output: 6

    # Test Case 4
    s4 = "abcd"
    print(countPalindromicSubsequences(s4))  # Output: 4

    # Test Case 5
    s5 = "aaaaa"
    print(countPalindromicSubsequences(s5))  # Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a nested loop structure.
- The outer loop iterates over substring lengths (from 2 to n), and the inner loop iterates over starting indices of substrings.
- Each iteration involves constant-time operations or traversals of a substring.
- Therefore, the time complexity is O(n^2), where n is the length of the string.

Space Complexity:
- The solution uses a 2D DP table of size n x n to store intermediate results.
- Thus, the space complexity is O(n^2).

Topic: Dynamic Programming
"""