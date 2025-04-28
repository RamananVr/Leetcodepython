"""
LeetCode Problem #204: Count Primes

Problem Statement:
Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

A prime number is a number greater than 1 with only two divisors: 1 and itself.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
- 0 <= n <= 5 * 10^6
"""

def countPrimes(n: int) -> int:
    """
    Returns the number of prime numbers less than n using the Sieve of Eratosthenes algorithm.
    """
    if n <= 2:
        return 0

    # Create a boolean array to mark prime numbers
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Use the Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n, i):
                is_prime[j] = False

    # Count the number of primes
    return sum(is_prime)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 10
    print(f"Number of primes less than {n1}: {countPrimes(n1)}")  # Expected Output: 4

    # Test Case 2
    n2 = 0
    print(f"Number of primes less than {n2}: {countPrimes(n2)}")  # Expected Output: 0

    # Test Case 3
    n3 = 1
    print(f"Number of primes less than {n3}: {countPrimes(n3)}")  # Expected Output: 0

    # Test Case 4
    n4 = 100
    print(f"Number of primes less than {n4}: {countPrimes(n4)}")  # Expected Output: 25

    # Test Case 5
    n5 = 5000
    print(f"Number of primes less than {n5}: {countPrimes(n5)}")  # Expected Output: 669

"""
Time Complexity:
- The Sieve of Eratosthenes algorithm runs in O(n log log n) time. 
  This is because for each prime number `p`, we mark its multiples, and the number of operations is proportional to n / p.

Space Complexity:
- The space complexity is O(n) due to the boolean array `is_prime` used to mark prime numbers.

Topic: Math, Sieve of Eratosthenes
"""