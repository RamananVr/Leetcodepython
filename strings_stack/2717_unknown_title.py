"""
LeetCode Problem #2717: Semi-Valid Parentheses

Problem Statement:
You are given a string `s` consisting of only '(' and ')'. A string is called semi-valid parentheses if:
1. It is valid parentheses, or
2. By removing at most one character from the string, it becomes valid parentheses.

Return `True` if the given string `s` is semi-valid parentheses, otherwise return `False`.

A string is valid parentheses if:
- Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
- Parentheses are properly nested.

Constraints:
- 1 <= len(s) <= 10^5
- s consists of '(' and ')'.

"""

# Solution
def isSemiValidParentheses(s: str) -> bool:
    def isValidParentheses(s: str) -> bool:
        # Helper function to check if a string is valid parentheses
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:  # More closing parentheses than opening
                return False
        return balance == 0  # All opening parentheses are matched

    # Check if the string is already valid
    if isValidParentheses(s):
        return True

    # Try removing one character and check if it becomes valid
    for i in range(len(s)):
        if isValidParentheses(s[:i] + s[i+1:]):
            return True

    return False


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Already valid parentheses
    s1 = "()()"
    print(isSemiValidParentheses(s1))  # Expected output: True

    # Test Case 2: Semi-valid by removing one character
    s2 = "(()))"
    print(isSemiValidParentheses(s2))  # Expected output: True

    # Test Case 3: Not semi-valid
    s3 = ")))"
    print(isSemiValidParentheses(s3))  # Expected output: False

    # Test Case 4: Semi-valid by removing one character
    s4 = "((())"
    print(isSemiValidParentheses(s4))  # Expected output: True

    # Test Case 5: Single character string
    s5 = "("
    print(isSemiValidParentheses(s5))  # Expected output: True

    # Test Case 6: Empty string (not valid or semi-valid)
    s6 = ""
    print(isSemiValidParentheses(s6))  # Expected output: False


# Time and Space Complexity Analysis
"""
Time Complexity:
- The `isValidParentheses` function runs in O(n), where n is the length of the string.
- In the worst case, we call `isValidParentheses` for each character in the string, resulting in O(n^2) complexity.

Space Complexity:
- The space complexity is O(1) since we only use a few variables to track the balance.

Overall:
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# Topic: Strings, Stack