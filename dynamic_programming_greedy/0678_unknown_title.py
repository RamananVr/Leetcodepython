"""
LeetCode Problem #678: Valid Parenthesis String

Problem Statement:
Given a string `s` containing only three types of characters: '(', ')' and '*', 
return `True` if the string is valid.

The string is valid if:
1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' can be treated as a single right parenthesis ')', a single left parenthesis '(',
   or an empty string.

An empty string is also considered valid.

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "(*)"
Output: True

Example 3:
Input: s = "(*))"
Output: True

Constraints:
- 1 <= len(s) <= 100
- s consists of '(' , ')' and '*' characters.
"""

def checkValidString(s: str) -> bool:
    """
    Function to determine if the given string is a valid parenthesis string.
    """
    # Initialize two counters for the range of possible open parentheses
    low = 0  # Minimum number of open parentheses
    high = 0  # Maximum number of open parentheses

    for char in s:
        if char == '(':
            # Increment both counters for an open parenthesis
            low += 1
            high += 1
        elif char == ')':
            # Decrement both counters for a close parenthesis
            low = max(low - 1, 0)  # Ensure low doesn't go below 0
            high -= 1
        elif char == '*':
            # '*' can act as '(', ')' or an empty string
            low = max(low - 1, 0)  # Treat '*' as ')' or empty string
            high += 1  # Treat '*' as '('

        # If high becomes negative, there are unmatched ')' characters
        if high < 0:
            return False

    # If low is 0, all open parentheses are matched
    return low == 0


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "()"
    print(checkValidString(s1))  # Output: True

    # Test Case 2
    s2 = "(*)"
    print(checkValidString(s2))  # Output: True

    # Test Case 3
    s3 = "(*))"
    print(checkValidString(s3))  # Output: True

    # Test Case 4
    s4 = "(((*)"
    print(checkValidString(s4))  # Output: False

    # Test Case 5
    s5 = "(*()"
    print(checkValidString(s5))  # Output: True

    # Test Case 6
    s6 = "(((((*))))"
    print(checkValidString(s6))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The algorithm uses only a few integer variables (`low` and `high`) to track the range of possible open parentheses.
- No additional data structures are used, so the space complexity is O(1).

Topic: Dynamic Programming / Greedy
"""