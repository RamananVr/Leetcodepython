"""
LeetCode Problem #1003: Check If Word Is Valid After Substitutions

Problem Statement:
Given a string `s`, determine if it is valid. A string is valid if, starting with an empty string, 
you can transform it into `s` after several steps of adding the string "abc".

Specifically, a string is valid if it can be constructed by repeatedly appending the string "abc" 
to an initially empty string.

Return `true` if the string is valid, otherwise return `false`.

Constraints:
- 1 <= s.length <= 2 * 10^4
- s consists of letters 'a', 'b', and 'c'

Example 1:
Input: s = "aabcbc"
Output: true
Explanation: 
- "" -> "abc" -> "aabcbc"

Example 2:
Input: s = "abcabcababcc"
Output: true
Explanation: 
- "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"

Example 3:
Input: s = "abccba"
Output: false

Example 4:
Input: s = "cababc"
Output: false
"""

def isValid(s: str) -> bool:
    """
    Function to check if the given string is valid after substitutions.
    """
    stack = []
    for char in s:
        stack.append(char)
        # Check if the last three characters in the stack form "abc"
        if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
            # Remove the last three characters
            stack.pop()
            stack.pop()
            stack.pop()
    # If the stack is empty, the string is valid
    return not stack

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aabcbc"
    print(isValid(s1))  # Output: True

    # Test Case 2
    s2 = "abcabcababcc"
    print(isValid(s2))  # Output: True

    # Test Case 3
    s3 = "abccba"
    print(isValid(s3))  # Output: False

    # Test Case 4
    s4 = "cababc"
    print(isValid(s4))  # Output: False

    # Test Case 5
    s5 = "abc"
    print(isValid(s5))  # Output: True

"""
Time Complexity Analysis:
- Let n be the length of the string `s`.
- We iterate through the string once, and for each character, we may perform a constant amount of work 
  (checking the last three characters in the stack and potentially popping them).
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is determined by the stack, which in the worst case can grow to the size of the input string `s`.
- Therefore, the space complexity is O(n).

Topic: Stack
"""