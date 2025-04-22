"""
LeetCode Question #10: Regular Expression Matching

Problem Statement:
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `.` and `*`.

"""

# Solution
def isMatch(s: str, p: str) -> bool:
    """
    Dynamic Programming solution for regular expression matching.
    """
    # Create a DP table where dp[i][j] represents whether s[:i] matches p[:j]
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns with '*' that can match zero preceding elements
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                # Characters match or '.' matches any character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero or more of the preceding element
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, p1 = "aa", "a"
    print(isMatch(s1, p1))  # Output: False

    # Test Case 2
    s2, p2 = "aa", "a*"
    print(isMatch(s2, p2))  # Output: True

    # Test Case 3
    s3, p3 = "ab", ".*"
    print(isMatch(s3, p3))  # Output: True

    # Test Case 4
    s4, p4 = "aab", "c*a*b"
    print(isMatch(s4, p4))  # Output: True

    # Test Case 5
    s5, p5 = "mississippi", "mis*is*p*."
    print(isMatch(s5, p5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution uses a 2D DP table of size (m+1) x (n+1), where m is the length of the string `s` and n is the length of the pattern `p`.
- Each cell in the table is computed in O(1) time.
- Therefore, the overall time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) due to the DP table.

In practice, the space complexity can be optimized to O(n) by using a rolling array, but the current implementation uses the full DP table.
"""

# Topic: Dynamic Programming