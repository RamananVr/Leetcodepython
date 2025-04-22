"""
LeetCode Question #7: Reverse Integer

Problem Statement:
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside 
the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
- -2^31 <= x <= 2^31 - 1
"""

def reverse(x: int) -> int:
    """
    Reverse the digits of a signed 32-bit integer.

    Args:
    x (int): The integer to reverse.

    Returns:
    int: The reversed integer, or 0 if the result exceeds the 32-bit signed integer range.
    """
    # Define the 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Determine the sign of the number
    sign = -1 if x < 0 else 1
    
    # Reverse the absolute value of the number
    reversed_x = int(str(abs(x))[::-1])
    
    # Apply the sign and check for overflow
    result = sign * reversed_x
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

# Example test cases
if __name__ == "__main__":
    # Test case 1: Positive number
    print(reverse(123))  # Output: 321
    
    # Test case 2: Negative number
    print(reverse(-123))  # Output: -321
    
    # Test case 3: Number with trailing zero
    print(reverse(120))  # Output: 21
    
    # Test case 4: Zero
    print(reverse(0))  # Output: 0
    
    # Test case 5: Overflow case
    print(reverse(1534236469))  # Output: 0

# Topic: Math