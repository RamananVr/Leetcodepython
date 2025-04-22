"""
LeetCode Question #8: String to Integer (atoi)

Problem Statement:
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to the C/C++ `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final number is negative or positive. Assume the result is positive if neither is present.
3. Read in the next characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e., "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. Return the integer as the final result.

Note:
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which makes the number negative. The rest of the string is "42".

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation: Conversion stops at the first non-digit character.

Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and other symbols.
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

# Example test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "42"
    print(myAtoi(s1))  # Output: 42

    # Test case 2
    s2 = "   -42"
    print(myAtoi(s2))  # Output: -42

    # Test case 3
    s3 = "4193 with words"
    print(myAtoi(s3))  # Output: 4193

    # Test case 4
    s4 = "words and 987"
    print(myAtoi(s4))  # Output: 0

    # Test case 5
    s5 = "-91283472332"
    print(myAtoi(s5))  # Output: -2147483648

    # Test case 6
    s6 = "+1"
    print(myAtoi(s6))  # Output: 1

    # Test case 7
    s7 = "00000-42a1234"
    print(myAtoi(s7))  # Output: 0

# Topic: Strings