"""
LeetCode Question #1896: Minimum Cost to Change the Final Value of Expression

Problem Statement:
You are given a valid boolean expression as a string expression consisting of the characters '1','0','&','|', and parentheses '(' and ')'.

- For example, the cost to change '1' to '0' is 1, and the cost to change '0' to '1' is 1.
- The cost to change '&' to '|' is 1, and the cost to change '|' to '&' is 1.

You want to change the final value of the expression. For example, if the expression evaluates to true, you want to make it false, and vice versa.

Return the minimum cost to achieve that.

Constraints:
- 1 <= expression.length <= 10^5
- expression only contains '1', '0', '&', '|', '(', and ')'.
- All parentheses are properly matched.
"""

# Solution
def minOperationsToFlip(expression: str) -> int:
    def dfs(expr, start):
        stack = []
        i = start
        while i < len(expr):
            if expr[i] == '(':
                val, cost, i = dfs(expr, i + 1)
                stack.append((val, cost))
            elif expr[i] == ')':
                break
            elif expr[i] in '01':
                stack.append((int(expr[i]), 1))
            elif expr[i] in '&|':
                stack.append(expr[i])
            i += 1

        while len(stack) > 1:
            left_val, left_cost = stack.pop(0)
            op = stack.pop(0)
            right_val, right_cost = stack.pop(0)

            if op == '&':
                new_val = left_val & right_val
                new_cost = min(left_cost + (1 - right_val), right_cost + (1 - left_val))
            elif op == '|':
                new_val = left_val | right_val
                new_cost = min(left_cost + right_val, right_cost + left_val)

            stack.insert(0, (new_val, new_cost))

        return stack[0][0], stack[0][1], i

    return dfs(expression, 0)[1]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "1&(0|1)"
    print(minOperationsToFlip(expression1))  # Expected Output: 1

    # Test Case 2
    expression2 = "1|0"
    print(minOperationsToFlip(expression2))  # Expected Output: 1

    # Test Case 3
    expression3 = "0&(1|0)"
    print(minOperationsToFlip(expression3))  # Expected Output: 1

    # Test Case 4
    expression4 = "1"
    print(minOperationsToFlip(expression4))  # Expected Output: 1

    # Test Case 5
    expression5 = "0"
    print(minOperationsToFlip(expression5))  # Expected Output: 1


# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm processes each character in the expression exactly once, and the operations on the stack are constant time.
- Therefore, the time complexity is O(n), where n is the length of the expression.

Space Complexity:
- The space complexity is O(n) due to the stack used for parsing and evaluating the expression.

Overall Complexity:
- Time: O(n)
- Space: O(n)
"""

# Topic: Expression Parsing, Stack, Recursion