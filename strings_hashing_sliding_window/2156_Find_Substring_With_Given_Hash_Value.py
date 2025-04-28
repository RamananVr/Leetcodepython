"""
LeetCode Problem #2156: Find Substring With Given Hash Value

Problem Statement:
You are given a string `s` and two integers `p` and `m`. You are also given an integer `k` and a hash value `target`.

The hash of a substring `s[l...r]` is defined as:
    hash(s[l...r]) = (val(s[l]) * p^0 + val(s[l+1]) * p^1 + ... + val(s[r]) * p^(r-l)) mod m
where `val(s[i])` is the ASCII value of the character `s[i]`.

Return the first (leftmost) substring of length `k` whose hash value is equal to `target`. If no such substring exists, return an empty string.

A substring is a contiguous non-empty sequence of characters within a string.

Example:
Input: s = "leetcode", k = 3, p = 7, m = 20, target = 10
Output: "lee"

Constraints:
- `1 <= k <= s.length <= 2 * 10^4`
- `1 <= p, m <= 10^9`
- `0 <= target < m`
- `s` consists of lowercase English letters only.
"""

# Solution
def subStrHash(s: str, p: int, m: int, k: int, target: int) -> str:
    n = len(s)
    current_hash = 0
    p_k = pow(p, k, m)  # Precompute p^k % m
    result = ""

    # Compute the hash for the last k-length substring
    for i in range(n - 1, n - k - 1, -1):
        current_hash = (current_hash * p + ord(s[i])) % m

    # Check if the last k-length substring matches the target
    if current_hash == target:
        result = s[n - k:]

    # Sliding window to compute hash for other substrings
    for i in range(n - k - 1, -1, -1):
        current_hash = (current_hash * p - ord(s[i + k]) * p_k + ord(s[i])) % m
        if current_hash == target:
            result = s[i:i + k]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "leetcode"
    k = 3
    p = 7
    m = 20
    target = 10
    print(subStrHash(s, p, m, k, target))  # Output: "lee"

    # Test Case 2
    s = "abcdefgh"
    k = 2
    p = 5
    m = 100
    target = 97
    print(subStrHash(s, p, m, k, target))  # Output: "ab"

    # Test Case 3
    s = "aaaaaa"
    k = 2
    p = 3
    m = 10
    target = 6
    print(subStrHash(s, p, m, k, target))  # Output: "aa"

    # Test Case 4
    s = "xyzxyzxyz"
    k = 3
    p = 2
    m = 50
    target = 29
    print(subStrHash(s, p, m, k, target))  # Output: "xyz"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the hash for the first substring takes O(k).
- Sliding window hash computation for the remaining substrings takes O(n - k).
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables and computations.
- Overall space complexity: O(1).
"""

# Topic: Strings, Hashing, Sliding Window