"""
LeetCode Question #32: Longest Valid Parentheses

Problem Statement:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 10^4
- s[i] is either '(' or ')'.
"""

def longestValidParentheses(s: str) -> int:
    """
    Finds the length of the longest valid parentheses substring.

    :param s: Input string containing '(' and ')'
    :return: Length of the longest valid parentheses substring
    """
    stack = []
    max_length = 0
    # Initialize a base index for valid substrings
    base_index = -1

    for i, char in enumerate(s):
        if char == '(':
            # Push the index of '(' onto the stack
            stack.append(i)
        else:
            # If the stack is not empty, pop the last '(' index
            if stack:
                stack.pop()
                # If the stack is empty, calculate the length using base_index
                if not stack:
                    max_length = max(max_length, i - base_index)
                else:
                    # Otherwise, calculate the length using the last unmatched '(' index
                    max_length = max(max_length, i - stack[-1])
            else:
                # Update base_index for unmatched ')'
                base_index = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(()"
    print(longestValidParentheses(s1))  # Output: 2

    # Test Case 2
    s2 = ")()())"
    print(longestValidParentheses(s2))  # Output: 4

    # Test Case 3
    s3 = ""
    print(longestValidParentheses(s3))  # Output: 0

    # Test Case 4
    s4 = "())((())"
    print(longestValidParentheses(s4))  # Output: 4

    # Test Case 5
    s5 = "((((((((("
    print(longestValidParentheses(s5))  # Output: 0

"""
Topic: Stack
"""