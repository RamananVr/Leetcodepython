"""
LeetCode Question #371: Sum of Two Integers

Problem Statement:
Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

Constraints:
- -2^31 <= a, b <= 2^31 - 1
- The result will always fit in a 32-bit integer.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
"""

def getSum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers without using the '+' or '-' operators.
    """
    # Define constants for 32-bit integer limits
    MAX_INT = 0x7FFFFFFF  # 2^31 - 1
    MIN_INT = 0x80000000  # -2^31
    MASK = 0xFFFFFFFF     # Mask to get last 32 bits

    while b != 0:
        # Calculate carry
        carry = (a & b) & MASK
        # XOR for addition without carry
        a = (a ^ b) & MASK
        # Shift carry left by 1
        b = (carry << 1) & MASK

    # If a is greater than MAX_INT, it means it's a negative number in 32-bit signed integer
    return a if a <= MAX_INT else ~(a ^ MASK)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b = 1, 2
    print(f"getSum({a}, {b}) = {getSum(a, b)}")  # Output: 3

    # Test Case 2
    a, b = 2, 3
    print(f"getSum({a}, {b}) = {getSum(a, b)}")  # Output: 5

    # Test Case 3
    a, b = -1, 1
    print(f"getSum({a}, {b}) = {getSum(a, b)}")  # Output: 0

    # Test Case 4
    a, b = -2, -3
    print(f"getSum({a}, {b}) = {getSum(a, b)}")  # Output: -5

    # Test Case 5
    a, b = 15, 25
    print(f"getSum({a}, {b}) = {getSum(a, b)}")  # Output: 40

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until there is no carry left. In the worst case, the carry propagates through all 32 bits.
- Therefore, the time complexity is O(1), as the number of iterations is bounded by the fixed size of integers (32 bits).

Space Complexity:
- The algorithm uses a constant amount of space for variables like `carry`, `a`, and `b`.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""