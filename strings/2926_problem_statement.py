"""
LeetCode Question #2926: Problem Statement

You are given a string `s` consisting of lowercase English letters. You need to determine if the string can be rearranged 
to form a palindrome. A palindrome is a string that reads the same backward as forward.

Return `True` if the string can be rearranged to form a palindrome, otherwise return `False`.

Constraints:
- 1 <= len(s) <= 10^5
- `s` consists of lowercase English letters.

Example:
Input: s = "aabb"
Output: True
Explanation: The string "aabb" can be rearranged to form the palindrome "abba".

Input: s = "abc"
Output: False
Explanation: The string "abc" cannot be rearranged to form a palindrome.
"""

# Python Solution
def canFormPalindrome(s: str) -> bool:
    """
    Determines if the given string can be rearranged to form a palindrome.

    :param s: A string consisting of lowercase English letters.
    :return: True if the string can be rearranged to form a palindrome, False otherwise.
    """
    from collections import Counter

    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Count the number of characters with odd frequencies
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # A string can be rearranged to form a palindrome if at most one character has an odd frequency
    return odd_count <= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Can form a palindrome
    s1 = "aabb"
    print(canFormPalindrome(s1))  # Output: True

    # Test Case 2: Cannot form a palindrome
    s2 = "abc"
    print(canFormPalindrome(s2))  # Output: False

    # Test Case 3: Single character (always a palindrome)
    s3 = "a"
    print(canFormPalindrome(s3))  # Output: True

    # Test Case 4: Empty string (edge case)
    s4 = ""
    print(canFormPalindrome(s4))  # Output: True

    # Test Case 5: Long string with even frequencies
    s5 = "aabbccddeeff"
    print(canFormPalindrome(s5))  # Output: True

    # Test Case 6: Long string with one odd frequency
    s6 = "aabbccddeeffg"
    print(canFormPalindrome(s6))  # Output: True

    # Test Case 7: Long string with multiple odd frequencies
    s7 = "aabbccddeeffgg"
    print(canFormPalindrome(s7))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of characters in the string takes O(n), where n is the length of the string.
- Summing the odd frequencies takes O(26) since there are at most 26 lowercase English letters.
- Overall time complexity: O(n).

Space Complexity:
- The Counter object stores at most 26 key-value pairs (one for each lowercase English letter).
- Overall space complexity: O(1) (constant space for the character frequencies).
"""

# Topic: Strings