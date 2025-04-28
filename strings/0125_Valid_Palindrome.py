"""
LeetCode Problem #125: Valid Palindrome

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: An empty string after removing non-alphanumeric characters is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters.
"""

# Solution
def isPalindrome(s: str) -> bool:
    """
    Determines if the given string is a valid palindrome after removing non-alphanumeric characters
    and converting all characters to lowercase.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the filtered string is equal to its reverse
    return filtered == filtered[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    print(isPalindrome(s1))  # Output: True

    # Test Case 2
    s2 = "race a car"
    print(isPalindrome(s2))  # Output: False

    # Test Case 3
    s3 = " "
    print(isPalindrome(s3))  # Output: True

    # Test Case 4
    s4 = "No lemon, no melon"
    print(isPalindrome(s4))  # Output: True

    # Test Case 5
    s5 = "12321"
    print(isPalindrome(s5))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- Filtering the string takes O(n), where n is the length of the input string `s`.
- Checking if the filtered string is a palindrome takes O(n) as well (due to slicing and comparison).
- Overall time complexity: O(n).

Space Complexity:
- The filtered string requires O(n) space in the worst case (if all characters are alphanumeric).
- Overall space complexity: O(n).
"""

# Topic: Strings