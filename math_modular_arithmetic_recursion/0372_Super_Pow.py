"""
LeetCode Problem #372: Super Pow

Problem Statement:
Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:
Input: a = 2, b = [3]
Output: 8

Example 2:
Input: a = 2, b = [1, 0]
Output: 1024

Example 3:
Input: a = 1, b = [4, 3, 3, 8, 5, 2]
Output: 1

Constraints:
- 1 <= a <= 2^31 - 1
- 1 <= b.length <= 2000
- 0 <= b[i] <= 9
- b does not contain leading zeros.
"""

def superPow(a: int, b: list[int]) -> int:
    """
    Calculate a^b mod 1337 where b is represented as a list of digits.
    """
    MOD = 1337

    def mod_exp(x: int, y: int) -> int:
        """
        Helper function to calculate (x^y) % MOD using modular exponentiation.
        """
        result = 1
        x %= MOD
        while y > 0:
            if y % 2 == 1:
                result = (result * x) % MOD
            x = (x * x) % MOD
            y //= 2
        return result

    def super_pow_recursive(a: int, b: list[int]) -> int:
        """
        Recursive function to calculate super power.
        """
        if not b:
            return 1
        last_digit = b.pop()
        part1 = mod_exp(a, last_digit)
        part2 = mod_exp(super_pow_recursive(a, b), 10)
        return (part1 * part2) % MOD

    return super_pow_recursive(a, b)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = 2
    b = [3]
    print(superPow(a, b))  # Output: 8

    # Test Case 2
    a = 2
    b = [1, 0]
    print(superPow(a, b))  # Output: 1024

    # Test Case 3
    a = 1
    b = [4, 3, 3, 8, 5, 2]
    print(superPow(a, b))  # Output: 1

    # Test Case 4
    a = 2147483647
    b = [2, 0, 0]
    print(superPow(a, b))  # Output: 1198

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `mod_exp` function runs in O(log(y)) time due to modular exponentiation.
- The recursive function `super_pow_recursive` is called for each digit in `b`, and for each call, it performs modular exponentiation.
- If `b` has length n, the total time complexity is O(n * log(10)) = O(n).

Space Complexity:
- The recursion depth is equal to the length of `b`, so the space complexity is O(n) due to the call stack.

Topic: Math, Modular Arithmetic, Recursion
"""