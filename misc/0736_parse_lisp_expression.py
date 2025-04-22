"""
LeetCode Question #736: Parse Lisp Expression

Problem Statement:
You are given a string expression representing a Lisp-like expression to evaluate. The expression can be one of the following:
1. An integer literal (e.g., "123").
2. A variable (e.g., "x").
3. Let expressions (e.g., "(let x 2 y 3 (add x y))").
4. Add expressions (e.g., "(add 1 2)").
5. Mult expressions (e.g., "(mult 3 4)").

The expressions are always valid and evaluate to a single integer. The let expressions assign values to variables and evaluate to the value of the last expression in the scope. Variables are lexically scoped, meaning that they are only valid within the block they are defined.

Implement a function `evaluate(expression: str) -> int` that evaluates the given Lisp-like expression and returns the result.

Constraints:
- The input expression is guaranteed to be valid.
- The length of the expression is at most 2000.
- The result of the expression and intermediate calculations are guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: expression = "(let x 2 (mult x 5))"
Output: 10

Example 2:
Input: expression = "(let x 2 y 3 (add x y))"
Output: 5

Example 3:
Input: expression = "(let x 2 y 3 z 4 (add x (mult y z)))"
Output: 14
"""

def evaluate(expression: str) -> int:
    def parse(tokens, scope):
        token = tokens.pop(0)
        if token == '(':
            op = tokens.pop(0)
            if op == 'let':
                new_scope = scope.copy()
                while tokens[0] != '(' and tokens[1] != ')':
                    var = tokens.pop(0)
                    if tokens[0] == '(':
                    else