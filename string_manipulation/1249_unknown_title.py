"""
LeetCode Problem #1249: Minimum Remove to Make Valid Parentheses

Problem Statement:
Given a string `s` of `'('`, `')'`, and lowercase English characters, your task is to remove the minimum number of parentheses 
('(' or ')') in any positions so that the resulting string is valid. A string is valid if:
1. Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
2. Every closing parenthesis ')' has a corresponding opening parenthesis '('.
3. Parentheses are properly nested.

Return the resulting string. Note that the input string may contain lowercase English letters in addition to parentheses.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either `'('`, `')'`, or a lowercase English letter.
"""

# Solution
def minRemoveToMakeValid(s: str) -> str:
    # First pass: Identify invalid parentheses
    stack = []
    to_remove = set()
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    # Add remaining unmatched '(' indices to the removal set
    to_remove.update(stack)
    
    # Second pass: Build the result string
    result = []
    for i, char in enumerate(s):
        if i not in to_remove:
            result.append(char)
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "lee(t(c)o)de)"
    print(minRemoveToMakeValid(s1))  # Output: "lee(t(c)o)de"

    # Test Case 2
    s2 = "a)b(c)d"
    print(minRemoveToMakeValid(s2))  # Output: "ab(c)d"

    # Test Case 3
    s3 = "))(("
    print(minRemoveToMakeValid(s3))  # Output: ""

    # Test Case 4
    s4 = "(a(b(c)d)"
    print(minRemoveToMakeValid(s4))  # Output: "a(b(c)d)"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The first pass iterates through the string `s` to identify invalid parentheses, which takes O(n) time.
- The second pass iterates through the string again to construct the result, which also takes O(n) time.
- Overall, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The `stack` and `to_remove` data structures store indices of parentheses, which in the worst case can be O(n) if all characters are parentheses.
- The `result` list also takes O(n) space to store the final valid string.
- Overall, the space complexity is O(n).
"""

# Topic: String Manipulation