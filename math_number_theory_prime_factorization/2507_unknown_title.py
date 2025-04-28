"""
LeetCode Problem #2507: Smallest Value After Replacing With Sum of Prime Factors

Problem Statement:
You are given a positive integer `n`.

Continuously replace `n` with the sum of its prime factors until `n` becomes a prime number.

Return the smallest value of `n` after the replacement.

Note:
- The prime factors of a number are the prime numbers that divide it exactly. For example, the prime factors of 12 are 2, 2, and 3.
- A number is prime if it has exactly two distinct positive divisors: 1 and itself.

Constraints:
- 2 <= n <= 10^5
"""

from math import isqrt

def smallestValue(n: int) -> int:
    def is_prime(x: int) -> bool:
        """Check if a number is prime."""
        if x < 2:
            return False
        for i in range(2, isqrt(x) + 1):
            if x % i == 0:
                return False
        return True

    def prime_factors_sum(x: int) -> int:
        """Calculate the sum of prime factors of a number."""
        total = 0
        factor = 2
        while factor * factor <= x:
            while x % factor == 0:
                total += factor
                x //= factor
            factor += 1
        if x > 1:  # If there's a remaining prime factor
            total += x
        return total

    while not is_prime(n):
        new_n = prime_factors_sum(n)
        if new_n == n:  # If the sum of prime factors doesn't change, break
            break
        n = new_n

    return n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    print(f"Smallest value for n={n1}: {smallestValue(n1)}")  # Expected: 7

    # Test Case 2
    n2 = 15
    print(f"Smallest value for n={n2}: {smallestValue(n2)}")  # Expected: 5

    # Test Case 3
    n3 = 4
    print(f"Smallest value for n={n3}: {smallestValue(n3)}")  # Expected: 3

    # Test Case 4
    n4 = 30
    print(f"Smallest value for n={n4}: {smallestValue(n4)}")  # Expected: 5

    # Test Case 5
    n5 = 7
    print(f"Smallest value for n={n5}: {smallestValue(n5)}")  # Expected: 7

"""
Time Complexity:
- The `is_prime` function runs in O(sqrt(n)) time.
- The `prime_factors_sum` function iterates over all potential factors up to sqrt(n), so it also runs in O(sqrt(n)).
- In the worst case, the loop in `smallestValue` runs for O(log(n)) iterations, as the value of `n` decreases significantly with each step.
- Overall time complexity: O(log(n) * sqrt(n)).

Space Complexity:
- The space complexity is O(1) since we use a constant amount of extra space.

Topic: Math, Number Theory, Prime Factorization
"""