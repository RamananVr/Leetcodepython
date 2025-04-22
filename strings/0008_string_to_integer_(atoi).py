"""
LeetCode Question #8: String to Integer (atoi)

Problem Statement:
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to the C/C++ `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive. Assume the result is positive if neither is present.
3. Read in the next characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e., "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. Return the integer as the final result.

Note:
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Constraints:
- `0 <= s.length <= 200`
- `s` consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and other symbols.

"""

def myAtoi(s: str) -> int:
    # Step 1: Remove leading whitespace
    s = s.lstrip()
    if not s:
        return 0

    # Step 2: Check for sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Step 3: Read digits
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # Step 4: Apply sign
    result *= sign

    # Step 5: Clamp to 32-bit signed integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic positive number
    print(myAtoi("42"))  # Output: 42

    # Test Case 2: Leading whitespace
    print(myAtoi("   -42"))  # Output: -42

    # Test Case 3: Number with trailing characters
    print(myAtoi("4193 with words"))  # Output: 4193

    # Test Case 4: Non-digit leading characters
    print(myAtoi("words and 987"))  # Output: 0

    # Test Case 5: Overflow positive
    print(myAtoi("2147483648"))  # Output: 2147483647

    # Test Case 6: Overflow negative
    print(myAtoi("-91283472332"))  # Output: -2147483648

    # Test Case 7: Empty string
    print(myAtoi(""))  # Output: 0

    # Test Case 8: Only sign
    print(myAtoi("+"))  # Output: 0

    # Test Case 9: Leading zeros
    print(myAtoi("000123"))  # Output: 123

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes the string `s` character by character. In the worst case, it iterates through all characters of the string.
- Let `n` be the length of the string. The time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `sign`, `result`, and constants `INT_MIN` and `INT_MAX`.
- The space complexity is O(1).

Topic: Strings
"""