"""
LeetCode Problem #2430: Maximum Deletions on a String

Problem Statement:
You are given a string `s` consisting of only lowercase English letters. In one operation, you can:
- Delete any non-empty substring of `s` that is a palindrome.

Return the maximum number of operations that can be performed on `s` such that the string becomes empty.

A string is a palindrome if it reads the same backward as forward.

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
"""

def deleteString(s: str) -> int:
    """
    This function calculates the maximum number of deletions that can be performed on the string `s`
    such that the string becomes empty.
    """
    n = len(s)
    # dp[i] represents the maximum number of deletions possible for the substring s[i:]
    dp = [1] * n

    # lcp[i][j] stores the length of the longest common prefix of s[i:] and s[j:]
    lcp = [[0] * (n + 1) for _ in range(n + 1)]

    # Compute the longest common prefix (LCP) array
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                lcp[i][j] = lcp[i + 1][j + 1] + 1

    # Fill the dp array
    for i in range(n - 1, -1, -1):
        for length in range(1, (n - i) // 2 + 1):
            if lcp[i][i + length] >= length:
                dp[i] = max(dp[i], 1 + dp[i + length])

    return dp[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcabcdabc"
    print(deleteString(s1))  # Expected Output: 2

    # Test Case 2
    s2 = "aaaaa"
    print(deleteString(s2))  # Expected Output: 5

    # Test Case 3
    s3 = "aabcaabcaabcaabc"
    print(deleteString(s3))  # Expected Output: 4

    # Test Case 4
    s4 = "leetcode"
    print(deleteString(s4))  # Expected Output: 1

    # Test Case 5
    s5 = "abababab"
    print(deleteString(s5))  # Expected Output: 4

"""
Time Complexity:
- Computing the LCP array takes O(n^2) time, where `n` is the length of the string.
- Filling the dp array also takes O(n^2) time, as we iterate over all substrings and check conditions.
- Overall time complexity: O(n^2).

Space Complexity:
- The LCP array requires O(n^2) space.
- The dp array requires O(n) space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming (DP)
"""