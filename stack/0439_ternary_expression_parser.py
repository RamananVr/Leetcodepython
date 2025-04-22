"""
LeetCode Question #439: Ternary Expression Parser

Problem Statement:
Given a string `expression` representing a ternary expression, return the result of evaluating it.

A ternary expression is of the form `condition ? value1 : value2`, where `condition` evaluates to either `true` or `false`.
If the condition is `true`, the expression evaluates to `value1`. Otherwise, it evaluates to `value2`.

The `expression` may contain nested ternary expressions. You must evaluate the innermost expressions first.

Constraints:
- The length of `expression` is between 1 and 10^4.
- The `expression` contains only the characters `0-9`, `?`, `:`, `T`, and `F`.
- It is guaranteed that the `expression` is valid and follows the ternary expression syntax.

Example:
Input: expression = "T?2:3"
Output: "2"

Input: expression = "F?1:T?4:5"
Output: "4"

Input: expression = "T?T?F:5:3"
Output: "F"
"""

# Python Solution
def parseTernary(expression: str) -> str:
    stack = []
    n = len(expression)
    
    # Traverse the expression from right to left
    for i in range(n - 1, -1, -1):
        char = expression[i]
        
        if stack and stack[-1] == '?':  # Found a ternary operator
            stack.pop()  # Remove '?'
            true_val = stack.pop()  # Value if condition is true
            stack.pop()  # Remove ':'
            false_val = stack.pop()  # Value if condition is false
            
            # Evaluate the condition
            stack.append(true_val if char == 'T' else false_val)
        else:
            stack.append(char)
    
    # The final result will be at the top of the stack
    return stack[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "T?2:3"
    print(parseTernary(expression1))  # Output: "2"

    # Test Case 2
    expression2 = "F?1:T?4:5"
    print(parseTernary(expression2))  # Output: "4"

    # Test Case 3
    expression3 = "T?T?F:5:3"
    print(parseTernary(expression3))  # Output: "F"

    # Test Case 4
    expression4 = "F?F?1:2:T?3:4"
    print(parseTernary(expression4))  # Output: "3"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm processes each character of the input string exactly once.
- Therefore, the time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The algorithm uses a stack to store intermediate results. In the worst case, the stack size can grow to O(n).
- Therefore, the space complexity is O(n).
"""

# Topic: Stack