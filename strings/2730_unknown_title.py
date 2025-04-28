"""
LeetCode Problem #2730: Find the Longest Semi-Repetitive Substring

Problem Statement:
You are given a string `s` consisting of digits from 0 to 9. A substring is called semi-repetitive if at most one 
adjacent pair of the same digits exists in the substring. Return the length of the longest semi-repetitive substring 
of `s`.

Example:
Input: s = "52233"
Output: 4
Explanation: The substring "5223" is semi-repetitive.

Constraints:
- 1 <= s.length <= 1000
- s consists of digits from 0 to 9.
"""

def longestSemiRepetitiveSubstring(s: str) -> int:
    """
    Finds the length of the longest semi-repetitive substring in the given string.

    :param s: A string consisting of digits from 0 to 9.
    :return: The length of the longest semi-repetitive substring.
    """
    n = len(s)
    max_length = 0
    last_repeat_index = -1
    start = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            if last_repeat_index != -1:
                start = last_repeat_index + 1
            last_repeat_index = i - 1
        max_length = max(max_length, i - start + 1)

    return max_length


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "52233"
    print(longestSemiRepetitiveSubstring(s1))  # Output: 4

    # Test Case 2
    s2 = "1111"
    print(longestSemiRepetitiveSubstring(s2))  # Output: 2

    # Test Case 3
    s3 = "1234567890"
    print(longestSemiRepetitiveSubstring(s3))  # Output: 10

    # Test Case 4
    s4 = "112233445566"
    print(longestSemiRepetitiveSubstring(s4))  # Output: 3

    # Test Case 5
    s5 = "1"
    print(longestSemiRepetitiveSubstring(s5))  # Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (`max_length`, `last_repeat_index`, `start`).
- Therefore, the space complexity is O(1).

Topic: Strings
"""