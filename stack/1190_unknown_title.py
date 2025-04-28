"""
LeetCode Problem #1190: Reverse Substrings Between Each Pair of Parentheses

Problem Statement:
You are given a string `s` that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any parentheses.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters and parentheses.
- It is guaranteed that all parentheses are balanced.
"""

# Solution
def reverseParentheses(s: str) -> str:
    stack = []
    for char in s:
        if char == ')':
            # Pop characters until the matching '(' is found
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            # Pop the '('
            stack.pop()
            # Push the reversed substring back onto the stack
            stack.extend(temp)
        else:
            stack.append(char)
    # Join the stack to form the final result
    return ''.join(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(abcd)"
    print(reverseParentheses(s1))  # Output: "dcba"

    # Test Case 2
    s2 = "(u(love)i)"
    print(reverseParentheses(s2))  # Output: "iloveu"

    # Test Case 3
    s3 = "(ed(et(oc))el)"
    print(reverseParentheses(s3))  # Output: "leetcode"

    # Test Case 4
    s4 = "a(bcdefghijkl(mno)p)q"
    print(reverseParentheses(s4))  # Output: "apmnolkjihgfedcbq"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each character in the string is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(n) because we use a stack to store characters, and in the worst case, the stack can hold all characters of the string.
"""

# Topic: Stack