"""
LeetCode Problem #2414: Length of the Longest Alphabetical Continuous Substring

Problem Statement:
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. 
In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

- For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.

Given a string `s` consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

Example 1:
Input: s = "abacaba"
Output: 2
Explanation: There are 4 alphabetical continuous substrings: "ab", "ba", "ac" and "ab". 
The longest one is "ab" with a length of 2.

Example 2:
Input: s = "abcde"
Output: 5
Explanation: "abcde" is an alphabetical continuous string with length 5.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only English lowercase letters.
"""

# Python Solution
def longestContinuousSubstring(s: str) -> int:
    if not s:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(s)):
        # Check if the current character is consecutive to the previous one
        if ord(s[i]) - ord(s[i - 1]) == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1  # Reset the current length

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abacaba"
    print(f"Input: {s1} -> Output: {longestContinuousSubstring(s1)}")  # Expected: 2

    # Test Case 2
    s2 = "abcde"
    print(f"Input: {s2} -> Output: {longestContinuousSubstring(s2)}")  # Expected: 5

    # Test Case 3
    s3 = "z"
    print(f"Input: {s3} -> Output: {longestContinuousSubstring(s3)}")  # Expected: 1

    # Test Case 4
    s4 = "xyzabc"
    print(f"Input: {s4} -> Output: {longestContinuousSubstring(s4)}")  # Expected: 3

    # Test Case 5
    s5 = "a"
    print(f"Input: {s5} -> Output: {longestContinuousSubstring(s5)}")  # Expected: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a constant amount of extra space for variables like `max_length` and `current_length`.
- Therefore, the space complexity is O(1).
"""

# Topic: Strings