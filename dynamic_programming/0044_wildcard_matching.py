"""
LeetCode Question #44: Wildcard Matching

Problem Statement:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

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
Explanation: '?' matches 'c', but 'a' does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The pattern '*a*b' matches 'adceb'.

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
    """
    Dynamic Programming solution for wildcard matching.
    """
    # Initialize DP table
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Fill in the first row for patterns with leading '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any single character or exact match
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

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming table of size (m+1) x (n+1), where m is the length of the string `s` and n is the length of the pattern `p`.
- Filling each cell in the table takes constant time, so the overall time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) due to the DP table.

Topic: Dynamic Programming
"""