"""
LeetCode Problem #2539: Count the Number of Good Subsequences

Problem Statement:
You are given a string `s` consisting of lowercase English letters. A subsequence of `s` is called good if it satisfies the following conditions:
1. The frequency of each character in the subsequence is equal.
2. The subsequence is non-empty.

Return the number of distinct good subsequences of `s`. Since the answer may be very large, return it modulo 10^9 + 7.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of lowercase English letters.
"""

# Solution
from collections import Counter

def countGoodSubsequences(s: str) -> int:
    MOD = 10**9 + 7
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Extract the frequencies of each character
    freq_values = list(freq.values())
    
    # Find the maximum frequency
    max_freq = max(freq_values)
    
    # Precompute factorials and modular inverses for combinations
    factorial = [1] * (max_freq + 1)
    for i in range(2, max_freq + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    
    def mod_inverse(x):
        return pow(x, MOD - 2, MOD)
    
    # Precompute modular inverses of factorials
    inv_factorial = [1] * (max_freq + 1)
    for i in range(2, max_freq + 1):
        inv_factorial[i] = mod_inverse(factorial[i])
    
    # Function to calculate combinations modulo MOD
    def comb(n, k):
        if k > n:
            return 0
        return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD
    
    # Count good subsequences
    result = 0
    for freq_count in range(1, max_freq + 1):
        subsequences = 1
        for f in freq_values:
            subsequences *= comb(f, freq_count) + 1
            subsequences %= MOD
        result += subsequences - 1
        result %= MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabb"
    print(countGoodSubsequences(s1))  # Expected Output: 15

    # Test Case 2
    s2 = "abc"
    print(countGoodSubsequences(s2))  # Expected Output: 7

    # Test Case 3
    s3 = "aaaa"
    print(countGoodSubsequences(s3))  # Expected Output: 15

    # Test Case 4
    s4 = "a"
    print(countGoodSubsequences(s4))  # Expected Output: 1

    # Test Case 5
    s5 = "abacaba"
    print(countGoodSubsequences(s5))  # Expected Output: 127

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the frequency of characters in the string takes O(n), where n is the length of the string.
- Precomputing factorials and modular inverses takes O(max_freq).
- Calculating combinations for each frequency count involves iterating over the frequencies and performing modular arithmetic, which is O(max_freq * len(freq_values)).
- Overall, the time complexity is O(n + max_freq * len(freq_values)).

Space Complexity:
- The space used for storing the frequency counter is O(26) (constant space for lowercase English letters).
- The space used for factorials and modular inverses is O(max_freq).
- Overall, the space complexity is O(max_freq).

Topic: Combinatorics, Strings
"""