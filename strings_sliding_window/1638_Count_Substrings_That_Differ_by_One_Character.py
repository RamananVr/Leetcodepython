"""
LeetCode Problem #1638: Count Substrings That Differ by One Character

Problem Statement:
Given two strings `s` and `t`, find the number of substrings in `s` and `t` that differ by exactly one character.

For example, the substrings "ab" and "ac" differ by one character, while "ab" and "ab" do not differ by any characters.

Constraints:
1. 1 <= s.length, t.length <= 100
2. s and t consist of lowercase English letters only.

You need to return the number of such substrings.

Example:
Input: s = "aba", t = "baba"
Output: 6
Explanation: The substrings are:
- ("aba", "bba") differ by 1 at index 0.
- ("aba", "bab") differ by 1 at index 1.
- ("aba", "aba") differ by 1 at index 2.
- ("ab", "bb") differ by 1 at index 0.
- ("ab", "ba") differ by 1 at index 1.
- ("ba", "bb") differ by 1 at index 1.
"""

def countSubstrings(s: str, t: str) -> int:
    def count_diff_by_one(s, t, i, j):
        """Helper function to count substrings starting at s[i] and t[j] that differ by exactly one character."""
        m, n = len(s), len(t)
        count = 0
        diff = 0
        while i < m and j < n:
            if s[i] != t[j]:
                diff += 1
            if diff > 1:
                break
            if diff == 1:
                count += 1
            i += 1
            j += 1
        return count

    result = 0
    # Iterate over all possible starting points in s and t
    for i in range(len(s)):
        for j in range(len(t)):
            result += count_diff_by_one(s, t, i, j)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aba"
    t1 = "baba"
    print(countSubstrings(s1, t1))  # Output: 6

    # Test Case 2
    s2 = "ab"
    t2 = "bb"
    print(countSubstrings(s2, t2))  # Output: 3

    # Test Case 3
    s3 = "a"
    t3 = "a"
    print(countSubstrings(s3, t3))  # Output: 0

    # Test Case 4
    s4 = "abc"
    t4 = "def"
    print(countSubstrings(s4, t4))  # Output: 9

"""
Time Complexity:
- The outer loops iterate over all starting indices in `s` and `t`, which is O(m * n), where `m` is the length of `s` and `n` is the length of `t`.
- The helper function `count_diff_by_one` iterates over the substrings starting at the given indices, which in the worst case can take O(min(m, n)) time.
- Overall, the time complexity is O(m * n * min(m, n)).

Space Complexity:
- The algorithm uses O(1) additional space, as it only uses a few variables for counting and comparisons.

Topic: Strings, Sliding Window
"""