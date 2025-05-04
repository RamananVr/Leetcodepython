"""
LeetCode Question #736: Parse Lisp Expression

Problem Statement:
You are given a string expression representing a Lisp-like expression to evaluate. The syntax for these expressions is as follows:

1. An expression can be either:
   - An integer, e.g., "123".
   - A variable, e.g., "x".
   - A let-expression, e.g., "(let x 2 (mult x 5))".
   - An add-expression, e.g., "(add 1 2)".
   - A mult-expression, e.g., "(mult 3 4)".

2. Expressions are evaluated as follows:
   - An integer evaluates to itself.
   - A variable evaluates to its current value (set by the most recent let-expression).
   - A let-expression assigns values to variables sequentially and evaluates the final expression in its scope.
   - An add-expression evaluates to the sum of two sub-expressions.
   - A mult-expression evaluates to the product of two sub-expressions.

3. There is no whitespace in the input.

4. You may assume the given expression is valid and evaluates to an integer. The result of all intermediate calculations and the final result will fit in a 32-bit signed integer.

Write a function to evaluate the given expression and return its result.

Constraints:
- The input expression is a valid Lisp-like expression.
- The length of the input expression does not exceed 2000 characters.
"""

def evaluate(expression: str) -> int:
    def parse(tokens):
        token = tokens.pop(0)
        if token == '(':
            sub_expr = []
            while tokens[0] != ')':
                sub_expr.append(parse(tokens))
            tokens.pop(0)  # Remove ')'
            return sub_expr
        elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            return int(token)
        else:
            return token

    def eval_expr(expr, scope):
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, str):
            return scope[expr]
        elif expr[0] == 'add':
            return eval_expr(expr[1], scope) + eval_expr(expr[2], scope)
        elif expr[0] == 'mult':
            return eval_expr(expr[1], scope) * eval_expr(expr[2], scope)
        elif expr[0] == 'let':
            new_scope = scope.copy()
            for i in range(1, len(expr) - 1, 2):
                if i + 1 < len(expr):
                    new_scope[expr[i]] = eval_expr(expr[i + 1], new_scope)
            return eval_expr(expr[-1], new_scope)

    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] == '(' or expression[i] == ')':
            tokens.append(expression[i])
            i += 1
        elif expression[i].isalnum() or expression[i] == '-':
            j = i
            while j < len(expression) and (expression[j].isalnum() or expression[j] == '-'):
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            i += 1

    parsed_expr = parse(tokens)
    return eval_expr(parsed_expr, {})

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "(add 1 2)"
    print(evaluate(expression1))  # Output: 3

    # Test Case 2
    expression2 = "(mult 3 (add 2 3))"
    print(evaluate(expression2))  # Output: 15

    # Test Case 3
    expression3 = "(let x 2 (mult x 5))"
    print(evaluate(expression3))  # Output: 10

    # Test Case 4
    expression4 = "(let x 2 (let y 3 (add x y)))"
    print(evaluate(expression4))  # Output: 5

    # Test Case 5
    expression5 = "(let x 2 (let x 3 (let x 4 x)))"
    print(evaluate(expression5))  # Output: 4

    # Test Case 6
    expression6 = "(let a1 3 b2 (add a1 1) b2)"
    print(evaluate(expression6))  # Output: 4

"""
Time Complexity:
- Parsing the expression takes O(n), where n is the length of the input string.
- Evaluating the expression depends on the depth of nested expressions. In the worst case, it could be O(n^2) due to copying the scope for each nested "let" expression.

Space Complexity:
- The space complexity is O(n) for the tokens and O(d) for the scope, where d is the depth of nested expressions.

Topic: Parsing, Recursion
"""