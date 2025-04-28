"""
LeetCode Problem #1698: Number of Distinct Substrings in a String

Problem Statement:
Given a string `s`, return the number of distinct substrings of `s`.

A substring is a contiguous sequence of characters within a string. For example, "abc" has the following substrings:
- "a", "b", "c", "ab", "bc", "abc"

Example 1:
Input: s = "aabbaba"
Output: 21
Explanation: The distinct substrings are:
"a", "b", "aa", "bb", "ab", "ba", "aab", "abb", "bba", "aba", "aabb", "abba", "baba", "aabba", "abbab", "bbaba", "aabbab", "abbaba", "bbaba", "aabbaba", "aabbaba".

Example 2:
Input: s = "abc"
Output: 6
Explanation: The distinct substrings are:
"a", "b", "c", "ab", "bc", "abc".

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.

Follow-up:
Can you solve this problem in O(n^2) or better time complexity?
"""

# Solution
def countDistinctSubstrings(s: str) -> int:
    """
    Returns the number of distinct substrings in the given string `s`.
    """
    # Use a set to store all unique substrings
    substrings = set()
    
    # Generate all substrings and add them to the set
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    
    # The size of the set is the number of distinct substrings
    return len(substrings)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabbaba"
    print(f"Number of distinct substrings in '{s1}': {countDistinctSubstrings(s1)}")  # Expected: 21

    # Test Case 2
    s2 = "abc"
    print(f"Number of distinct substrings in '{s2}': {countDistinctSubstrings(s2)}")  # Expected: 6

    # Test Case 3
    s3 = "aaaa"
    print(f"Number of distinct substrings in '{s3}': {countDistinctSubstrings(s3)}")  # Expected: 10

    # Test Case 4
    s4 = "abac"
    print(f"Number of distinct substrings in '{s4}': {countDistinctSubstrings(s4)}")  # Expected: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs `n` times (for each starting index of the substring).
- The inner loop runs approximately `n/2` times on average (for each ending index of the substring).
- Adding a substring to the set takes O(1) on average.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n^2) in the worst case, as the set can store up to n(n+1)/2 substrings (all possible substrings of the string).
"""

# Topic: Strings, Hashing