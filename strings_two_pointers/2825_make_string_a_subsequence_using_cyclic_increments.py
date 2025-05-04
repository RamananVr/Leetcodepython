"""
LeetCode Question #2825: Make String a Subsequence Using Cyclic Increments

Problem Statement:
You are given two strings `s` and `t`, both consisting of lowercase English letters.

You are allowed to perform the following operation any number of times on `s`:
- Choose any character of `s` and increment it cyclically to the next character. For example, 'a' becomes 'b', 'b' becomes 'c', ..., and 'z' becomes 'a'.

Return `true` if it is possible to make `s` a subsequence of `t` using the above operation any number of times. Otherwise, return `false`.

A string `s` is a subsequence of string `t` if deleting some number of characters from `t` (possibly zero) results in the string `s`.

Constraints:
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist only of lowercase English letters.
"""

def canMakeSubsequence(s: str, t: str) -> bool:
    """
    Determines if string `s` can be made a subsequence of string `t` using cyclic increments.

    Args:
    s (str): The string to transform.
    t (str): The target string.

    Returns:
    bool: True if `s` can be made a subsequence of `t`, False otherwise.
    """
    i, j = 0, 0  # Pointers for s and t
    while i < len(s) and j < len(t):
        # Check if characters match directly or via cyclic increment
        if s[i] == t[j] or (ord(s[i]) - ord('a') + 1) % 26 == (ord(t[j]) - ord('a')):
            i += 1  # Move to the next character in s
        j += 1  # Always move to the next character in t
    return i == len(s)  # If we processed all of s, return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple match
    s1, t1 = "abc", "ahbgdc"
    print(canMakeSubsequence(s1, t1))  # Expected: True

    # Test Case 2: Requires cyclic increment
    s2, t2 = "az", "ayz"
    print(canMakeSubsequence(s2, t2))  # Expected: True

    # Test Case 3: Not possible to form subsequence
    s3, t3 = "abc", "def"
    print(canMakeSubsequence(s3, t3))  # Expected: False

    # Test Case 4: Edge case with single character
    s4, t4 = "a", "z"
    print(canMakeSubsequence(s4, t4))  # Expected: True

    # Test Case 5: Edge case with large input
    s5, t5 = "a" * 10**5, "a" * 10**5
    print(canMakeSubsequence(s5, t5))  # Expected: True

"""
Time Complexity:
- The algorithm processes each character of `t` at most once, and each character of `s` at most once.
- Therefore, the time complexity is O(n + m), where `n` is the length of `s` and `m` is the length of `t`.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Strings, Two Pointers
"""