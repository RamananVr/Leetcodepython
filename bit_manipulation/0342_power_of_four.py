"""
LeetCode Question #342: Power of Four

Problem Statement:
Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

An integer `n` is a power of four if there exists an integer `x` such that `n == 4^x`.

Example 1:
Input: n = 16
Output: true
Explanation: 16 = 4^2.

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
Explanation: 1 = 4^0.

Constraints:
- -2^31 <= n <= 2^31 - 1

Follow up:
Could you solve it without using loops/recursion?
"""

def isPowerOfFour(n: int) -> bool:
    """
    Determines if the given integer n is a power of four.

    Args:
    n (int): The input integer.

    Returns:
    bool: True if n is a power of four, False otherwise.
    """
    # A number is a power of four if:
    # 1. It is greater than 0.
    # 2. It is a power of two (only one bit is set in its binary representation).
    # 3. The single set bit is in an odd position (1-based index).
    return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 16 (4^2)
    print(isPowerOfFour(16))  # Expected output: True

    # Test Case 2: n = 5 (not a power of 4)
    print(isPowerOfFour(5))  # Expected output: False

    # Test Case 3: n = 1 (4^0)
    print(isPowerOfFour(1))  # Expected output: True

    # Test Case 4: n = 64 (4^3)
    print(isPowerOfFour(64))  # Expected output: True

    # Test Case 5: n = 0 (not a power of 4)
    print(isPowerOfFour(0))  # Expected output: False

    # Test Case 6: n = -4 (negative numbers cannot be powers of 4)
    print(isPowerOfFour(-4))  # Expected output: False

"""
Time Complexity:
- The solution performs a constant number of bitwise operations, so the time complexity is O(1).

Space Complexity:
- The solution does not use any additional data structures, so the space complexity is O(1).

Topic: Bit Manipulation
"""