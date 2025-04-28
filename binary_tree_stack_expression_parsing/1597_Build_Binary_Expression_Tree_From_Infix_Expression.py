"""
LeetCode Problem #1597: Build Binary Expression Tree From Infix Expression

Problem Statement:
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. 
Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with no children) 
represent operands (numbers), and non-leaf nodes represent the operators (+, -, *, /).

Given a string `s` that represents an infix expression, construct the binary expression tree of the expression 
and return its root. The input expression is guaranteed to be valid and consists of digits and the operators 
`+`, `-`, `*`, and `/`. All operands are positive integers, and the expression does not contain any spaces.

Note:
- You may assume that the input expression is always valid.
- The order of operations follows the standard precedence rules: 
  `*` and `/` have higher precedence than `+` and `-`.
- Parentheses can override precedence rules.

Example 1:
Input: s = "3*4-2*5"
Output: The root node of the binary expression tree representing the expression.

Example 2:
Input: s = "2+3/(5*2)"
Output: The root node of the binary expression tree representing the expression.

Constraints:
- 1 <= s.length <= 100
- `s` consists of digits and the operators `+`, `-`, `*`, and `/`.
- All integer values are positive and in the range [1, 99].
- The expression is guaranteed to be valid and does not contain any spaces.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> TreeNode:
        # Helper function to determine operator precedence
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        # Helper function to build a tree node from an operator and its operands
        def build(op, left, right):
            return TreeNode(op, left, right)

        # Shunting-yard algorithm to convert infix expression to postfix
        operators = []
        operands = []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                # Parse the number
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                operands.append(TreeNode(str(num)))
                continue
            elif s[i] == '(':
                operators.append(s[i])
            elif s[i] == ')':
                while operators and operators[-1] != '(':
                    op = operators.pop()
                    right = operands.pop()
                    left = operands.pop()
                    operands.append(build(op, left, right))
                operators.pop()  # Pop the '('
            else:  # Operator
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(s[i])):
                    op = operators.pop()
                    right = operands.pop()
                    left = operands.pop()
                    operands.append(build(op, left, right))
                operators.append(s[i])
            i += 1

        # Process remaining operators
        while operators:
            op = operators.pop()
            right = operands.pop()
            left = operands.pop()
            operands.append(build(op, left, right))

        return operands[-1]

# Example Test Cases
def print_tree(node):
    """Helper function to print the tree in pre-order traversal."""
    if not node:
        return ""
    left = print_tree(node.left)
    right = print_tree(node.right)
    return f"{node.val}({left},{right})" if left or right else f"{node.val}"

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "3*4-2*5"
    root1 = solution.expTree(s1)
    print("Test Case 1:", print_tree(root1))  # Expected: "-(*3,(*4,(*2,5)))"

    # Test Case 2
    s2 = "2+3/(5*2)"
    root2 = solution.expTree(s2)
    print("Test Case 2:", print_tree(root2))  # Expected: "+(2,/(3,*(5,2)))"

    # Test Case 3
    s3 = "1+2*3-4"
    root3 = solution.expTree(s3)
    print("Test Case 3:", print_tree(root3))  # Expected: "-(+(1,*(2,3)),4)"

"""
Time Complexity:
- Parsing the string and processing each character takes O(n), where n is the length of the string.
- Each operator is pushed and popped from the stack at most once, so the overall complexity is O(n).

Space Complexity:
- The space used by the operators stack and operands stack is O(n) in the worst case.
- The space used by the tree nodes is also O(n).
- Overall space complexity is O(n).

Topic: Binary Tree, Stack, Expression Parsing
"""