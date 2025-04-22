"""
LeetCode Question #10: Regular Expression Matching

Problem Statement:
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example:
- Input: s = "aa", p = "a*"
- Output: True
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it matches the entire string.

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.

Write a function:
```python
def isMatch(s: str, p: str) -> bool:
```
that returns whether `s` matches the pattern `p`.
"""

def isMatch(s: str, p: str) -> bool:
    """
    Dynamic Programming solution for Regular Expression Matching.
    """
    # Create a DP table where dp[i][j] represents whether s[:i] matches p[:j].
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty string matches empty pattern.
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc., that can match an empty string.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the DP table.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                # If characters match or pattern has '.', carry forward the result.
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero or more of the preceding element.
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Exact match
    s1, p1 = "aa", "a*"
    print(isMatch(s1, p1))  # Expected: True

    # Test Case 2: Match with '.'
    s2, p2 = "ab", ".*"
    print(isMatch(s2, p2))  # Expected: True

    # Test Case 3: No match
    s3, p3 = "mississippi", "mis*is*p*."
    print(isMatch(s3, p3))  # Expected: False

    # Test Case 4: Match with empty string
    s4, p4 = "", "a*"
    print(isMatch(s4, p4))  # Expected: True

    # Test Case 5: Complex pattern
    s5, p5 = "aab", "c*a*b"
    print(isMatch(s5, p5))  # Expected: True

"""
Topic: Dynamic Programming
"""