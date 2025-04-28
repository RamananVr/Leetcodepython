"""
LeetCode Problem #1628: Design an Expression Tree With Evaluate Function

Problem Statement:
Design an expression tree where each node is an operator (+, -, *, /) or an integer. Implement the `TreeBuilder` class that builds the tree from a postfix expression and the `Node` class that evaluates the tree.

The `TreeBuilder` class should have the following methods:
1. `buildTree(postfix: List[str]) -> 'Node'`: This method takes a list of strings representing a postfix expression and returns the root node of the expression tree.

The `Node` class should have the following methods:
1. `evaluate() -> int`: This method evaluates the expression tree and returns the result.

Constraints:
- The input postfix expression is guaranteed to be valid.
- Division is integer division (truncate towards zero).
- The operators are limited to +, -, *, and /.
- The input expression contains only integers and operators.

Example:
Input: ["3", "4", "+", "2", "*", "7", "/"]
Output: 2
Explanation: The expression tree represents the expression ((3 + 4) * 2) / 7, which evaluates to 2.
"""

from typing import List

class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        if self.value.isdigit() or (self.value[0] == '-' and self.value[1:].isdigit()):
            return int(self.value)
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()
        if self.value == '+':
            return left_value + right_value
        elif self.value == '-':
            return left_value - right_value
        elif self.value == '*':
            return left_value * right_value
        elif self.value == '/':
            return left_value // right_value

class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(Node(token))
            else:
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack[-1]

# Example Test Cases
if __name__ == "__main__":
    tree_builder = TreeBuilder()

    # Test Case 1
    postfix1 = ["3", "4", "+", "2", "*", "7", "/"]
    root1 = tree_builder.buildTree(postfix1)
    print(root1.evaluate())  # Output: 2

    # Test Case 2
    postfix2 = ["2", "3", "4", "*", "+"]
    root2 = tree_builder.buildTree(postfix2)
    print(root2.evaluate())  # Output: 14

    # Test Case 3
    postfix3 = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    root3 = tree_builder.buildTree(postfix3)
    print(root3.evaluate())  # Output: 14

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `buildTree` method processes each token in the postfix expression exactly once, so its time complexity is O(n), where n is the length of the postfix expression.
   - The `evaluate` method traverses the tree recursively, visiting each node once. Since the tree has n nodes, the time complexity of evaluation is O(n).
   - Overall time complexity: O(n).

2. Space Complexity:
   - The `buildTree` method uses a stack to store nodes during construction. In the worst case, the stack size can grow to O(n).
   - The expression tree itself contains n nodes, so the space complexity for storing the tree is O(n).
   - Overall space complexity: O(n).

Topic: Binary Tree
"""