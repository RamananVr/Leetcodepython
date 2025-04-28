"""
LeetCode Problem #1312: Minimum Insertion Steps to Make a String Palindrome

Problem Statement:
Given a string s. In one step you can insert any character at any position of the string.
Return the minimum number of steps to make s a palindrome.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already a palindrome, so no insertions are needed.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be transformed into "madam" by inserting two characters.

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: String can be transformed into "leetcodocteel" by inserting five characters.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""

# Solution
def minInsertions(s: str) -> int:
    """
    Returns the minimum number of insertions required to make the string a palindrome.
    Uses dynamic programming to solve the problem efficiently.
    """
    n = len(s)
    # dp[i][j] represents the minimum insertions needed to make s[i:j+1] a palindrome
    dp = [[0] * n for _ in range(n)]

    # Fill the DP table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "zzazz"
    print(minInsertions(s1))  # Output: 0

    # Test Case 2
    s2 = "mbadm"
    print(minInsertions(s2))  # Output: 2

    # Test Case 3
    s3 = "leetcode"
    print(minInsertions(s3))  # Output: 5

    # Test Case 4
    s4 = "a"
    print(minInsertions(s4))  # Output: 0

    # Test Case 5
    s5 = "ab"
    print(minInsertions(s5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a nested loop structure.
- The outer loop iterates over substring lengths (from 2 to n), and the inner loop iterates over starting indices of substrings.
- Filling the DP table takes O(n^2) time, where n is the length of the string.

Space Complexity:
- The solution uses a 2D DP table of size n x n, which requires O(n^2) space.

Overall:
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Topic: Dynamic Programming
"""