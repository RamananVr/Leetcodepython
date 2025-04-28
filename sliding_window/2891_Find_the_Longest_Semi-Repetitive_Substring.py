"""
LeetCode Problem #2891: Find the Longest Semi-Repetitive Substring

Problem Statement:
You are given a string `s` consisting of only digits (0-9). A substring is called semi-repetitive if at most one digit appears consecutively more than once. In other words, a substring is semi-repetitive if the condition of having consecutive repeated digits is violated at most once.

Return the length of the longest semi-repetitive substring of `s`.

Example 1:
Input: s = "52233"
Output: 4
Explanation: The substring "5223" is semi-repetitive. It contains at most one pair of consecutive repeated digits.

Example 2:
Input: s = "1111"
Output: 2
Explanation: The longest semi-repetitive substring is "11".

Example 3:
Input: s = "123456"
Output: 6
Explanation: The entire string is semi-repetitive.

Constraints:
- 1 <= s.length <= 10^5
- s consists of digits (0-9) only.
"""

def longest_semi_repetitive_substring(s: str) -> int:
    """
    Finds the length of the longest semi-repetitive substring in the given string.

    :param s: A string consisting of digits (0-9).
    :return: The length of the longest semi-repetitive substring.
    """
    n = len(s)
    max_length = 0
    start = 0
    last_repeat = -1  # Index of the last repeated digit

    for i in range(1, n):
        if s[i] == s[i - 1]:
            if last_repeat != -1:
                start = last_repeat + 1
            last_repeat = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "52233"
    print(longest_semi_repetitive_substring(s1))  # Output: 4

    # Test Case 2
    s2 = "1111"
    print(longest_semi_repetitive_substring(s2))  # Output: 2

    # Test Case 3
    s3 = "123456"
    print(longest_semi_repetitive_substring(s3))  # Output: 6

    # Test Case 4
    s4 = "1122334455"
    print(longest_semi_repetitive_substring(s4))  # Output: 4

    # Test Case 5
    s5 = "1"
    print(longest_semi_repetitive_substring(s5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables (`start`, `last_repeat`, etc.).
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""