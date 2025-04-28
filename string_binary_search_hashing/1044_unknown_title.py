"""
LeetCode Problem #1044: Longest Duplicate Substring

Problem Statement:
Given a string s, find the longest substring that appears at least twice in s. 
If no such substring exists, return an empty string.

Example 1:
Input: s = "banana"
Output: "ana"

Example 2:
Input: s = "abcd"
Output: ""

Constraints:
- 2 <= s.length <= 3 * 10^4
- s consists of lowercase English letters.
"""

# Solution
def longestDupSubstring(s: str) -> str:
    def search(length, base, modulus):
        """Search for a duplicate substring of given length using Rabin-Karp."""
        hash_val = 0
        for i in range(length):
            hash_val = (hash_val * base + ord(s[i])) % modulus
        
        seen = {hash_val}
        base_l = pow(base, length, modulus)  # base^length % modulus
        
        for i in range(1, len(s) - length + 1):
            hash_val = (hash_val * base - ord(s[i - 1]) * base_l + ord(s[i + length - 1])) % modulus
            if hash_val in seen:
                return i
            seen.add(hash_val)
        return -1

    # Binary search for the length of the longest duplicate substring
    base = 256
    modulus = 2**63 - 1
    left, right = 1, len(s)
    start = -1
    max_length = 0

    while left < right:
        mid = (left + right) // 2
        idx = search(mid, base, modulus)
        if idx != -1:  # Found a duplicate substring of length `mid`
            start = idx
            max_length = mid
            left = mid + 1
        else:  # No duplicate substring of length `mid`
            right = mid

    return s[start:start + max_length] if start != -1 else ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "banana"
    print(longestDupSubstring(s1))  # Output: "ana"

    # Test Case 2
    s2 = "abcd"
    print(longestDupSubstring(s2))  # Output: ""

    # Test Case 3
    s3 = "aaaaa"
    print(longestDupSubstring(s3))  # Output: "aaaa"

    # Test Case 4
    s4 = "abcabcabc"
    print(longestDupSubstring(s4))  # Output: "abcabc"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(n)), where n is the length of the string.
- For each length `mid` during binary search, the Rabin-Karp algorithm computes hashes in O(n).
- Therefore, the overall time complexity is O(n * log(n)).

Space Complexity:
- The space complexity is O(n) due to the hash set used to store seen hash values.

Topic: String, Binary Search, Hashing
"""