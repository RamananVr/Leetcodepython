"""
LeetCode Problem #2014: Longest Subsequence Repeated k Times

Problem Statement:
You are given a string s of length n, and an integer k. A subsequence of s is a string that can be formed by deleting 
some (possibly zero) characters from s without changing the order of the remaining characters.

Return the longest subsequence repeated k times in s. If multiple subsequences of the same length exist, return the 
lexicographically largest one. If there is no valid subsequence, return an empty string.

Example 1:
Input: s = "letsleetcode", k = 2
Output: "let"

Example 2:
Input: s = "bb", k = 2
Output: "b"

Example 3:
Input: s = "ab", k = 2
Output: ""

Constraints:
- n == s.length
- 2 <= n <= 100
- 2 <= k <= 10
- s consists of lowercase English letters.
"""

from itertools import combinations

def longestSubsequenceRepeatedK(s: str, k: int) -> str:
    def is_k_subsequence(subseq: str) -> bool:
        """Check if subseq is a subsequence of s repeated k times."""
        it = iter(s)
        count = 0
        for _ in range(k):
            for char in subseq:
                if char not in it:
                    return False
            count += 1
        return count == k

    # Count character frequencies in s
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Filter characters that appear at least k times
    valid_chars = [char for char, count in freq.items() if count >= k]

    # Generate all possible subsequences of valid characters
    max_length = len(s) // k
    result = ""

    for length in range(1, max_length + 1):
        for subseq in combinations(valid_chars, length):
            candidate = "".join(subseq)
            if is_k_subsequence(candidate):
                if len(candidate) > len(result) or (len(candidate) == len(result) and candidate > result):
                    result = candidate

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "letsleetcode", 2
    print(longestSubsequenceRepeatedK(s1, k1))  # Output: "let"

    # Test Case 2
    s2, k2 = "bb", 2
    print(longestSubsequenceRepeatedK(s2, k2))  # Output: "b"

    # Test Case 3
    s3, k3 = "ab", 2
    print(longestSubsequenceRepeatedK(s3, k3))  # Output: ""

    # Test Case 4
    s4, k4 = "aaaa", 3
    print(longestSubsequenceRepeatedK(s4, k4))  # Output: "a"

    # Test Case 5
    s5, k5 = "abcabcabc", 3
    print(longestSubsequenceRepeatedK(s5, k5))  # Output: "abc"


"""
Time Complexity:
- Let n = len(s) and m = len(valid_chars).
- Generating all combinations of valid characters up to length n // k takes O(m^n/k).
- For each combination, checking if it is a k-subsequence takes O(n).
- Overall complexity is O(m^n/k * n), which is exponential in the worst case.

Space Complexity:
- The space complexity is O(m^n/k) for storing combinations and O(n) for the input string.

Topic: Strings, Backtracking, Combinatorics
"""