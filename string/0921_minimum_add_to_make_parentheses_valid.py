"""
LeetCode Question #921: Minimum Add to Make Parentheses Valid

Problem Statement:
Given a string `s` of '(' and ')' parentheses, return the minimum number of parentheses you must add to make the string valid.

A string is valid if:
1. Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
2. Every closing parenthesis ')' has a corresponding opening parenthesis '('.
3. Parentheses are properly nested.

Example:
- Input: s = "())"
- Output: 1

- Input: s = "((("
- Output: 3

- Input: s = "()"
- Output: 0

- Input: s = "()))(("
- Output: 4

Constraints:
- 1 <= s.length <= 1000
- s consists of '(' and ')' characters only.
"""

def minAddToMakeValid(s: str) -> int:
    """
    Calculate the minimum number of parentheses to add to make the string valid.

    :param s: A string consisting of '(' and ')' characters.
    :return: Minimum number of parentheses to add to make the string valid.
    """
    # Initialize counters for unmatched opening and closing parentheses
    open_count = 0
    close_count = 0

    # Iterate through the string
    for char in s:
        if char == '(':
            # Increment open_count for an opening parenthesis
            open_count += 1
        elif char == ')':
            # If there's an unmatched opening parenthesis, match it
            if open_count > 0:
                open_count -= 1
            else:
                # Otherwise, increment close_count for an unmatched closing parenthesis
                close_count += 1

    # The total number of additions needed is the sum of unmatched opening and closing parentheses
    return open_count + close_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "())"
    print(minAddToMakeValid(s1))  # Output: 1

    # Test Case 2
    s2 = "((("
    print(minAddToMakeValid(s2))  # Output: 3

    # Test Case 3
    s3 = "()"
    print(minAddToMakeValid(s3))  # Output: 0

    # Test Case 4
    s4 = "()))(("
    print(minAddToMakeValid(s4))  # Output: 4

    # Test Case 5
    s5 = ""
    print(minAddToMakeValid(s5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space (two integer counters: `open_count` and `close_count`).
- Therefore, the space complexity is O(1).

Topic: String
"""