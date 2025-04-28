"""
LeetCode Problem #2116: Check if a Parentheses String Can Be Valid

Problem Statement:
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if at any moment 
the number of ')' characters never exceeds the number of '(' characters, and the total number of '(' 
characters is equal to the total number of ')' characters.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary 
string consisting only of '0's and '1's. A '0' means that the corresponding character in `s` can be 
changed to either '(' or ')', while a '1' means that the corresponding character in `s` cannot be changed.

Return `true` if you can make `s` a valid parentheses string. Otherwise, return `false`.

Constraints:
- `n == s.length == locked.length`
- `1 <= n <= 10^5`
- `s[i]` is either '(' or ')'.
- `locked[i]` is either '0' or '1'.

Example 1:
Input: s = "))()))", locked = "010100"
Output: true
Explanation: We can change the first and last parentheses to '(' to make the string valid.

Example 2:
Input: s = "()()", locked = "1111"
Output: true
Explanation: The string is already valid.

Example 3:
Input: s = ")", locked = "0"
Output: false
Explanation: There is no way to make the string valid.

"""

def canBeValid(s: str, locked: str) -> bool:
    # If the length of the string is odd, it's impossible to make it valid
    if len(s) % 2 != 0:
        return False

    # Forward pass: Check if we can balance '('
    open_count = 0
    for i in range(len(s)):
        if locked[i] == '0' or s[i] == '(':
            open_count += 1
        else:
            open_count -= 1
        if open_count < 0:
            return False

    # Backward pass: Check if we can balance ')'
    close_count = 0
    for i in range(len(s) - 1, -1, -1):
        if locked[i] == '0' or s[i] == ')':
            close_count += 1
        else:
            close_count -= 1
        if close_count < 0:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "))()))"
    locked1 = "010100"
    print(canBeValid(s1, locked1))  # Output: True

    # Test Case 2
    s2 = "()()"
    locked2 = "1111"
    print(canBeValid(s2, locked2))  # Output: True

    # Test Case 3
    s3 = ")"
    locked3 = "0"
    print(canBeValid(s3, locked3))  # Output: False

    # Test Case 4
    s4 = "((("
    locked4 = "000"
    print(canBeValid(s4, locked4))  # Output: False

    # Test Case 5
    s5 = "(()))"
    locked5 = "11001"
    print(canBeValid(s5, locked5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves two linear passes over the string `s` (one forward and one backward).
- Each pass takes O(n) time, where `n` is the length of the string.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space for variables like `open_count` and `close_count`.
- Thus, the space complexity is O(1).

Topic: Strings, Greedy
"""