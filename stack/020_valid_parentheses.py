"""
LeetCode Question #20: Valid Parentheses

Problem Statement:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    """
    Function to determine if a string of parentheses is valid.
    """
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to map closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the top element from the stack if it's not empty, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched correctly
    return not stack

# Example test cases
if __name__ == "__main__":
    # Test case 1: Valid parentheses
    print(isValid("()"))  # Output: True
    
    # Test case 2: Multiple valid parentheses
    print(isValid("()[]{}"))  # Output: True
    
    # Test case 3: Mismatched parentheses
    print(isValid("(]"))  # Output: False
    
    # Test case 4: Incorrect order of parentheses
    print(isValid("([)]"))  # Output: False
    
    # Test case 5: Nested valid parentheses
    print(isValid("{[]}"))  # Output: True

# Topic: Stack