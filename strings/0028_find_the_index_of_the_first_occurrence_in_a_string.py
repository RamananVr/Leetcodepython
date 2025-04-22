"""
LeetCode Question #28: Find the Index of the First Occurrence in a String

Problem Statement:
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Clarifications:
- The function should return `0` if `needle` is an empty string, as an empty string is considered to occur at the beginning of any string.
- The input strings consist of only lowercase English characters.

Constraints:
- 1 <= len(haystack), len(needle) <= 10^4
- `needle` is guaranteed to be a substring of `haystack` in some test cases.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" does not occur in "leetcode", so we return -1.
"""

# Clean and Correct Python Solution
def strStr(haystack: str, needle: str) -> int:
    # Edge case: if needle is an empty string, return 0
    if not needle:
        return 0
    
    # Use Python's built-in string find method
    return haystack.find(needle)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Needle is at the beginning
    haystack = "sadbutsad"
    needle = "sad"
    print(strStr(haystack, needle))  # Output: 0

    # Test Case 2: Needle is not in haystack
    haystack = "leetcode"
    needle = "leeto"
    print(strStr(haystack, needle))  # Output: -1

    # Test Case 3: Needle is an empty string
    haystack = "hello"
    needle = ""
    print(strStr(haystack, needle))  # Output: 0

    # Test Case 4: Needle is at the end
    haystack = "mississippi"
    needle = "pi"
    print(strStr(haystack, needle))  # Output: 9

    # Test Case 5: Needle is the entire haystack
    haystack = "abc"
    needle = "abc"
    print(strStr(haystack, needle))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `find` method in Python is implemented using a variation of the Knuth-Morris-Pratt (KMP) algorithm.
- In the worst case, the time complexity is O(n + m), where n is the length of `haystack` and m is the length of `needle`.

Space Complexity:
- The space complexity is O(1) as no additional data structures are used.

Overall:
- Time Complexity: O(n + m)
- Space Complexity: O(1)
"""

# Topic: Strings