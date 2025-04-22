"""
LeetCode Question #301: Remove Invalid Parentheses

Problem Statement:
Given a string `s` that contains parentheses and letters, you need to remove the minimum number of invalid parentheses to make the input string valid. Return all possible results. You may return the answer in any order.

A valid string is defined as:
1. An empty string is valid.
2. A string containing only lowercase letters is valid.
3. A string can be valid if it contains balanced parentheses, i.e., every opening parenthesis '(' has a corresponding closing parenthesis ')'.

Example 1:
Input: s = "()())()"
Output: ["(())()", "()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()", "(a)()()"]

Example 3:
Input: s = ")("
Output: [""]

Constraints:
- `1 <= s.length <= 50`
- `s` consists of lowercase English letters and parentheses '(' and ')'.
"""

from collections import deque

def removeInvalidParentheses(s):
    """
    Removes the minimum number of invalid parentheses to make the input string valid.
    Returns all possible valid strings.
    """
    def is_valid(string):
        """Helper function to check if a string has valid parentheses."""
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    # BFS initialization
    queue = deque([s])
    visited = set([s])
    valid_strings = []
    found = False

    while queue:
        current = queue.popleft()

        # If the current string is valid, add it to the result list
        if is_valid(current):
            valid_strings.append(current)
            found = True

        # If a valid string has been found, skip further exploration
        if found:
            continue

        # Generate all possible strings by removing one parenthesis
        for i in range(len(current)):
            if current[i] not in "()":
                continue
            next_string = current[:i] + current[i+1:]
            if next_string not in visited:
                visited.add(next_string)
                queue.append(next_string)

    return valid_strings


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "()())()"
    print(removeInvalidParentheses(s1))  # Output: ["(())()", "()()()"]

    # Test Case 2
    s2 = "(a)())()"
    print(removeInvalidParentheses(s2))  # Output: ["(a())()", "(a)()()"]

    # Test Case 3
    s3 = ")("
    print(removeInvalidParentheses(s3))  # Output: [""]

    # Test Case 4
    s4 = "n"
    print(removeInvalidParentheses(s4))  # Output: ["n"]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - In the worst case, we generate all possible substrings of `s` by removing parentheses.
   - For a string of length `n`, there are at most `2^n` substrings.
   - For each substring, we check its validity, which takes O(n) time.
   - Therefore, the worst-case time complexity is O(n * 2^n).

2. Space Complexity:
   - The space complexity is dominated by the BFS queue and the visited set.
   - The queue and visited set can store up to `2^n` substrings in the worst case.
   - Each substring has a length of at most `n`.
   - Therefore, the space complexity is O(n * 2^n).

Topic: Breadth-First Search (BFS)
"""