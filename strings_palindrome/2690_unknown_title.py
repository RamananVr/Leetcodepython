"""
LeetCode Problem #2690: Infinite Process in a String

Problem Statement:
You are given a string `s` consisting of lowercase English letters. You can perform the following operation on the string any number of times:

- Choose any character in the string and replace it with the character that comes immediately after it in the English alphabet. For example, 'a' becomes 'b', 'b' becomes 'c', ..., and 'z' becomes 'a'.

Your task is to determine if it is possible to make the string `s` a palindrome by performing the above operation any number of times.

A string is a palindrome if it reads the same backward as forward.

Return `True` if it is possible to make the string a palindrome, otherwise return `False`.

Constraints:
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.

Example:
Input: s = "abc"
Output: False

Input: s = "aab"
Output: True
"""

# Solution
def canMakePalindrome(s: str) -> bool:
    """
    Determines if it is possible to make the string `s` a palindrome by replacing
    characters with their next alphabetic character any number of times.

    :param s: Input string consisting of lowercase English letters
    :return: True if it is possible to make the string a palindrome, False otherwise
    """
    # Count the frequency of each character
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1

    # Count the number of characters with odd frequencies
    odd_count = sum(f % 2 for f in freq)

    # A string can be rearranged into a palindrome if at most one character has an odd frequency
    return odd_count <= 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    print(canMakePalindrome(s1))  # Output: False

    # Test Case 2
    s2 = "aab"
    print(canMakePalindrome(s2))  # Output: True

    # Test Case 3
    s3 = "racecar"
    print(canMakePalindrome(s3))  # Output: True

    # Test Case 4
    s4 = "abcd"
    print(canMakePalindrome(s4))  # Output: False

    # Test Case 5
    s5 = "a"
    print(canMakePalindrome(s5))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters in the string takes O(n), where n is the length of the string.
- Summing the odd frequencies takes O(26) = O(1), as the alphabet size is constant.
- Overall time complexity: O(n).

Space Complexity:
- We use an array of size 26 to store character frequencies, which is O(1) space.
- Overall space complexity: O(1).

Topic: Strings, Palindrome
"""