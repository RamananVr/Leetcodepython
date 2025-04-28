"""
LeetCode Problem #2764: "Find the Longest Semi-Repetitive Substring"

Problem Statement:
You are given a string `s` consisting of digits from '0' to '9'. A substring is called semi-repetitive if at most one 
adjacent pair of the same digit exists in the substring. Return the length of the longest semi-repetitive substring 
of `s`.

Example:
Input: s = "52233"
Output: 4
Explanation: The substring "5223" is semi-repetitive.

Constraints:
- 1 <= s.length <= 10^5
- s consists of digits from '0' to '9'.
"""

def longestSemiRepetitiveSubstring(s: str) -> int:
    """
    Finds the length of the longest semi-repetitive substring in the given string.

    :param s: A string consisting of digits from '0' to '9'.
    :return: The length of the longest semi-repetitive substring.
    """
    n = len(s)
    max_length = 0
    last_repeat = -1  # Index of the last repeated character
    prev_repeat = -1  # Index of the second-to-last repeated character
    start = 0  # Start of the current substring

    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            prev_repeat = last_repeat
            last_repeat = i
            start = prev_repeat + 1 if prev_repeat != -1 else start
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
    s5 = "999999999"
    print(longestSemiRepetitiveSubstring(s5))  # Output: 2


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (`last_repeat`, `prev_repeat`, `start`, etc.).
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""