"""
LeetCode Problem #2842: Count K-Subsequences of a String With Maximum Beauty

Problem Statement:
You are given a string `s` and an integer `k`. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

The beauty of a string is defined as the number of distinct characters in the string.

- Return the number of k-length subsequences of `s` that have the maximum beauty. Since the answer may be very large, return it modulo 10^9 + 7.

A k-length subsequence of `s` is a subsequence of `s` where the length of the subsequence is `k`.

Constraints:
- `1 <= s.length <= 1000`
- `1 <= k <= s.length`
- `s` consists of lowercase English letters.

"""

from collections import Counter
from math import comb

MOD = 10**9 + 7

def countKSubsequencesWithMaxBeauty(s: str, k: int) -> int:
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # If there are fewer than k distinct characters, it's impossible to form a k-length subsequence
    if len(freq) < k:
        return 0

    # Sort characters by frequency in descending order
    sorted_freq = sorted(freq.values(), reverse=True)
    
    # Find the maximum beauty by selecting the top k most frequent characters
    max_beauty_chars = sorted_freq[:k]
    min_freq_in_max_beauty = max_beauty_chars[-1]
    
    # Count how many characters have the minimum frequency in the top k
    min_freq_count = max_beauty_chars.count(min_freq_in_max_beauty)
    
    # Count how many characters in the entire frequency list have the minimum frequency
    total_min_freq_count = sorted_freq.count(min_freq_in_max_beauty)
    
    # Calculate the number of ways to choose the required characters with the minimum frequency
    ways_to_choose_min_freq = comb(total_min_freq_count, min_freq_count)
    
    # Calculate the product of frequencies for the top k characters
    product_of_frequencies = 1
    for freq in max_beauty_chars:
        product_of_frequencies = (product_of_frequencies * freq) % MOD
    
    # Multiply the product of frequencies with the number of ways to choose the minimum frequency characters
    result = (product_of_frequencies * ways_to_choose_min_freq) % MOD
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabbcc"
    k1 = 2
    print(countKSubsequencesWithMaxBeauty(s1, k1))  # Expected Output: 6

    # Test Case 2
    s2 = "abcabc"
    k2 = 3
    print(countKSubsequencesWithMaxBeauty(s2, k2))  # Expected Output: 6

    # Test Case 3
    s3 = "aaaa"
    k3 = 2
    print(countKSubsequencesWithMaxBeauty(s3, k3))  # Expected Output: 6

    # Test Case 4
    s4 = "xyz"
    k4 = 3
    print(countKSubsequencesWithMaxBeauty(s4, k4))  # Expected Output: 1

    # Test Case 5
    s5 = "aabbcc"
    k5 = 4
    print(countKSubsequencesWithMaxBeauty(s5, k5))  # Expected Output: 0

"""
Time Complexity:
- Counting frequencies takes O(n), where n is the length of the string `s`.
- Sorting the frequencies takes O(d log d), where d is the number of distinct characters in `s`.
- Calculating combinations is O(k) in the worst case.
- Overall complexity: O(n + d log d + k), where d <= 26 (constant for lowercase English letters).

Space Complexity:
- The space complexity is O(d) for storing the frequency dictionary, where d is the number of distinct characters in `s`.
- Overall space complexity: O(d), which is effectively O(1) since d <= 26.

Topic: Strings, Combinatorics
"""