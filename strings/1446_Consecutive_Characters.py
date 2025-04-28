"""
LeetCode Problem #1446: Consecutive Characters

Problem Statement:
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string `s`, return the power of `s`.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
Input: s = "triplepillooooow"
Output: 5

Example 4:
Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:
Input: s = "tourist"
Output: 1

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters.
"""

def maxPower(s: str) -> int:
    """
    Function to calculate the power of the string, which is the maximum length
    of a substring containing only one unique character.

    :param s: Input string
    :return: Maximum power of the string
    """
    max_power = 1  # At least one character will always have a power of 1
    current_power = 1  # Tracks the length of the current streak of the same character

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # If the current character matches the previous one
            current_power += 1
            max_power = max(max_power, current_power)  # Update max_power if needed
        else:
            current_power = 1  # Reset the streak for a new character

    return max_power


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcode"
    print(maxPower(s1))  # Output: 2

    # Test Case 2
    s2 = "abbcccddddeeeeedcba"
    print(maxPower(s2))  # Output: 5

    # Test Case 3
    s3 = "triplepillooooow"
    print(maxPower(s3))  # Output: 5

    # Test Case 4
    s4 = "hooraaaaaaaaaaay"
    print(maxPower(s4))  # Output: 11

    # Test Case 5
    s5 = "tourist"
    print(maxPower(s5))  # Output: 1


"""
Time Complexity Analysis:
- The function iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The function uses a constant amount of extra space (variables `max_power` and `current_power`).
- Therefore, the space complexity is O(1).

Topic: Strings
"""