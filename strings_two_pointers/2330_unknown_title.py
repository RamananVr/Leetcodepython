"""
LeetCode Problem #2330: Valid Palindrome IV

Problem Statement:
You are given a string s consisting of lowercase English letters, and you are allowed to perform at most one operation on the string. In one operation, you can remove any character from the string.

Return true if it is possible to make the string a palindrome after at most one operation. Otherwise, return false.

A string is a palindrome if it reads the same forward and backward.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
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
            # Try removing either the left or the right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Removing one character makes it a palindrome
    s1 = "abca"
    print(validPalindrome(s1))  # Expected output: True

    # Test Case 2: Already a palindrome
    s2 = "racecar"
    print(validPalindrome(s2))  # Expected output: True

    # Test Case 3: Cannot be made a palindrome
    s3 = "abc"
    print(validPalindrome(s3))  # Expected output: False

    # Test Case 4: Single character string (always a palindrome)
    s4 = "a"
    print(validPalindrome(s4))  # Expected output: True

    # Test Case 5: Removing one character makes it a palindrome
    s5 = "deified"
    print(validPalindrome(s5))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The main loop runs in O(n), where n is the length of the string.
- The helper function `is_palindrome_range` runs in O(n) in the worst case (when checking the entire substring).
- In the worst case, we call `is_palindrome_range` twice, so the total time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space since it only uses a few pointers and does not allocate extra memory proportional to the input size.

Topic: Strings, Two Pointers
"""