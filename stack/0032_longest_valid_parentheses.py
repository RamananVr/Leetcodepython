"""
LeetCode Question #32: Longest Valid Parentheses

Problem Statement:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is either '(' or ')'.
"""

def longestValidParentheses(s: str) -> int:
    """
    This function finds the length of the longest valid parentheses substring.
    """
    stack = [-1]  # Initialize stack with a base index
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push the index of '(' onto the stack
        else:
            stack.pop()  # Pop the last index
            if not stack:
                stack.append(i)  # Push the current index as a base
            else:
                max_length = max(max_length, i - stack[-1])  # Calculate the length of valid substring

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(()"
    print(f"Input: {s1} -> Output: {longestValidParentheses(s1)}")  # Expected Output: 2

    # Test Case 2
    s2 = ")()())"
    print(f"Input: {s2} -> Output: {longestValidParentheses(s2)}")  # Expected Output: 4

    # Test Case 3
    s3 = ""
    print(f"Input: {s3} -> Output: {longestValidParentheses(s3)}")  # Expected Output: 0

    # Test Case 4
    s4 = "()(())"
    print(f"Input: {s4} -> Output: {longestValidParentheses(s4)}")  # Expected Output: 6

    # Test Case 5
    s5 = "())"
    print(f"Input: {s5} -> Output: {longestValidParentheses(s5)}")  # Expected Output: 2

"""
Time Complexity Analysis:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The space complexity is O(n) in the worst case, as the stack may store up to n indices.

Topic: Stack
"""