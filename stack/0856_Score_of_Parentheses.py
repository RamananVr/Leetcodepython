"""
LeetCode Problem #856: Score of Parentheses

Problem Statement:
Given a balanced parentheses string `s`, compute the score of the string based on the following rules:
1. `()` has a score of 1.
2. `AB` has a score of `A + B`, where `A` and `B` are balanced parentheses strings.
3. `(A)` has a score of `2 * A`, where `A` is a balanced parentheses string.

A balanced parentheses string is a string consisting of `(` and `)` characters, and:
- It is empty, or
- It can be written as `AB` (A concatenated with B), where A and B are balanced parentheses strings, or
- It can be written as `(A)`, where A is a balanced parentheses string.

Example:
Input: s = "()"
Output: 1

Input: s = "(())"
Output: 2

Input: s = "()()"
Output: 2

Constraints:
- 1 <= s.length <= 50
- `s` consists of only `'('` and `')'`.
- `s` is a balanced parentheses string.
"""

# Python Solution
def scoreOfParentheses(s: str) -> int:
    stack = []
    score = 0

    for char in s:
        if char == '(':
            stack.append(score)
            score = 0
        else:
            score = stack.pop() + max(2 * score, 1)
    
    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "()"
    print(scoreOfParentheses(s1))  # Output: 1

    # Test Case 2
    s2 = "(())"
    print(scoreOfParentheses(s2))  # Output: 2

    # Test Case 3
    s3 = "()()"
    print(scoreOfParentheses(s3))  # Output: 2

    # Test Case 4
    s4 = "(()(()))"
    print(scoreOfParentheses(s4))  # Output: 6

    # Test Case 5
    s5 = "((()))"
    print(scoreOfParentheses(s5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each character in the string `s` exactly once.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The space complexity is O(n) in the worst case, as the stack may store up to `n` elements (one for each opening parenthesis).
- However, the space usage is proportional to the depth of nested parentheses.

Topic: Stack
"""