"""
LeetCode Problem #2720: "Maximum Number of Non-Overlapping Palindrome Substrings"

Problem Statement:
You are given a string `s` and an integer `k`. A substring is called a palindrome if it reads the same backward as forward. A palindrome substring is non-overlapping if it does not share any character with another palindrome substring.

Your task is to find the maximum number of non-overlapping palindrome substrings of length at least `k` that can be extracted from the string `s`.

Constraints:
- 1 <= k <= len(s) <= 10^5
- s consists of lowercase English letters.

Example:
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: The two non-overlapping palindromes are "aba" and "dbbd".

Write a function `maxPalindromes(s: str, k: int) -> int` to solve the problem.
"""

def maxPalindromes(s: str, k: int) -> int:
    def is_palindrome(l: int, r: int) -> bool:
        """Helper function to check if s[l:r+1] is a palindrome."""
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    n = len(s)
    dp = [0] * (n + 1)  # dp[i] represents the max number of palindromes in s[:i]

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]  # By default, carry over the previous count
        if i >= k and is_palindrome(i - k, i - 1):
            dp[i] = max(dp[i], dp[i - k] + 1)
        if i > k and is_palindrome(i - k - 1, i - 1):
            dp[i] = max(dp[i], dp[i - k - 1] + 1)

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "abaccdbbd", 3
    print(maxPalindromes(s1, k1))  # Output: 2

    # Test Case 2
    s2, k2 = "aaaaa", 2
    print(maxPalindromes(s2, k2))  # Output: 2

    # Test Case 3
    s3, k3 = "racecar", 7
    print(maxPalindromes(s3, k3))  # Output: 1

    # Test Case 4
    s4, k4 = "abc", 2
    print(maxPalindromes(s4, k4))  # Output: 0

    # Test Case 5
    s5, k5 = "aabaa", 3
    print(maxPalindromes(s5, k5))  # Output: 1

"""
Time Complexity Analysis:
- The `is_palindrome` function runs in O(k) time for each call.
- The main loop iterates over the string of length `n`, and for each iteration, it may call `is_palindrome` twice.
- Therefore, the overall time complexity is O(n * k).

Space Complexity Analysis:
- The `dp` array requires O(n) space.
- No additional space is used apart from the `dp` array and a few variables.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""