"""
LeetCode Problem #1614: Maximum Nesting Depth of the Parentheses

Problem Statement:
A string is a valid parentheses string (VPS) if it meets one of the following:
- It is an empty string "".
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a VPS represented as a string `s`. Return the maximum nesting depth of the parentheses in `s`.

The nesting depth of a VPS is defined as the maximum depth of nested parentheses. For example:
- "" has a nesting depth of 0.
- "()()" has a nesting depth of 1.
- "(())" has a nesting depth of 2.

Constraints:
- 1 <= s.length <= 100
- s consists of digits 0-9 and characters '(' and ')'.
- It is guaranteed that parentheses in `s` form a valid parentheses string.

Example:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Input: s = "(1)+((2))+(((3)))"
Output: 3
"""

# Solution
def maxDepth(s: str) -> int:
    """
    Calculate the maximum nesting depth of parentheses in the given string.

    :param s: A valid parentheses string containing digits, '(' and ')'.
    :return: Maximum nesting depth of the parentheses.
    """
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return max_depth

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(1+(2*3)+((8)/4))+1"
    print(maxDepth(s1))  # Output: 3

    # Test Case 2
    s2 = "(1)+((2))+(((3)))"
    print(maxDepth(s2))  # Output: 3

    # Test Case 3
    s3 = "1+(2*3)/(2-1)"
    print(maxDepth(s3))  # Output: 1

    # Test Case 4
    s4 = "((()))"
    print(maxDepth(s4))  # Output: 3

    # Test Case 5
    s5 = "()"
    print(maxDepth(s5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a few integer variables (`max_depth` and `current_depth`) to track the depth.
- No additional data structures are used, so the space complexity is O(1).
"""

# Topic: String