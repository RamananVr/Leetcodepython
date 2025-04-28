"""
LeetCode Problem #2124: Check if All A's Appears Before All B's

Problem Statement:
Given a string `s` consisting of only the characters 'a' and 'b', return `true` if every 'a' appears before every 'b' in the string. Otherwise, return `false`.

Example 1:
Input: s = "aaabbb"
Output: true
Explanation: All 'a's appear before all 'b's.

Example 2:
Input: s = "abab"
Output: false
Explanation: There is an 'a' after a 'b'.

Example 3:
Input: s = "bbb"
Output: true
Explanation: There are no 'a's, so the condition is trivially satisfied.

Constraints:
- 1 <= s.length <= 100
- s[i] is either 'a' or 'b'.
"""

# Solution
def checkString(s: str) -> bool:
    """
    Function to check if all 'a's appear before all 'b's in the given string.

    :param s: A string consisting of only 'a' and 'b'.
    :return: True if all 'a's appear before all 'b's, False otherwise.
    """
    # Iterate through the string and check if 'b' appears before 'a'
    seen_b = False
    for char in s:
        if char == 'b':
            seen_b = True
        elif char == 'a' and seen_b:
            return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaabbb"
    print(checkString(s1))  # Output: True

    # Test Case 2
    s2 = "abab"
    print(checkString(s2))  # Output: False

    # Test Case 3
    s3 = "bbb"
    print(checkString(s3))  # Output: True

    # Test Case 4
    s4 = "a"
    print(checkString(s4))  # Output: True

    # Test Case 5
    s5 = "b"
    print(checkString(s5))  # Output: True

    # Test Case 6
    s6 = "aaabbbaaa"
    print(checkString(s6))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the string once, performing constant-time operations for each character.
Thus, the time complexity is O(n), where n is the length of the string.

Space Complexity:
The function uses a single boolean variable (`seen_b`) to track whether a 'b' has been encountered.
Thus, the space complexity is O(1).
"""

# Topic: Strings