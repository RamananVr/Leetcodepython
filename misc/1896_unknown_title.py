"""
LeetCode Problem #1896: Minimum Cost to Change the Final Value of Expression

Problem Statement:
You are given a valid boolean expression as a string `expression`, consisting of the characters '1', '0', '&', '|', '(', and ')'.

- '1' represents the boolean value True.
- '0' represents the boolean value False.
- '&' represents the boolean AND operation.
- '|' represents the boolean OR operation.

You are allowed to flip one operation ('&' to '|', or '| to '&') or one boolean value ('1' to '0', or '0' to '1') in the expression. Your task is to return the minimum cost to change the final value of the expression.

Example:
Input: expression = "1&(0|1)"
Output: 1
Explanation: Changing '|' to '&' results in the expression "1&(0&1)", which evaluates to False.

Constraints:
- 1 <= expression.length <= 10^5
- `expression` contains only '1', '0', '&', '|', '(', and ')'.
- `expression` is a valid boolean expression.

"""

# Solution
def minOperationsToFlip(expression: str) -> int:
    def evaluate(expr, start, end):
        stack = []
        i = start
        while i <= end:
            if expr[i] == '(':
                # Find the matching closing parenthesis
                open_count = 1
                j = i + 1
                while j <= end and open_count > 0:
                    if expr[j] == '(':
                        open_count += 1
                    elif expr[j] == ')':
                        open_count -= 1
                    j += 1
                # Evaluate the sub-expression
                value, flip_cost = evaluate(expr, i + 1, j - 2)
                stack.append((value, flip_cost))
                i = j
            elif expr[i] in '01':
                stack.append((int(expr[i]), 1))
                i += 1
            elif expr[i] in '&|':
                stack.append(expr[i])
                i += 1
            else:
                i += 1
        return stack[0]
# Example Test Cases