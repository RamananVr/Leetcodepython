"""
LeetCode Problem #1092: Shortest Common Supersequence

Problem Statement:
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. 
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters (possibly zero) from t 
results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
"cabac" is the shortest string that has both "abac" and "cab" as subsequences.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of lowercase English letters.
"""

# Python Solution
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    # Helper function to find the Longest Common Subsequence (LCS)
    def find_lcs(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        
        return dp[m][n]

    # Find the LCS of str1 and str2
    lcs = find_lcs(str1, str2)
    
    # Build the shortest common supersequence using the LCS
    i, j = 0, 0
    result = []
    
    for char in lcs:
        # Add characters from str1 that are not part of the LCS
        while i < len(str1) and str1[i] != char:
            result.append(str1[i])
            i += 1
        # Add characters from str2 that are not part of the LCS
        while j < len(str2) and str2[j] != char:
            result.append(str2[j])
            j += 1
        # Add the current character from the LCS
        result.append(char)
        i += 1
        j += 1
    
    # Add remaining characters from str1 and str2
    result.extend(str1[i:])
    result.extend(str2[j:])
    
    return "".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    str1 = "abac"
    str2 = "cab"
    print(shortestCommonSupersequence(str1, str2))  # Output: "cabac"

    # Test Case 2
    str1 = "aaaaaaaa"
    str2 = "aaaaaaaa"
    print(shortestCommonSupersequence(str1, str2))  # Output: "aaaaaaaa"

    # Test Case 3
    str1 = "abc"
    str2 = "def"
    print(shortestCommonSupersequence(str1, str2))  # Output: "abcdef"

    # Test Case 4
    str1 = "geek"
    str2 = "eke"
    print(shortestCommonSupersequence(str1, str2))  # Output: "geeke"

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Finding the LCS takes O(m * n), where m and n are the lengths of str1 and str2 respectively.
   - Constructing the shortest common supersequence based on the LCS takes O(m + n).
   - Overall time complexity: O(m * n).

2. Space Complexity:
   - The DP table used for finding the LCS takes O(m * n) space.
   - The result string and intermediate variables take O(m + n) space.
   - Overall space complexity: O(m * n).

Topic: Dynamic Programming (DP)
"""