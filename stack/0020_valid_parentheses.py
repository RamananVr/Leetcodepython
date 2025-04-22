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
    # Mapping of closing to opening brackets
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

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "()"
    print(isValid(s1))  # Output: True

    # Test Case 2
    s2 = "()[]{}"
    print(isValid(s2))  # Output: True

    # Test Case 3
    s3 = "(]"
    print(isValid(s3))  # Output: False

    # Test Case 4
    s4 = "([)]"
    print(isValid(s4))  # Output: False

    # Test Case 5
    s5 = "{[]}"
    print(isValid(s5))  # Output: True

"""
Time Complexity Analysis:
- The algorithm processes each character in the string exactly once.
- Each push and pop operation on the stack takes O(1) time.
- Therefore, the overall time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- In the worst case, the stack can contain all the opening brackets in the string.
- This happens when the string consists only of opening brackets.
- Therefore, the space complexity is O(n), where n is the length of the string.

Topic: Stack
"""