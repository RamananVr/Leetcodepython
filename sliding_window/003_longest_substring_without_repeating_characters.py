"""
LeetCode Question #3: Longest Substring Without Repeating Characters

Problem Statement:
Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols, and spaces.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    # Initialize a set to store characters in the current window
    char_set = set()
    # Initialize pointers for the sliding window
    left = 0
    # Variable to store the maximum length of substring
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(length_of_longest_substring(s1))  # Output: 3

    # Test case 2
    s2 = "bbbbb"
    print(length_of_longest_substring(s2))  # Output: 1

    # Test case 3
    s3 = "pwwkew"
    print(length_of_longest_substring(s3))  # Output: 3

    # Test case 4
    s4 = ""
    print(length_of_longest_substring(s4))  # Output: 0

    # Test case 5
    s5 = " "
    print(length_of_longest_substring(s5))  # Output: 1

    # Test case 6
    s6 = "au"
    print(length_of_longest_substring(s6))  # Output: 2

# Topic: Sliding Window