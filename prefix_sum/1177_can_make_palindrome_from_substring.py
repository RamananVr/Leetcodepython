"""
LeetCode Question #1177: Can Make Palindrome from Substring

Problem Statement:
You are given a string `s` and an array of queries `queries` where `queries[i] = [left_i, right_i, k_i]`.
We may rearrange the substring `s[left_i...right_i]` for each query and then choose up to `k_i` characters to replace.

Return a boolean array `answer`, where `answer[i]` is true if the substring `s[left_i...right_i]` can be rearranged to form a palindrome after at most `k_i` replacements.

A string can be rearranged to form a palindrome if the number of characters with odd frequencies is at most 1. With replacements, we can reduce the number of odd frequencies.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= queries.length <= 10^5`
- `0 <= left_i <= right_i < s.length`
- `0 <= k_i <= 10^5`
"""

# Solution
from typing import List

def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
    # Precompute prefix frequency counts for each character
    n = len(s)
    prefix = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(n):
        prefix[i + 1] = prefix[i][:]
        prefix[i + 1][ord(s[i]) - ord('a')] += 1
    
    # Helper function to calculate odd frequencies in a range
    def countOddFrequencies(left: int, right: int) -> int:
        odd_count = 0
        for i in range(26):
            freq = prefix[right + 1][i] - prefix[left][i]
            if freq % 2 != 0:
                odd_count += 1
        return odd_count
    
    # Process each query
    result = []
    for left, right, k in queries:
        odd_count = countOddFrequencies(left, right)
        # A palindrome can have at most one odd frequency, so we need (odd_count - 1) replacements
        result.append((odd_count - 1) // 2 <= k)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    print(canMakePaliQueries(s, queries))  # Output: [True, False, False, True, True]

    # Test Case 2
    s = "aabbcc"
    queries = [[0, 5, 0], [0, 5, 1], [0, 5, 2], [0, 5, 3]]
    print(canMakePaliQueries(s, queries))  # Output: [False, False, True, True]

    # Test Case 3
    s = "xxyyzz"
    queries = [[0, 5, 0], [0, 5, 1], [0, 5, 2], [0, 5, 3]]
    print(canMakePaliQueries(s, queries))  # Output: [False, True, True, True]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing prefix frequency counts: O(n * 26) = O(n), where n is the length of the string `s`.
- Processing each query: O(queries.length * 26) = O(queries.length), where queries.length is the number of queries.
- Total: O(n + queries.length).

Space Complexity:
- Prefix frequency array: O(n * 26) = O(n).
- Result array: O(queries.length).
- Total: O(n + queries.length).

Topic: Prefix Sum
"""