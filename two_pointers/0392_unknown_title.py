"""
LeetCode Problem #392: Is Subsequence

Problem Statement:
Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

Follow up:
If there are lots of incoming `s` strings, say `s1, s2, ..., sk` where `k >= 10^5`, how would you change your code to handle multiple `s` strings efficiently?
"""

# Clean, Correct Python Solution
def isSubsequence(s: str, t: str) -> bool:
    """
    Determines if string `s` is a subsequence of string `t`.

    :param s: The string to check as a subsequence.
    :param t: The string to check against.
    :return: True if `s` is a subsequence of `t`, False otherwise.
    """
    s_pointer, t_pointer = 0, 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    return s_pointer == len(s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: s is a subsequence of t
    s1 = "abc"
    t1 = "ahbgdc"
    print(isSubsequence(s1, t1))  # Expected Output: True

    # Test Case 2: s is not a subsequence of t
    s2 = "axc"
    t2 = "ahbgdc"
    print(isSubsequence(s2, t2))  # Expected Output: False

    # Test Case 3: Empty s string
    s3 = ""
    t3 = "ahbgdc"
    print(isSubsequence(s3, t3))  # Expected Output: True

    # Test Case 4: s is longer than t
    s4 = "abc"
    t4 = "ab"
    print(isSubsequence(s4, t4))  # Expected Output: False

    # Test Case 5: Both s and t are empty
    s5 = ""
    t5 = ""
    print(isSubsequence(s5, t5))  # Expected Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through both strings `s` and `t` using two pointers.
- In the worst case, we traverse the entire string `t`, which has a length of `n`.
- Therefore, the time complexity is O(n), where `n` is the length of `t`.

Space Complexity:
- The algorithm uses a constant amount of extra space (two pointers).
- Therefore, the space complexity is O(1).
"""

# Topic: Two Pointers