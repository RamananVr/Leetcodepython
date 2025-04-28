"""
LeetCode Problem #150: Evaluate Reverse Polish Notation

Problem Statement:
You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (RPN).

Evaluate the expression. Return an integer that represents the result.

Note:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- Division between two integers should truncate toward zero.
- The given `tokens` array will always be valid RPN. That means the expression is guaranteed to evaluate to a single result, and there will be no division by zero.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
  = ((10 * (6 / -132)) + 17) + 5
  = ((10 * 0) + 17) + 5
  = (0 + 17) + 5
  = 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

# Solution
def evalRPN(tokens):
    """
    Evaluate the Reverse Polish Notation (RPN) expression.

    :param tokens: List[str] - The RPN expression as a list of strings.
    :return: int - The result of the evaluation.
    """
    stack = []
    
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            # Pop the last two operands from the stack
            b = stack.pop()
            a = stack.pop()
            
            # Perform the operation
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Integer division truncating toward zero
                stack.append(int(a / b))
        else:
            # Push the operand onto the stack
            stack.append(int(token))
    
    # The final result will be the only element in the stack
    return stack[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens1))  # Output: 9

    # Test Case 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(evalRPN(tokens2))  # Output: 6

    # Test Case 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens3))  # Output: 22

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each token is processed exactly once, and each operation (push, pop, arithmetic) takes O(1).
- Therefore, the time complexity is O(n), where n is the number of tokens.

Space Complexity:
- The space complexity is O(n) in the worst case, where all tokens are operands and are pushed onto the stack.
"""

# Topic: Stack