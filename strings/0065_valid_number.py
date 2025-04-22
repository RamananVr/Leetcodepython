"""
LeetCode Question #65: Valid Number

Problem Statement:
A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
   a. At least one digit, followed by a dot '.' (e.g., "123.", "0.").
   b. At least one digit, followed by a dot '.', followed by at least one digit (e.g., "123.456", "0.1").
   c. A dot '.', followed by at least one digit (e.g., ".456").

An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. At least one digit (e.g., "123", "-456").

For this problem, we are given a string `s` and need to determine if it is a valid number.

Constraints:
- `s` consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
- `s` is non-empty and has a length of at most 200.

Write a function `isNumber(s: str) -> bool` that returns `True` if `s` is a valid number, otherwise `False`.
"""

import re

def isNumber(s: str) -> bool:
    """
    Determines if the given string is a valid number.
    """
    # Regular expression to match valid numbers
    pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$'
    return bool(re.match(pattern, s))


# Example Test Cases
if __name__ == "__main__":
    test_cases = [
        ("0", True),          # Valid integer
        (" 0.1 ", True),      # Valid decimal number with spaces
        ("abc", False),       # Invalid string
        ("1 a", False),       # Invalid string
        ("2e10", True),       # Valid scientific notation
        (" -90e3   ", True),  # Valid scientific notation with spaces
        (" 1e", False),       # Invalid scientific notation
        ("e3", False),        # Invalid scientific notation
        (" 6e-1", True),      # Valid scientific notation
        ("99e2.5", False),    # Invalid scientific notation
        ("53.5e93", True),    # Valid scientific notation
        (" --6 ", False),     # Invalid number
        ("-+3", False),       # Invalid number
        ("95a54e53", False),  # Invalid number
        (".1", True),         # Valid decimal number
        ("3.", True),         # Valid decimal number
        ("3.e2", True),       # Valid scientific notation
        ("+.8", True),        # Valid decimal number
        ("46.e3", True),      # Valid scientific notation
        ("4e+", False),       # Invalid scientific notation
    ]

    for s, expected in test_cases:
        result = isNumber(s.strip())  # Strip spaces before testing
        print(f"isNumber({repr(s)}) = {result}, Expected = {expected}")
        assert result == expected, f"Test case failed for input: {s}"


"""
Time and Space Complexity Analysis:

Time Complexity:
- The regular expression matching operation `re.match()` runs in O(n) time, where `n` is the length of the input string `s`.
- Therefore, the time complexity of the solution is O(n).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from the regular expression.

Topic: Strings
"""