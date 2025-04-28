"""
LeetCode Problem #1175: Prime Arrangements

Problem Statement:
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed).
Since the answer may be large, return the answer modulo 10^9 + 7.

Constraints:
1 <= n <= 100
"""

from math import factorial

def numPrimeArrangements(n: int) -> int:
    """
    Calculate the number of valid permutations of numbers 1 to n such that
    prime numbers are at prime indices.

    Args:
    n (int): The upper limit of the range [1, n].

    Returns:
    int: The number of valid permutations modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    def is_prime(num: int) -> bool:
        """Helper function to check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Count the number of primes in the range [1, n]
    prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
    non_prime_count = n - prime_count

    # The result is the product of factorials of prime_count and non_prime_count
    return (factorial(prime_count) * factorial(non_prime_count)) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    print(f"numPrimeArrangements({n}) = {numPrimeArrangements(n)}")  # Expected: 12

    # Test Case 2
    n = 10
    print(f"numPrimeArrangements({n}) = {numPrimeArrangements(n)}")  # Expected: 17280

    # Test Case 3
    n = 1
    print(f"numPrimeArrangements({n}) = {numPrimeArrangements(n)}")  # Expected: 1

    # Test Case 4
    n = 100
    print(f"numPrimeArrangements({n}) = {numPrimeArrangements(n)}")  # Expected: 682289015


"""
Time Complexity:
- Determining if a number is prime takes O(sqrt(k)) for a number k.
- Checking all numbers from 1 to n for primality takes O(n * sqrt(n)).
- Calculating factorials for prime_count and non_prime_count takes O(p + (n - p)) = O(n), where p is the number of primes.
- Overall time complexity: O(n * sqrt(n)).

Space Complexity:
- The space complexity is O(1) as we are using a constant amount of extra space.

Topic: Math, Combinatorics
"""