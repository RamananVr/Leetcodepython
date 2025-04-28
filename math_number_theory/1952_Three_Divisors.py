"""
LeetCode Problem #1952: Three Divisors

Problem Statement:
Given an integer `n`, return `true` if `n` has exactly three positive divisors. Otherwise, return `false`.

An integer `m` has exactly three positive divisors if and only if it is a square of a prime number. For example:
- 4 has exactly three divisors: 1, 2, and 4.
- 9 has exactly three divisors: 1, 3, and 9.
- 16 does not have exactly three divisors because it has five divisors: 1, 2, 4, 8, and 16.

Constraints:
- 1 <= n <= 10^4
"""

def isThree(n: int) -> bool:
    """
    Determines if the given integer `n` has exactly three positive divisors.

    Args:
    n (int): The input integer.

    Returns:
    bool: True if `n` has exactly three positive divisors, False otherwise.
    """
    # A number has exactly three divisors if and only if it is the square of a prime number.
    # Step 1: Check if `n` is a perfect square.
    root = int(n**0.5)
    if root * root != n:
        return False
    
    # Step 2: Check if the square root of `n` is a prime number.
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    return is_prime(root)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 4 (4 = 2^2, and 2 is prime)
    print(isThree(4))  # Expected output: True

    # Test Case 2: n = 9 (9 = 3^2, and 3 is prime)
    print(isThree(9))  # Expected output: True

    # Test Case 3: n = 16 (16 = 4^2, but 4 is not prime)
    print(isThree(16))  # Expected output: False

    # Test Case 4: n = 25 (25 = 5^2, and 5 is prime)
    print(isThree(25))  # Expected output: True

    # Test Case 5: n = 1 (1 is not a square of a prime number)
    print(isThree(1))  # Expected output: False

    # Test Case 6: n = 10 (10 is not a perfect square)
    print(isThree(10))  # Expected output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Checking if `n` is a perfect square: O(1).
- Checking if the square root of `n` is prime:
  - The prime-checking function iterates up to the square root of the square root of `n`.
  - In the worst case, this is O(sqrt(sqrt(n))).
- Overall time complexity: O(sqrt(sqrt(n))).

Space Complexity:
- The algorithm uses a constant amount of space, so the space complexity is O(1).

Topic: Math, Number Theory
"""