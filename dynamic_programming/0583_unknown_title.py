"""
LeetCode Problem #583: Delete Operation for Two Strings

Problem Statement:
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.
"""

def minDistance(word1: str, word2: str) -> int:
    """
    This function calculates the minimum number of steps required to make two strings the same
    by deleting characters from either string.
    """
    # Find the length of the longest common subsequence (LCS)
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The minimum number of deletions is the total length of both strings
    # minus twice the length of the LCS
    lcs_length = dp[m][n]
    return (m - lcs_length) + (n - lcs_length)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "sea"
    word2 = "eat"
    print(f"Input: word1 = {word1}, word2 = {word2}")
    print(f"Output: {minDistance(word1, word2)}")  # Expected Output: 2

    # Test Case 2
    word1 = "leetcode"
    word2 = "etco"
    print(f"Input: word1 = {word1}, word2 = {word2}")
    print(f"Output: {minDistance(word1, word2)}")  # Expected Output: 4

    # Test Case 3
    word1 = "abc"
    word2 = "def"
    print(f"Input: word1 = {word1}, word2 = {word2}")
    print(f"Output: {minDistance(word1, word2)}")  # Expected Output: 6

    # Test Case 4
    word1 = "a"
    word2 = "a"
    print(f"Input: word1 = {word1}, word2 = {word2}")
    print(f"Output: {minDistance(word1, word2)}")  # Expected Output: 0

"""
Time Complexity:
- The solution uses a dynamic programming table of size (m+1) x (n+1), where m and n are the lengths of word1 and word2.
- Filling the table requires O(m * n) time, as we iterate through all cells.

Space Complexity:
- The space complexity is O(m * n) due to the dp table.

Topic: Dynamic Programming
"""