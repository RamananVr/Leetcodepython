"""
LeetCode Problem #1328: Break a Palindrome

Problem Statement:
Given a palindromic string `palindrome` consisting of only lowercase English letters, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"

Example 2:
Input: palindrome = "a"
Output: ""

Constraints:
- 1 <= palindrome.length <= 1000
- `palindrome` consists of only lowercase English letters.
"""

def breakPalindrome(palindrome: str) -> str:
    # If the length of the palindrome is 1, it's impossible to make it non-palindromic
    if len(palindrome) == 1:
        return ""
    
    # Convert the string to a list for easier manipulation
    chars = list(palindrome)
    n = len(chars)
    
    # Iterate through the first half of the string
    for i in range(n // 2):
        # Replace the first non-'a' character with 'a'
        if chars[i] != 'a':
            chars[i] = 'a'
            return "".join(chars)
    
    # If all characters in the first half are 'a', replace the last character with 'b'
    chars[-1] = 'b'
    return "".join(chars)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    palindrome = "abccba"
    print(breakPalindrome(palindrome))  # Output: "aaccba"

    # Test Case 2
    palindrome = "a"
    print(breakPalindrome(palindrome))  # Output: ""

    # Test Case 3
    palindrome = "aaaa"
    print(breakPalindrome(palindrome))  # Output: "aaab"

    # Test Case 4
    palindrome = "racecar"
    print(breakPalindrome(palindrome))  # Output: "aacecar"

    # Test Case 5
    palindrome = "aaaabaaa"
    print(breakPalindrome(palindrome))  # Output: "aaabaaaa"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through at most half of the string (n // 2), making the time complexity O(n), where n is the length of the input string.

Space Complexity:
- The algorithm uses O(n) space to store the list representation of the string. However, if we consider the input and output strings as part of the problem constraints, the space complexity is O(1) for additional space usage.

Topic: Strings
"""