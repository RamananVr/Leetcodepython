"""
LeetCode Problem #2781: Length of the Longest Valid Substring

Problem Statement:
You are given a string `s` and a list of strings `forbidden`. A substring of `s` is called valid if it does not contain any string from `forbidden` as a substring. Return the length of the longest valid substring of `s`.

A substring is a contiguous sequence of characters within a string.

Constraints:
- `1 <= s.length <= 10^5`
- `1 <= forbidden.length <= 1000`
- `1 <= forbidden[i].length <= 10`
- `s` consists of lowercase English letters.
- `forbidden[i]` consists of lowercase English letters.

Example:
Input: s = "cbaaaabc", forbidden = ["aaa", "abc"]
Output: 4
Explanation: The longest valid substring is "cbaa", which does not contain "aaa" or "abc".

Input: s = "leetcode", forbidden = ["code", "leet"]
Output: 4
Explanation: The longest valid substring is "leetc", which does not contain "code" or "leet".
"""

# Solution
def longestValidSubstring(s: str, forbidden: list[str]) -> int:
    forbidden_set = set(forbidden)
    n = len(s)
    max_length = 0
    start = 0

    for end in range(n):
        # Check substrings of length up to 10 (max length of forbidden strings)
        for length in range(1, min(10, end - start + 1) + 1):
            if s[end - length + 1:end + 1] in forbidden_set:
                start = end - length + 2
                break
        max_length = max(max_length, end - start + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cbaaaabc"
    forbidden1 = ["aaa", "abc"]
    print(longestValidSubstring(s1, forbidden1))  # Output: 4

    # Test Case 2
    s2 = "leetcode"
    forbidden2 = ["code", "leet"]
    print(longestValidSubstring(s2, forbidden2))  # Output: 4

    # Test Case 3
    s3 = "abcde"
    forbidden3 = ["xyz"]
    print(longestValidSubstring(s3, forbidden3))  # Output: 5

    # Test Case 4
    s4 = "aaaaa"
    forbidden4 = ["aaa"]
    print(longestValidSubstring(s4, forbidden4))  # Output: 2

    # Test Case 5
    s5 = "abcdefghij"
    forbidden5 = ["abc", "def", "ghi"]
    print(longestValidSubstring(s5, forbidden5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over the string `s`, so it runs `O(n)` times, where `n` is the length of `s`.
- For each character, we check substrings of length up to 10 (the maximum length of forbidden strings). This takes `O(10)` operations per character.
- Therefore, the overall time complexity is `O(10 * n)`, which simplifies to `O(n)`.

Space Complexity:
- The `forbidden_set` stores all forbidden strings, which takes `O(m)` space, where `m` is the number of forbidden strings.
- Other variables use constant space.
- Therefore, the overall space complexity is `O(m)`.

Topic: Sliding Window, Strings
"""