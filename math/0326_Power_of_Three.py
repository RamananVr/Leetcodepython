"""
LeetCode Problem #326: Power of Three

Problem Statement:
Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.

An integer `n` is a power of three if there exists an integer `x` such that `n == 3^x`.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = -1 since 3^x is always positive.

Constraints:
- -2^31 <= n <= 2^31 - 1

Follow-up:
Could you solve it without using loops or recursion?
"""

def isPowerOfThree(n: int) -> bool:
    """
    Determines if the given integer n is a power of three.

    Args:
    n (int): The input integer.

    Returns:
    bool: True if n is a power of three, False otherwise.
    """
    # The largest power of 3 within the range of a 32-bit signed integer is 3^19 = 1162261467.
    # If n is a power of three, it must divide 1162261467 without a remainder.
    return n > 0 and 1162261467 % n == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 27 (3^3)
    print(isPowerOfThree(27))  # Expected output: True

    # Test Case 2: n = 0 (not a power of three)
    print(isPowerOfThree(0))  # Expected output: False

    # Test Case 3: n = -1 (not a power of three)
    print(isPowerOfThree(-1))  # Expected output: False

    # Test Case 4: n = 9 (3^2)
    print(isPowerOfThree(9))  # Expected output: True

    # Test Case 5: n = 45 (not a power of three)
    print(isPowerOfThree(45))  # Expected output: False

"""
Time Complexity Analysis:
- The solution uses a single modulo operation, which is O(1).
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution does not use any additional data structures or memory.
- Therefore, the space complexity is O(1).

Topic: Math
"""