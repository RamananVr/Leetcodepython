"""
LeetCode Problem #97: Interleaving String

Problem Statement:
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s1 and s2 is a string that contains all characters of s1 and s2 and preserves the order of characters from each string.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""

# Solution
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # If the lengths don't match, return False immediately
    if len(s1) + len(s2) != len(s3):
        return False

    # Initialize a DP table
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Base case: empty s1 and s2 can interleave to form empty s3
    dp[0][0] = True

    # Fill the DP table
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # Check if the current character of s3 matches with s1[i-1]
            if i > 0 and s3[i + j - 1] == s1[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            # Check if the current character of s3 matches with s2[j-1]
            if j > 0 and s3[i + j - 1] == s2[j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]

    return dp[len(s1)][len(s2)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1, s2, s3))  # Output: True

    # Test Case 2
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(isInterleave(s1, s2, s3))  # Output: False

    # Test Case 3
    s1 = ""
    s2 = ""
    s3 = ""
    print(isInterleave(s1, s2, s3))  # Output: True

    # Test Case 4
    s1 = "abc"
    s2 = "def"
    s3 = "adbcef"
    print(isInterleave(s1, s2, s3))  # Output: True

    # Test Case 5
    s1 = "abc"
    s2 = "def"
    s3 = "abdecf"
    print(isInterleave(s1, s2, s3))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a nested loop to fill a DP table of size (len(s1) + 1) x (len(s2) + 1).
- Therefore, the time complexity is O(len(s1) * len(s2)).

Space Complexity:
- The solution uses a DP table of size (len(s1) + 1) x (len(s2) + 1).
- Therefore, the space complexity is O(len(s1) * len(s2)).
- Note: The follow-up asks for O(s2.length) space, which can be achieved by optimizing the DP table to use a single row.

Topic: Dynamic Programming (DP)
"""