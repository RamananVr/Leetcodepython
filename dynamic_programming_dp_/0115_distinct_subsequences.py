"""
LeetCode Question #115: Distinct Subsequences

Problem Statement:
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
- rabbbit
- rabbbit
- rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
- babgbag
- babgbag
- babgbag
- babgbag
- babgbag

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
"""

# Clean, Correct Python Solution
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    # dp[i][j] represents the number of distinct subsequences of s[:i] that equals t[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: An empty t can be formed by any prefix of s in exactly one way (by deleting all characters)
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                # If characters match, we can either include this character or exclude it
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                # If characters don't match, we can only exclude the current character of s
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "rabbbit"
    t1 = "rabbit"
    print(f"numDistinct('{s1}', '{t1}') = {numDistinct(s1, t1)}")  # Output: 3

    # Test Case 2
    s2 = "babgbag"
    t2 = "bag"
    print(f"numDistinct('{s2}', '{t2}') = {numDistinct(s2, t2)}")  # Output: 5

    # Test Case 3
    s3 = "abc"
    t3 = "abc"
    print(f"numDistinct('{s3}', '{t3}') = {numDistinct(s3, t3)}")  # Output: 1

    # Test Case 4
    s4 = "abc"
    t4 = "d"
    print(f"numDistinct('{s4}', '{t4}') = {numDistinct(s4, t4)}")  # Output: 0

    # Test Case 5
    s5 = "aaaaa"
    t5 = "aa"
    print(f"numDistinct('{s5}', '{t5}') = {numDistinct(s5, t5)}")  # Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution involves filling up a 2D DP table of size (m+1) x (n+1), where m = len(s) and n = len(t).
- Each cell is computed in O(1) time.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) due to the 2D DP table.
- This can be optimized to O(n) by using a rolling array, but the current implementation uses O(m * n) space.
"""

# Topic: Dynamic Programming (DP)