"""
LeetCode Problem #1180: Count Substrings with Only One Distinct Letter

Problem Statement:
Given a string `s`, return the number of substrings that have only one distinct letter.

Example:
Input: s = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "a", "a", "a", "aa", "aaa", "b", "a", "a".

Input: s = "aaaa"
Output: 10
Explanation: The substrings with one distinct letter are "a", "a", "a", "a", "aa", "aa", "aa", "aaa", "aaa", "aaaa".

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

# Solution
def countLetters(s: str) -> int:
    """
    Count the number of substrings with only one distinct letter.

    :param s: Input string consisting of lowercase English letters.
    :return: Number of substrings with only one distinct letter.
    """
    count = 0
    length = 1  # Length of the current sequence of identical characters

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            length += 1
        else:
            count += (length * (length + 1)) // 2  # Sum of first `length` natural numbers
            length = 1

    # Add the count for the last sequence
    count += (length * (length + 1)) // 2

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaaba"
    print(countLetters(s1))  # Expected Output: 8

    # Test Case 2
    s2 = "aaaa"
    print(countLetters(s2))  # Expected Output: 10

    # Test Case 3
    s3 = "abc"
    print(countLetters(s3))  # Expected Output: 3

    # Test Case 4
    s4 = "a"
    print(countLetters(s4))  # Expected Output: 1

    # Test Case 5
    s5 = "ababab"
    print(countLetters(s5))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the string once, making it O(n), where n is the length of the string.

Space Complexity:
- The solution uses a constant amount of extra space, making it O(1).

Topic: Strings
"""