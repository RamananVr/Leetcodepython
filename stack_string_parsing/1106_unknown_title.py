"""
LeetCode Problem #1106: Parsing A Boolean Expression

Problem Statement:
Given a string `expression` representing a boolean expression, return the result of evaluating it.

An expression can either represent:
1. "true" or "false" as a boolean constant,
2. "!(subExpr)" where subExpr is a boolean expression (logical NOT),
3. "&(subExpr1, subExpr2, ...)" where subExpr1, subExpr2, ... are boolean expressions (logical AND),
4. "|(subExpr1, subExpr2, ...)" where subExpr1, subExpr2, ... are boolean expressions (logical OR).

It is guaranteed that the given expression is valid and follows the rules of boolean logic.

Constraints:
- 1 <= expression.length <= 20000
- expression[i] is one of '(', ')', '&', '|', '!', 't', 'f', ','.
- All sub-expressions are guaranteed to be valid.

Example:
Input: expression = "|(&(t,f,t),!(t))"
Output: false
"""

def parseBoolExpr(expression: str) -> bool:
    """
    Evaluates a boolean expression and returns the result.

    :param expression: A string representing a boolean expression.
    :return: A boolean value representing the result of the expression.
    """
    def evaluate(stack):
        operator = stack.pop()
        if operator == '!':
            return not stack.pop()
        elif operator == '&':
            return all(stack)
        elif operator == '|':
            return any(stack)

    stack = []
    for char in expression:
        if char == 't':
            stack.append(True)
        elif char == 'f':
            stack.append(False)
        elif char in '!)|&':
            stack.append(char)
        elif char == ')':
            temp = []
            while stack and stack[-1] not in '!|&':
                temp.append(stack.pop())
            temp.reverse()
            operator = stack.pop()
            stack.append(evaluate(temp + [operator]))
    return stack[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "|(&(t,f,t),!(t))"
    print(parseBoolExpr(expression1))  # Output: False

    # Test Case 2
    expression2 = "&(t,t,t)"
    print(parseBoolExpr(expression2))  # Output: True

    # Test Case 3
    expression3 = "|(f,f,f,t)"
    print(parseBoolExpr(expression3))  # Output: True

    # Test Case 4
    expression4 = "!(f)"
    print(parseBoolExpr(expression4))  # Output: True

    # Test Case 5
    expression5 = "&(t,!(f),|(f,t))"
    print(parseBoolExpr(expression5))  # Output: True

"""
Time Complexity Analysis:
- Parsing the expression involves iterating through the string once, which is O(n), where n is the length of the expression.
- Evaluating the boolean operations involves processing each sub-expression, but each character is processed at most once.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The stack is used to store intermediate results and operators. In the worst case, the stack size can grow to O(n).
- Therefore, the space complexity is O(n).

Topic: Stack, String Parsing
"""