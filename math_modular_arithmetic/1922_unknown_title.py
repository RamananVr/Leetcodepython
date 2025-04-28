"""
LeetCode Problem #1922: Count Good Numbers

Problem Statement:
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

- For example, "2582" is good because the digits (2 and 8) at even positions are even, and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 10^9 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Constraints:
- 1 <= n <= 10^15
"""

# Python Solution
def countGoodNumbers(n: int) -> int:
    MOD = 10**9 + 7

    # Helper function to perform modular exponentiation
    def modular_exponentiation(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:  # If the exponent is odd
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    # Even indices can have 5 choices (0, 2, 4, 6, 8)
    # Odd indices can have 4 choices (2, 3, 5, 7)
    even_count = (n + 1) // 2  # Number of even indices
    odd_count = n // 2         # Number of odd indices

    # Calculate the total number of good digit strings
    return (modular_exponentiation(5, even_count, MOD) * modular_exponentiation(4, odd_count, MOD)) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(countGoodNumbers(n))  # Expected Output: 5

    # Test Case 2
    n = 4
    print(countGoodNumbers(n))  # Expected Output: 400

    # Test Case 3
    n = 50
    print(countGoodNumbers(n))  # Expected Output: 564908303

    # Test Case 4
    n = 1000000000000000
    print(countGoodNumbers(n))  # Expected Output: (large number modulo 10^9 + 7)

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The modular exponentiation function runs in O(log(exp)) time, where exp is the exponent.
   - In this problem, the exponents are `even_count` and `odd_count`, which are proportional to n.
   - Since modular exponentiation is logarithmic, the time complexity is O(log(n)).

2. Space Complexity:
   - The space complexity is O(1) because we are using a constant amount of extra space.

Topic: Math, Modular Arithmetic
"""