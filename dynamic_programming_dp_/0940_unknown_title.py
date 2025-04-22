"""
LeetCode Problem #940: Distinct Subsequences II

Problem Statement:
Given a string `s`, return the number of distinct non-empty subsequences of the string. 
Since the answer may be very large, return it modulo 10^9 + 7.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

Example:
- "abc" has the following distinct subsequences: "a", "b", "c", "ab", "ac", "bc", "abc".
- "aaa" has the following distinct subsequences: "a", "aa", "aaa".

Constraints:
1. `1 <= s.length <= 2000`
2. `s` consists of lowercase English letters.

"""

# Python Solution
def distinctSubseqII(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i] represents the number of distinct subsequences that can be formed using the first i characters of s
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has one subsequence (the empty subsequence)

    # last_seen keeps track of the last index where each character was seen
    last_seen = {}

    for i in range(1, n + 1):
        char = s[i - 1]
        dp[i] = (2 * dp[i - 1]) % MOD  # Double the subsequences from the previous step

        # If the character was seen before, subtract the subsequences formed before its last occurrence
        if char in last_seen:
            dp[i] -= dp[last_seen[char] - 1]
            dp[i] %= MOD  # Ensure non-negative modulo

        # Update the last seen index for the current character
        last_seen[char] = i

    # Subtract 1 to exclude the empty subsequence
    return (dp[n] - 1) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(distinctSubseqII(s1))  # Expected Output: 7

    # Test Case 2
    s2 = "aaa"
    print(distinctSubseqII(s2))  # Expected Output: 3

    # Test Case 3
    s3 = "abab"
    print(distinctSubseqII(s3))  # Expected Output: 14

    # Test Case 4
    s4 = "a"
    print(distinctSubseqII(s4))  # Expected Output: 1

    # Test Case 5
    s5 = "abac"
    print(distinctSubseqII(s5))  # Expected Output: 15


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Thus, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The `dp` array requires O(n) space.
- The `last_seen` dictionary requires O(26) space in the worst case (one entry for each lowercase English letter).
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""