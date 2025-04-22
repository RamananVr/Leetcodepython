"""
LeetCode Problem #231: Power of Two

Problem Statement:
Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x` such that `n == 2^x`.

Constraints:
- -2^31 <= n <= 2^31 - 1

Follow-up:
Could you solve it without loops/recursion?
"""

def isPowerOfTwo(n: int) -> bool:
    """
    Determines if the given integer n is a power of two.

    Args:
    n (int): The input integer.

    Returns:
    bool: True if n is a power of two, False otherwise.
    """
    # A number is a power of two if it is greater than 0 and has only one bit set in its binary representation.
    return n > 0 and (n & (n - 1)) == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n is a power of two
    n1 = 1
    print(isPowerOfTwo(n1))  # Expected output: True (2^0 = 1)

    # Test Case 2: n is a power of two
    n2 = 16
    print(isPowerOfTwo(n2))  # Expected output: True (2^4 = 16)

    # Test Case 3: n is not a power of two
    n3 = 3
    print(isPowerOfTwo(n3))  # Expected output: False

    # Test Case 4: n is zero
    n4 = 0
    print(isPowerOfTwo(n4))  # Expected output: False

    # Test Case 5: n is negative
    n5 = -8
    print(isPowerOfTwo(n5))  # Expected output: False

    # Test Case 6: n is a large power of two
    n6 = 2**30
    print(isPowerOfTwo(n6))  # Expected output: True

"""
Time Complexity Analysis:
- The solution uses a single bitwise operation, which takes O(1) time.
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution does not use any additional data structures or memory.
- Therefore, the space complexity is O(1).

Topic: Bit Manipulation
"""