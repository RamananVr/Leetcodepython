"""
LeetCode Question #1143: Longest Common Subsequence

Problem Statement:
Given two strings `text1` and `text2`, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

For example:
- "ace" is a subsequence of "abcde".
- "aec" is not a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

# Solution
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Get the lengths of the two strings
    m, n = len(text1), len(text2)
    
    # Create a 2D DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The bottom-right cell contains the length of the LCS
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text1 = "abcde"
    text2 = "ace"
    print(longestCommonSubsequence(text1, text2))  # Output: 3

    # Test Case 2
    text1 = "abc"
    text2 = "abc"
    print(longestCommonSubsequence(text1, text2))  # Output: 3

    # Test Case 3
    text1 = "abc"
    text2 = "def"
    print(longestCommonSubsequence(text1, text2))  # Output: 0

    # Test Case 4
    text1 = "bl"
    text2 = "yby"
    print(longestCommonSubsequence(text1, text2))  # Output: 1

    # Test Case 5
    text1 = "abcdef"
    text2 = "badcfe"
    print(longestCommonSubsequence(text1, text2))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a nested loop to fill a DP table of size (m+1) x (n+1), where m is the length of `text1` and n is the length of `text2`.
- Each cell in the DP table is computed in constant time.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The solution uses a 2D DP table of size (m+1) x (n+1).
- Therefore, the space complexity is O(m * n).

Topic: Dynamic Programming (DP)
"""