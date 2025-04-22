"""
LeetCode Problem #50: Pow(x, n)

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4
"""

def myPow(x: float, n: int) -> float:
    """
    Calculate x raised to the power n (x^n) using an efficient approach.
    """
    if n == 0:
        return 1  # Base case: x^0 = 1
    if n < 0:
        x = 1 / x  # Handle negative powers by taking reciprocal
        n = -n

    result = 1
    current_product = x

    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply the result by the current product
            result *= current_product
        current_product *= current_product  # Square the current product
        n //= 2  # Divide n by 2 (integer division)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1, n1 = 2.00000, 10
    print(f"myPow({x1}, {n1}) = {myPow(x1, n1)}")  # Expected: 1024.00000

    # Test Case 2
    x2, n2 = 2.10000, 3
    print(f"myPow({x2}, {n2}) = {myPow(x2, n2)}")  # Expected: 9.26100

    # Test Case 3
    x3, n3 = 2.00000, -2
    print(f"myPow({x3}, {n3}) = {myPow(x3, n3)}")  # Expected: 0.25000

    # Test Case 4
    x4, n4 = 0.00001, 2147483647
    print(f"myPow({x4}, {n4}) = {myPow(x4, n4)}")  # Expected: 0.0 (very small number)

    # Test Case 5
    x5, n5 = 1.00000, -2147483648
    print(f"myPow({x5}, {n5}) = {myPow(x5, n5)}")  # Expected: 1.0

# Topic: Math