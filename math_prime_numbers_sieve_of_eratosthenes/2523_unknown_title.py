"""
LeetCode Problem #2523: Closest Prime Numbers in Range

Problem Statement:
Given two integers `left` and `right`, find the two closest prime numbers in the inclusive range `[left, right]`. 
If there are multiple pairs of closest prime numbers, return the pair with the smallest first number. 
If there are no prime numbers in the range, return `[-1, -1]`.

A prime number is a number greater than 1 that has no divisors other than 1 and itself.

Example:
Input: left = 10, right = 19
Output: [11, 13]

Constraints:
- 1 <= left <= right <= 10^6
"""

# Solution
from math import isqrt

def closest_primes(left: int, right: int) -> list[int]:
    def sieve_of_eratosthenes(n: int) -> list[bool]:
        """Generate a list of booleans where True indicates the number is prime."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, isqrt(n) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Generate primes up to `right` using the sieve of Eratosthenes
    is_prime = sieve_of_eratosthenes(right)

    # Collect all primes in the range [left, right]
    primes_in_range = [i for i in range(left, right + 1) if is_prime[i]]

    # If there are fewer than 2 primes, return [-1, -1]
    if len(primes_in_range) < 2:
        return [-1, -1]

    # Find the closest pair of primes
    closest_pair = [-1, -1]
    min_diff = float('inf')
    for i in range(1, len(primes_in_range)):
        diff = primes_in_range[i] - primes_in_range[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = [primes_in_range[i - 1], primes_in_range[i]]

    return closest_pair

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    left = 10
    right = 19
    print(closest_primes(left, right))  # Output: [11, 13]

    # Test Case 2
    left = 1
    right = 10
    print(closest_primes(left, right))  # Output: [2, 3]

    # Test Case 3
    left = 20
    right = 22
    print(closest_primes(left, right))  # Output: [-1, -1]

    # Test Case 4
    left = 100
    right = 120
    print(closest_primes(left, right))  # Output: [101, 103]

    # Test Case 5
    left = 1
    right = 2
    print(closest_primes(left, right))  # Output: [-1, -1]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The sieve of Eratosthenes runs in O(n log log n), where n is `right`.
   - Collecting primes in the range [left, right] takes O(right - left).
   - Finding the closest pair of primes takes O(k), where k is the number of primes in the range.
   - Overall time complexity: O(n log log n), dominated by the sieve.

2. Space Complexity:
   - The sieve uses O(n) space to store the boolean array `is_prime`.
   - The list `primes_in_range` uses O(k) space, where k is the number of primes in the range.
   - Overall space complexity: O(n).

Topic: Math, Prime Numbers, Sieve of Eratosthenes
"""