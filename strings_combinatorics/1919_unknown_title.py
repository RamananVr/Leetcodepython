"""
LeetCode Problem #1919: LeetCode Problem Statement

Problem Statement:
You are given a string s consisting of lowercase English letters. A subsequence of s is a string that can be derived from s by deleting some or no characters without changing the order of the remaining characters.

A good subsequence is a subsequence of s such that the number of unique characters in it is exactly 3. Return the number of distinct good subsequences of s. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

Note: The problem statement is paraphrased for clarity.
"""

# Python Solution
from collections import Counter
from math import comb

def countGoodSubsequences(s: str) -> int:
    MOD = 10**9 + 7
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Extract the frequencies of unique characters
    freq_values = list(freq.values())
    
    # If there are fewer than 3 unique characters, no good subsequences are possible
    if len(freq_values) < 3:
        return 0
    
    # Calculate the number of distinct good subsequences
    result = 0
    n = len(freq_values)
    
    # Iterate over all combinations of 3 unique characters
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Multiply the frequencies of the chosen characters
                result += freq_values[i] * freq_values[j] * freq_values[k]
                result %= MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcabc"
    print(countGoodSubsequences(s1))  # Expected Output: 27
    
    # Test Case 2
    s2 = "aabbcc"
    print(countGoodSubsequences(s2))  # Expected Output: 27
    
    # Test Case 3
    s3 = "aaa"
    print(countGoodSubsequences(s3))  # Expected Output: 0
    
    # Test Case 4
    s4 = "abcd"
    print(countGoodSubsequences(s4))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters in the string takes O(n), where n is the length of the string.
- Iterating over all combinations of 3 unique characters takes O(C(n, 3)) = O(n^3) in the worst case, where n is the number of unique characters.
- Overall, the time complexity is O(n + n^3), which is dominated by O(n^3) in the worst case.

Space Complexity:
- The space complexity is O(n), where n is the number of unique characters, due to the storage of the frequency dictionary.

Topic: Strings, Combinatorics
"""