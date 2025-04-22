"""
LeetCode Question #58: Length of Last Word

Problem Statement:
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '.
- There will be at least one word in `s`.
"""

# Python Solution
def lengthOfLastWord(s: str) -> int:
    """
    This function returns the length of the last word in the given string `s`.
    """
    # Strip trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word
    return len(words[-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "Hello World"
    print(lengthOfLastWord(s1))  # Output: 5

    # Test Case 2
    s2 = "   fly me   to   the moon  "
    print(lengthOfLastWord(s2))  # Output: 4

    # Test Case 3
    s3 = "luffy is still joyboy"
    print(lengthOfLastWord(s3))  # Output: 6

    # Test Case 4
    s4 = "a"
    print(lengthOfLastWord(s4))  # Output: 1

    # Test Case 5
    s5 = "day"
    print(lengthOfLastWord(s5))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Stripping trailing spaces and splitting the string into words takes O(n), where n is the length of the string `s`.
- Accessing the last word and calculating its length is O(1).
- Overall time complexity: O(n).

Space Complexity:
- The `split()` function creates a list of words, which in the worst case can take O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Strings