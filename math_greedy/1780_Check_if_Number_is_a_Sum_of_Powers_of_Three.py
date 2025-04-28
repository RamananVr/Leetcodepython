"""
LeetCode Problem #1780: Check if Number is a Sum of Powers of Three

Problem Statement:
Given an integer `n`, return `true` if it is possible to represent `n` as the sum of distinct powers of three. Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3^x`.

Constraints:
- 1 <= n <= 10^7
"""

def checkPowersOfThree(n: int) -> bool:
    """
    Determines if a number can be represented as the sum of distinct powers of three.

    Args:
    n (int): The input number.

    Returns:
    bool: True if the number can be represented as the sum of distinct powers of three, False otherwise.
    """
    while n > 0:
        if n % 3 == 2:  # If the remainder is 2, it's not possible to represent n as a sum of powers of three
            return False
        n //= 3  # Reduce n by dividing it by 3
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 12
    # Explanation: 12 = 3^1 + 3^2
    print(checkPowersOfThree(12))  # Expected output: True

    # Test Case 2: n = 91
    # Explanation: 91 = 3^0 + 3^2 + 3^4
    print(checkPowersOfThree(91))  # Expected output: True

    # Test Case 3: n = 21
    # Explanation: 21 cannot be represented as the sum of distinct powers of three
    print(checkPowersOfThree(21))  # Expected output: False

    # Test Case 4: n = 1
    # Explanation: 1 = 3^0
    print(checkPowersOfThree(1))  # Expected output: True

    # Test Case 5: n = 27
    # Explanation: 27 = 3^3
    print(checkPowersOfThree(27))  # Expected output: True

"""
Time Complexity Analysis:
- The algorithm repeatedly divides `n` by 3 until `n` becomes 0. The number of iterations is proportional to the number of digits in the base-3 representation of `n`.
- The number of digits in base-3 is approximately log3(n), which is O(log(n)).

Space Complexity Analysis:
- The algorithm uses a constant amount of space, as no additional data structures are used.
- Space complexity is O(1).

Topic: Math, Greedy
"""