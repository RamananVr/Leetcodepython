"""
LeetCode Problem #1735: Count Ways to Make Array With Product

Problem Statement:
You are given a 2D array `queries` where each `queries[i] = [n, k]`. For each query, you want to find the number of different arrays that consist of `n` positive integers and have a product equal to `k`. Since the answer may be too large, return it modulo 10^9 + 7.

Two arrays are considered different if there exists at least one index `i` such that the value at index `i` is different in the two arrays.

Example:
Input: queries = [[2, 6], [5, 1], [73, 660]]
Output: [4, 1, 50734910]

Constraints:
- 1 <= queries.length <= 10^4
- 1 <= n <= 75
- 1 <= k <= 10^9
"""

from math import comb
from collections import Counter

MOD = 10**9 + 7

def countWays(queries):
    def prime_factorization(x):
        """Returns the prime factorization of x as a Counter."""
        factors = Counter()
        d = 2
        while d * d <= x:
            while x % d == 0:
                factors[d] += 1
                x //= d
            d += 1
        if x > 1:
            factors[x] += 1
        return factors

    # Precompute factorials and modular inverses for combinations
    max_n = 75
    fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    def comb_mod(n, r):
        """Computes nCr % MOD."""
        if n < r or r < 0:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    results = []
    for n, k in queries:
        factors = prime_factorization(k)
        ways = 1
        for prime, count in factors.items():
            ways = ways * comb_mod(count + n - 1, n - 1) % MOD
        results.append(ways)
    return results

# Example Test Cases
if __name__ == "__main__":
    queries = [[2, 6], [5, 1], [73, 660]]
    print(countWays(queries))  # Output: [4, 1, 50734910]

"""
Time Complexity:
- Prime factorization: O(sqrt(k)) for each query, where k is the second element in the query.
- Combination calculation: O(1) per prime factor due to precomputed factorials.
- Total complexity: O(Q * sqrt(k)), where Q is the number of queries.

Space Complexity:
- O(max_n) for precomputed factorials and modular inverses.

Topic: Math, Combinatorics, Prime Factorization
"""