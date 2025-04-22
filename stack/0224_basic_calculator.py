"""
LeetCode Question #224: Basic Calculator

Problem Statement:
Given a string `s` representing a mathematical expression, implement a basic calculator to evaluate it. 
The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus `-` sign, 
non-negative integers, and empty spaces. The expression is always valid and follows these rules:

1. You may assume that the given expression is always valid.
2. All intermediate results will be in the range of [-2^31, 2^31 - 1].
3. You are not allowed to use any built-in library function to directly evaluate the expression (e.g., `eval()`).

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
- 1 <= s.length <= 3 * 10^5
- `s` consists of digits, '+', '-', '(', ')', and ' '.
- `s` is a valid expression.
"""

# Solution
def calculate(s: str) -> int:
    """
    Evaluate the given mathematical expression string `s`.
    """
    stack = []
    current_number = 0
    result = 0
    sign = 1  # 1 represents positive, -1 represents negative

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+':
            result += sign * current_number
            current_number = 0
            sign = 1
        elif char == '-':
            result += sign * current_number
            current_number = 0
            sign = -1
        elif char == '(':
            # Push the current result and sign onto the stack
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Complete the current number and add it to the result
            result += sign * current_number
            current_number = 0
            # Pop the sign and previous result from the stack
            result *= stack.pop()  # Multiply by the sign
            result += stack.pop()  # Add the previous result
        # Ignore spaces
    result += sign * current_number
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1 + 1"
    print(calculate(s1))  # Output: 2

    # Test Case 2
    s2 = " 2-1 + 2 "
    print(calculate(s2))  # Output: 3

    # Test Case 3
    s3 = "(1+(4+5+2)-3)+(6+8)"
    print(calculate(s3))  # Output: 23

    # Test Case 4
    s4 = "10 - (2 + 3)"
    print(calculate(s4))  # Output: 5

    # Test Case 5
    s5 = "((1+2)-(3-4))"
    print(calculate(s5))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm processes each character in the string `s` exactly once.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The space complexity depends on the stack used to store intermediate results and signs.
- In the worst case, the stack size is proportional to the number of parentheses in the expression.
- Therefore, the space complexity is O(n), where `n` is the length of the string.
"""

# Topic: Stack