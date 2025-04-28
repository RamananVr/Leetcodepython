"""
LeetCode Problem #2486: Append Characters to String to Make Subsequence

Problem Statement:
You are given two strings `s` and `t` consisting of only lowercase English letters. 
You need to append characters to the end of `s` to make `t` a subsequence of `s`. 
Return the minimum number of characters that you need to append.

A string `a` is a subsequence of a string `b` if `a` can be obtained from `b` by deleting 
some (possibly zero) characters without changing the order of the remaining characters.

Example 1:
Input: s = "abc", t = "abcbc"
Output: 2
Explanation: We can append "bc" to "abc" to make "abcbc" a subsequence of "abc".

Example 2:
Input: s = "abc", t = "acdbc"
Output: 3
Explanation: We can append "dbc" to "abc" to make "acdbc" a subsequence of "abc".

Example 3:
Input: s = "abc", t = "abc"
Output: 0
Explanation: "abc" is already a subsequence of "abc".

Constraints:
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.
"""

def appendCharacters(s: str, t: str) -> int:
    """
    Function to calculate the minimum number of characters to append to `s` 
    to make `t` a subsequence of `s`.
    """
    # Pointer for `s`
    i = 0
    # Pointer for `t`
    j = 0

    # Traverse both strings
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1  # Move `t` pointer if characters match
        i += 1  # Always move `s` pointer

    # The remaining characters in `t` are the ones we need to append
    return len(t) - j

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    t1 = "abcbc"
    print(appendCharacters(s1, t1))  # Output: 2

    # Test Case 2
    s2 = "abc"
    t2 = "acdbc"
    print(appendCharacters(s2, t2))  # Output: 3

    # Test Case 3
    s3 = "abc"
    t3 = "abc"
    print(appendCharacters(s3, t3))  # Output: 0

    # Test Case 4
    s4 = "a"
    t4 = "aaaa"
    print(appendCharacters(s4, t4))  # Output: 3

    # Test Case 5
    s5 = "xyz"
    t5 = "xyzxyz"
    print(appendCharacters(s5, t5))  # Output: 3

"""
Time Complexity Analysis:
- The function uses two pointers to traverse `s` and `t`. Each pointer moves at most once through its respective string.
- Therefore, the time complexity is O(n + m), where `n` is the length of `s` and `m` is the length of `t`.

Space Complexity Analysis:
- The function uses a constant amount of extra space (two pointers and a few variables).
- Therefore, the space complexity is O(1).

Topic: Two Pointers
"""