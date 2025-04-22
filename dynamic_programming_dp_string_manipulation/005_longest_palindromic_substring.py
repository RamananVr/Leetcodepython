"""
LeetCode Question #5: Longest Palindromic Substring

Problem Statement:
Given a string `s`, return the longest palindromic substring in `s`.

A string is called a palindrome when it reads the same backward as forward. For example, "aba" is a palindrome, while "abc" is not.

Constraints:
- 1 <= s.length <= 1000
- s consists of only digits and English letters.
"""

def longestPalindrome(s: str) -> str:
    """
    This function finds the longest palindromic substring in the given string `s`.
    """
    if len(s) <= 1:
        return s

    start, max_length = 0, 0

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                start = left
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd-length palindromes (single character center)
        expand_around_center(i, i)
        # Even-length palindromes (two character center)
        expand_around_center(i, i + 1)

    return s[start:start + max_length]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "babad"
    print(longestPalindrome(s1))  # Output: "bab" or "aba"

    # Test Case 2
    s2 = "cbbd"
    print(longestPalindrome(s2))  # Output: "bb"

    # Test Case 3
    s3 = "a"
    print(longestPalindrome(s3))  # Output: "a"

    # Test Case 4
    s4 = "ac"
    print(longestPalindrome(s4))  # Output: "a" or "c"

    # Test Case 5
    s5 = "racecar"
    print(longestPalindrome(s5))  # Output: "racecar"

# Topic: Dynamic Programming (DP) / String Manipulation