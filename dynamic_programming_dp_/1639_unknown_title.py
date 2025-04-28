"""
LeetCode Problem #1639: Number of Ways to Form a Target String Given a Dictionary

Problem Statement:
You are given a list of strings `words` and a string `target`. Return the number of ways to form the `target` string by 
choosing one letter from each string in `words` such that the chosen letters form the `target` string.

Each string in `words` can only be used once per letter. Order matters, so the letters must be chosen in the same order 
as they appear in the `target`.

Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- All strings in `words` have the same length.
- `1 <= target.length <= 1000`
- `words[i]` and `target` contain only lowercase English letters.
"""

from collections import defaultdict

def numWays(words, target):
    MOD = 10**9 + 7
    m, n = len(target), len(words[0])
    
    # Precompute the frequency of each character at each position in words
    char_count = [defaultdict(int) for _ in range(n)]
    for word in words:
        for i, char in enumerate(word):
            char_count[i][char] += 1
    
    # DP array: dp[i][j] represents the number of ways to form target[:i] using the first j columns of words
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1  # Base case: 1 way to form an empty target
    
    for j in range(1, n + 1):
        dp[0][j] = 1  # Still 1 way to form an empty target with any number of columns
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Option 1: Skip the current column
            dp[i][j] = dp[i][j - 1]
            
            # Option 2: Use the current column if the character matches
            if target[i - 1] in char_count[j - 1]:
                dp[i][j] += dp[i - 1][j - 1] * char_count[j - 1][target[i - 1]]
                dp[i][j] %= MOD
    
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["acca", "bbbb", "caca"]
    target1 = "aba"
    print(numWays(words1, target1))  # Output: 6

    # Test Case 2
    words2 = ["abba", "baab"]
    target2 = "bab"
    print(numWays(words2, target2))  # Output: 4

    # Test Case 3
    words3 = ["abcd", "abcd", "abcd"]
    target3 = "abcd"
    print(numWays(words3, target3))  # Output: 1

    # Test Case 4
    words4 = ["abab", "baba", "abba", "baab"]
    target4 = "abba"
    print(numWays(words4, target4))  # Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing the frequency of each character at each position takes O(n * len(words)).
- Filling the DP table takes O(m * n), where m is the length of the target and n is the length of each word.
- Overall time complexity: O(n * len(words) + m * n).

Space Complexity:
- The `char_count` array takes O(n * 26) space (26 for each letter of the alphabet).
- The DP table takes O(m * n) space.
- Overall space complexity: O(n * 26 + m * n).

Primary Topic: Dynamic Programming (DP)
"""