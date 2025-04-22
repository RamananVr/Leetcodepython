"""
LeetCode Problem #680: Valid Palindrome II

Problem Statement:
Given a string `s`, return `true` if the `s` can be a palindrome after deleting at most one character from it.

A string is a palindrome when it reads the same backward as forward.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def validPalindrome(s: str) -> bool:
    def is_palindrome_range(left: int, right: int) -> bool:
        """Helper function to check if a substring is a palindrome."""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try skipping either the left or the right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aba"
    print(validPalindrome(s1))  # Output: True

    # Test Case 2
    s2 = "abca"
    print(validPalindrome(s2))  # Output: True

    # Test Case 3
    s3 = "abc"
    print(validPalindrome(s3))  # Output: False

    # Test Case 4
    s4 = "deeee"
    print(validPalindrome(s4))  # Output: True

    # Test Case 5
    s5 = "racecar"
    print(validPalindrome(s5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The main loop runs in O(n), where n is the length of the string.
- The helper function `is_palindrome_range` runs in O(n) in the worst case (when checking the substring).
- Since we call the helper function at most twice, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space since it operates directly on the input string and does not use any extra data structures.

Topic: Strings
"""