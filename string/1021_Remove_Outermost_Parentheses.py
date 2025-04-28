"""
LeetCode Problem #1021: Remove Outermost Parentheses

Problem Statement:
A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is non-empty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` non-empty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings.

Return `s` after removing the outermost parentheses of every primitive string in the primitive decomposition of `s`.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:
- 1 <= s.length <= 10^5
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.
"""

def removeOuterParentheses(s: str) -> str:
    """
    Removes the outermost parentheses of every primitive string in the input string.

    Args:
    s (str): A valid parentheses string.

    Returns:
    str: The modified string with outermost parentheses removed.
    """
    result = []
    balance = 0  # Tracks the depth of the parentheses

    for char in s:
        if char == '(':
            if balance > 0:  # Only add '(' if it's not an outermost one
                result.append(char)
            balance += 1
        elif char == ')':
            balance -= 1
            if balance > 0:  # Only add ')' if it's not an outermost one
                result.append(char)

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(()())(())"
    print(removeOuterParentheses(s1))  # Expected Output: "()()()"

    # Test Case 2
    s2 = "(()())(())(()(()))"
    print(removeOuterParentheses(s2))  # Expected Output: "()()()()(())"

    # Test Case 3
    s3 = "()()"
    print(removeOuterParentheses(s3))  # Expected Output: ""

    # Test Case 4
    s4 = "((()))"
    print(removeOuterParentheses(s4))  # Expected Output: "(())"

    # Test Case 5
    s5 = "(()(()))"
    print(removeOuterParentheses(s5))  # Expected Output: "()(()))"

"""
Time Complexity Analysis:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity Analysis:
- The algorithm uses a list `result` to store the modified string, which in the worst case can be of size `n`.
- Therefore, the space complexity is O(n).

Topic: String
"""