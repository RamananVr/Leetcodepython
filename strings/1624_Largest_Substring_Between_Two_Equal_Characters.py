"""
LeetCode Problem #1624: Largest Substring Between Two Equal Characters

Problem Statement:
Given a string `s`, return the length of the largest substring between two equal characters, 
excluding the two characters. If there is no such substring, return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The substring between the two 'a's is empty.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The substring between the two 'a's is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no two equal characters, so the result is -1.

Example 4:
Input: s = "cabbac"
Output: 4
Explanation: The substring between the two 'c's is "abba".

Constraints:
- 1 <= s.length <= 10^3
- s contains only lowercase English letters.
"""

def maxLengthBetweenEqualCharacters(s: str) -> int:
    """
    Finds the length of the largest substring between two equal characters.

    :param s: Input string
    :return: Length of the largest substring between two equal characters, or -1 if no such substring exists
    """
    # Dictionary to store the first occurrence index of each character
    first_occurrence = {}
    max_length = -1

    for i, char in enumerate(s):
        if char in first_occurrence:
            # Calculate the length of the substring between the two equal characters
            max_length = max(max_length, i - first_occurrence[char] - 1)
        else:
            # Store the first occurrence of the character
            first_occurrence[char] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aa"
    print(maxLengthBetweenEqualCharacters(s1))  # Output: 0

    # Test Case 2
    s2 = "abca"
    print(maxLengthBetweenEqualCharacters(s2))  # Output: 2

    # Test Case 3
    s3 = "cbzxy"
    print(maxLengthBetweenEqualCharacters(s3))  # Output: -1

    # Test Case 4
    s4 = "cabbac"
    print(maxLengthBetweenEqualCharacters(s4))  # Output: 4

    # Test Case 5 (Edge Case: Single character string)
    s5 = "a"
    print(maxLengthBetweenEqualCharacters(s5))  # Output: -1

    # Test Case 6 (Edge Case: All unique characters)
    s6 = "abcdef"
    print(maxLengthBetweenEqualCharacters(s6))  # Output: -1

    # Test Case 7 (Edge Case: Repeated characters with no substring)
    s7 = "aaaa"
    print(maxLengthBetweenEqualCharacters(s7))  # Output: 2

"""
Time Complexity Analysis:
- The function iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The function uses a dictionary to store the first occurrence of each character. 
  In the worst case, the dictionary will store all unique characters in the string.
- Since the input string contains only lowercase English letters, the dictionary can have at most 26 entries.
- Thus, the space complexity is O(1) (constant space).

Topic: Strings
"""