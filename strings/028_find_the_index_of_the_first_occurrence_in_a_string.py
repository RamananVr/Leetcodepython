"""
LeetCode Question #28: Find the Index of the First Occurrence in a String

Problem Statement:
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

Clarifications:
- The function should return 0 if `needle` is an empty string, as per the problem constraints.
- The comparison is case-sensitive, and the substring search should be exact.

Constraints:
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" does not occur in "leetcode", so return -1.

Example 3:
Input: haystack = "hello", needle = ""
Output: 0
Explanation: An empty string is always found at index 0.

Follow-up:
Can you implement this function using only O(n + m) time complexity, where n is the length of `haystack` and m is the length of `needle`?
"""

# Clean, correct Python solution
def strStr(haystack: str, needle: str) -> int:
    # Edge case: If needle is an empty string, return 0
    if not needle:
        return 0
    
    # Use Python's built-in `find` method to locate the first occurrence
    return haystack.find(needle)

# Example test cases
if __name__ == "__main__":
    # Test case 1: Needle is found at the beginning
    haystack = "sadbutsad"
    needle = "sad"
    print(strStr(haystack, needle))  # Output: 0

    # Test case 2: Needle is not found
    haystack = "leetcode"
    needle = "leeto"
    print(strStr(haystack, needle))  # Output: -1

    # Test case 3: Needle is an empty string
    haystack = "hello"
    needle = ""
    print(strStr(haystack, needle))  # Output: 0

    # Test case 4: Needle is found in the middle
    haystack = "mississippi"
    needle = "issip"
    print(strStr(haystack, needle))  # Output: 4

    # Test case 5: Needle is the same as haystack
    haystack = "abc"
    needle = "abc"
    print(strStr(haystack, needle))  # Output: 0

# Topic: Strings