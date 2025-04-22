"""
LeetCode Problem #44: Wildcard Matching

Problem Statement:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false

Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.
"""

# Solution
def isMatch(s: str, p: str) -> bool:
    # Dynamic Programming approach
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty string matches empty pattern

    # Handle patterns with '*' at the beginning
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any single character, or characters match
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, p1 = "aa", "a"
    print(isMatch(s1, p1))  # Output: False

    # Test Case 2
    s2, p2 = "aa", "*"
    print(isMatch(s2, p2))  # Output: True

    # Test Case 3
    s3, p3 = "cb", "?a"
    print(isMatch(s3, p3))  # Output: False

    # Test Case 4
    s4, p4 = "adceb", "*a*b"
    print(isMatch(s4, p4))  # Output: True

    # Test Case 5
    s5, p5 = "acdcb", "a*c?b"
    print(isMatch(s5, p5))  # Output: False

# Topic: Dynamic Programming (DP)