"""
LeetCode Problem #29: Divide Two Integers

Problem Statement:
Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return the quotient after dividing `dividend` by `divisor`.

Note:
- Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than `2^31 − 1`, return `2^31 − 1`. If the quotient is strictly less than `−2^31`, return `−2^31`.

Constraints:
- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`
"""

def divide(dividend: int, divisor: int) -> int:
    # Handle edge cases for overflow
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # If dividend is INT_MIN and divisor is -1, the result overflows
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)

    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)

    # Perform the division using subtraction
    quotient = 0
    while dividend >= divisor:
        temp_divisor, num_divisors = divisor, 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            num_divisors <<= 1
        dividend -= temp_divisor
        quotient += num_divisors

    # Apply the sign
    if negative:
        quotient = -quotient

    # Clamp the result to the 32-bit signed integer range
    return max(INT_MIN, min(INT_MAX, quotient))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dividend = 10
    divisor = 3
    print(divide(dividend, divisor))  # Output: 3

    # Test Case 2
    dividend = 7
    divisor = -3
    print(divide(dividend, divisor))  # Output: -2

    # Test Case 3
    dividend = 0
    divisor = 1
    print(divide(dividend, divisor))  # Output: 0

    # Test Case 4
    dividend = -2147483648
    divisor = -1
    print(divide(dividend, divisor))  # Output: 2147483647 (clamped to INT_MAX)

    # Test Case 5
    dividend = -2147483648
    divisor = 2
    print(divide(dividend, divisor))  # Output: -1073741824

"""
Topic: Math, Bit Manipulation
"""