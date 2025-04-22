"""
LeetCode Question #7: Reverse Integer

Problem Statement:
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside 
the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
- `-2^31 <= x <= 2^31 - 1`

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
"""

def reverse(x: int) -> int:
    """
    Reverses the digits of a 32-bit signed integer. Returns 0 if the reversed integer overflows.
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1  # Define 32-bit integer range
    result = 0
    sign = -1 if x < 0 else 1  # Determine the sign of the number
    x = abs(x)  # Work with the absolute value of x

    while x != 0:
        digit = x % 10  # Extract the last digit
        x //= 10  # Remove the last digit from x

        # Check for overflow before updating the result
        if result > (INT_MAX - digit) // 10:
            return 0  # Return 0 if the reversed number overflows

        result = result * 10 + digit  # Append the digit to the reversed number

    return sign * result  # Restore the sign and return the result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1 = 123
    print(f"Input: {x1}, Output: {reverse(x1)}")  # Expected Output: 321

    # Test Case 2
    x2 = -123
    print(f"Input: {x2}, Output: {reverse(x2)}")  # Expected Output: -321

    # Test Case 3
    x3 = 120
    print(f"Input: {x3}, Output: {reverse(x3)}")  # Expected Output: 21

    # Test Case 4
    x4 = 0
    print(f"Input: {x4}, Output: {reverse(x4)}")  # Expected Output: 0

    # Test Case 5 (Overflow Case)
    x5 = 1534236469
    print(f"Input: {x5}, Output: {reverse(x5)}")  # Expected Output: 0


"""
Time Complexity Analysis:
- The time complexity of the solution is O(log10(x)), where x is the input integer. This is because we process each digit of x once, and the number of digits in x is proportional to log10(x).

Space Complexity Analysis:
- The space complexity is O(1) because we use a constant amount of extra space regardless of the input size.

Topic: Math
"""