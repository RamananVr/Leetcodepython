"""
LeetCode Question #29: Divide Two Integers

Problem Statement:
Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than `2^31 − 1`, then return `2^31 − 1`. If the quotient is strictly less than `−2^31`, then return `−2^31`.

Constraints:
- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`
"""

def divide(dividend: int, divisor: int) -> int:
    """
    Divide two integers without using multiplication, division, or mod operator.
    """
    # Handle edge cases for overflow
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Special case: overflow
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)
    
    # Work with absolute values
    dividend, divisor = abs(dividend), abs(divisor)
    
    # Perform division using subtraction and bit manipulation
    quotient = 0
    while dividend >= divisor:
        current_divisor, num_divisors = divisor, 1
        while dividend >= (current_divisor << 1):
            current_divisor <<= 1
            num_divisors <<= 1
        dividend -= current_divisor
        quotient += num_divisors
    
    # Apply the sign
    if negative:
        quotient = -quotient
    
    # Clamp the result to the 32-bit signed integer range
    return max(INT_MIN, min(INT_MAX, quotient))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Positive division
    print(divide(10, 3))  # Expected output: 3
    
    # Test Case 2: Negative division
    print(divide(7, -3))  # Expected output: -2
    
    # Test Case 3: Division resulting in zero
    print(divide(0, 1))  # Expected output: 0
    
    # Test Case 4: Large numbers
    print(divide(-2**31, 1))  # Expected output: -2147483648
    
    # Test Case 5: Overflow case
    print(divide(-2**31, -1))  # Expected output: 2147483647

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a loop to repeatedly subtract the divisor (or its multiples) from the dividend.
- In the worst case, the loop runs O(log(dividend)) times due to the doubling of the divisor in each iteration.
- Therefore, the time complexity is O(log(dividend)).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""