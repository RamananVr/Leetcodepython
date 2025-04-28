"""
LeetCode Problem #2994: Problem Statement

You are given a string `s` consisting of lowercase English letters. You need to find the number of distinct subsequences of `s` modulo 10^9 + 7.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Return the number of distinct subsequences of `s` modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 1000
- `s` consists of lowercase English letters.
"""

# Python Solution
def distinctSubseqII(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i] represents the number of distinct subsequences of s[:i]
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has one subsequence (the empty subsequence)
    
    # last_seen keeps track of the last index where each character was seen
    last_seen = {}
    
    for i in range(1, n + 1):
        char = s[i - 1]
        dp[i] = (2 * dp[i - 1]) % MOD  # Double the subsequences from the previous step
        
        # If the character was seen before, subtract the subsequences that were duplicated
        if char in last_seen:
            dp[i] -= dp[last_seen[char] - 1]
            dp[i] %= MOD
        
        # Update the last seen index for the current character
        last_seen[char] = i
    
    # Subtract 1 to exclude the empty subsequence
    return (dp[n] - 1) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(distinctSubseqII(s1))  # Expected Output: 7 (subsequences: "", "a", "b", "c", "ab", "ac", "bc", "abc")
    
    # Test Case 2
    s2 = "aaa"
    print(distinctSubseqII(s2))  # Expected Output: 7 (subsequences: "", "a", "aa", "aaa")
    
    # Test Case 3
    s3 = "abab"
    print(distinctSubseqII(s3))  # Expected Output: 15
    
    # Test Case 4
    s4 = "leetcode"
    print(distinctSubseqII(s4))  # Expected Output: 63

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the string `s` once, which takes O(n) time.
- For each character, we perform constant-time operations (e.g., updating `dp` and `last_seen`).
- Therefore, the overall time complexity is O(n), where n is the length of the string.

Space Complexity:
- We use a `dp` array of size n+1, which takes O(n) space.
- We use a dictionary `last_seen` to store the last index of each character, which takes O(26) space in the worst case (for all lowercase English letters).
- Therefore, the overall space complexity is O(n).
"""

# Topic: Dynamic Programming