"""
LeetCode Question #2761: Prime Pairs With Target Sum

Problem Statement:
You are given an integer `n`. We say that two integers `x` and `y` form a prime pair if:
- 1 <= x <= y <= n
- x + y = n
- Both `x` and `y` are prime numbers.

Return a list of all prime pairs `[x, y]` (sorted in ascending order) that satisfy the conditions. The pairs should also be sorted in ascending order based on `x`.

Example 1:
Input: n = 10
Output: [[3, 7], [5, 5]]
Explanation: In this case, there are two prime pairs that satisfy the conditions:
- 3 + 7 = 10, and both 3 and 7 are prime.
- 5 + 5 = 10, and 5 is prime.

Example 2:
Input: n = 4
Output: []
Explanation: There are no prime pairs for this value of `n`.

Constraints:
- 1 <= n <= 10^6
"""

# Solution
from math import isqrt

def prime_pairs(n):
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    # Generate all primes up to n using the Sieve of Eratosthenes
    def sieve_of_eratosthenes(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, isqrt(limit) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return is_prime

    # Generate primes up to n
    primes = sieve_of_eratosthenes(n)
    result = []

    # Find all prime pairs
    for x in range(2, n // 2 + 1):
        if primes[x] and primes[n - x]:
            result.append([x, n - x])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 10
    print(f"Input: n = {n1}")
    print(f"Output: {prime_pairs(n1)}")  # Expected: [[3, 7], [5, 5]]

    # Test Case 2
    n2 = 4
    print(f"Input: n = {n2}")
    print(f"Output: {prime_pairs(n2)}")  # Expected: []

    # Test Case 3
    n3 = 26
    print(f"Input: n = {n3}")
    print(f"Output: {prime_pairs(n3)}")  # Expected: [[3, 23], [7, 19], [13, 13]]

    # Test Case 4
    n4 = 2
    print(f"Input: n = {n4}")
    print(f"Output: {prime_pairs(n4)}")  # Expected: []

"""
Time Complexity:
- The Sieve of Eratosthenes runs in O(n log log n) to generate all primes up to `n`.
- The loop to find prime pairs runs in O(n / 2) = O(n).
- Overall time complexity: O(n log log n).

Space Complexity:
- The Sieve of Eratosthenes uses O(n) space to store the boolean array for primes.
- The result list may take up to O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Arrays, Math, Prime Numbers
"""