"""
LeetCode Question #772: Basic Calculator III

Problem Statement:
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, non-negative integers, and the multiplication `*` and division `/` operators. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note:
- You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 4:
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12

Example 5:
Input: s = "0"
Output: 0

Constraints:
- 1 <= s.length <= 10^4
- s consists of digits, `+`, `-`, `*`, `/`, `(`, `)`, and spaces.
- s is a valid expression.
"""

def calculate(s: str) -> int:
    def evaluate(stack):
        """Helper function to evaluate the stack."""
        res = stack.pop() if stack else 0
        while stack and stack[-1] != "(":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            elif sign == "-":
                res -= stack.pop()
        return res

    stack = []
    num = 0
    sign = "+"
    i = 0

    while i < len(s):
        char = s[i]
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "(":
            stack.append(sign)
            stack.append("(")
            sign = "+"
            num = 0
        elif char in "+-*/)":
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))  # Truncate toward zero
            if char == ")":
                num = evaluate(stack)
                stack.pop()  # Remove the "("
            else:
                num = 0
                sign = char
        i += 1

    # Final evaluation for any remaining numbers in the stack
    if sign == "+":
        stack.append(num)
    elif sign == "-":
        stack.append(-num)
    elif sign == "*":
        stack.append(stack.pop() * num)
    elif sign == "/":
        stack.append(int(stack.pop() / num))

    return evaluate(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1+1"
    print(calculate(s1))  # Output: 2

    # Test Case 2
    s2 = "6-4/2"
    print(calculate(s2))  # Output: 4

    # Test Case 3
    s3 = "2*(5+5*2)/3+(6/2+8)"
    print(calculate(s3))  # Output: 21

    # Test Case 4
    s4 = "(2+6*3+5-(3*14/7+2)*5)+3"
    print(calculate(s4))  # Output: -12

    # Test Case 5
    s5 = "0"
    print(calculate(s5))  # Output: 0

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - Each character in the string is processed once, and operations like addition, subtraction, multiplication, and division are O(1).
# - Parentheses are handled using a stack, which adds a constant overhead for each opening and closing parenthesis.

# Space Complexity: O(n)
# - The stack is used to store intermediate results and operators. In the worst case, the stack size can grow to O(n) for deeply nested parentheses.

# Topic: Stack