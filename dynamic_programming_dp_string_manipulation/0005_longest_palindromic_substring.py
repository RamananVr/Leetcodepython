"""
LeetCode Question #5: Longest Palindromic Substring

Problem Statement:
Given a string `s`, return the longest palindromic substring in `s`.

A string is called a palindrome if it reads the same backward as forward.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.
"""

# Solution
def longestPalindrome(s: str) -> str:
    def expandAroundCenter(left: int, right: int) -> str:
        # Expand around the center while the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        odd_palindrome = expandAroundCenter(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Even-length palindrome
        even_palindrome = expandAroundCenter(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

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

# Time and Space Complexity Analysis
"""
Time Complexity:
The function `expandAroundCenter` is called for each character in the string `s` (both for odd-length and even-length palindromes).
For each call, the expansion can take up to O(n) time in the worst case, where `n` is the length of the string.
Thus, the overall time complexity is O(n^2).

Space Complexity:
The solution uses constant space, as no additional data structures are used apart from variables to store indices and substrings.
Thus, the space complexity is O(1).
"""

# Topic: Dynamic Programming (DP) / String Manipulation