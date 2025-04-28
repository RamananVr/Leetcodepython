"""
LeetCode Problem #2338: Count the Number of Ideal Arrays

Problem Statement:
You are given two integers `n` and `maxValue`. You want to construct an array `nums` of length `n` such that:
1. Every element in `nums` is a positive integer and does not exceed `maxValue`.
2. The absolute difference between any two adjacent elements in `nums` is at most 1.

Return the number of such arrays. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 2 <= n <= 10^4
- 1 <= maxValue <= 100
"""

# Solution
def idealArrays(n: int, maxValue: int) -> int:
    MOD = 10**9 + 7

    # Precompute binomial coefficients (nCr) using Pascal's Triangle
    def precompute_binomial_coefficients(n):
        binomial = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            binomial[i][0] = binomial[i][i] = 1
            for j in range(1, i):
                binomial[i][j] = (binomial[i - 1][j - 1] + binomial[i - 1][j]) % MOD
        return binomial

    # Precompute all divisors for numbers up to maxValue
    def precompute_divisors(maxValue):
        divisors = [[] for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            for j in range(i, maxValue + 1, i):
                divisors[j].append(i)
        return divisors

    # Precompute binomial coefficients and divisors
    binomial = precompute_binomial_coefficients(n)
    divisors = precompute_divisors(maxValue)

    # DP array to count the number of arrays ending with each value
    dp = [0] * (maxValue + 1)
    for i in range(1, maxValue + 1):
        dp[i] = 1

    result = 0
    for length in range(1, n + 1):
        if length == 1:
            result += maxValue
            continue

        new_dp = [0] * (maxValue + 1)
        for value in range(1, maxValue + 1):
            for divisor in divisors[value]:
                new_dp[value] += dp[divisor]
                new_dp[value] %= MOD

        dp = new_dp
        result += sum(dp) % MOD
        result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, maxValue1 = 2, 5
    print(idealArrays(n1, maxValue1))  # Expected Output: 10

    # Test Case 2
    n2, maxValue2 = 3, 3
    print(idealArrays(n2, maxValue2))  # Expected Output: 19

    # Test Case 3
    n3, maxValue3 = 4, 2
    print(idealArrays(n3, maxValue3))  # Expected Output: 8

"""
Time Complexity:
- Precomputing binomial coefficients: O(n^2)
- Precomputing divisors: O(maxValue * log(maxValue))
- Main DP loop: O(n * maxValue * d), where d is the average number of divisors for numbers up to maxValue.
  In the worst case, d is approximately log(maxValue), so the complexity is O(n * maxValue * log(maxValue)).

Space Complexity:
- Binomial coefficients: O(n^2)
- Divisors array: O(maxValue * log(maxValue))
- DP arrays: O(maxValue)
Overall: O(n^2 + maxValue * log(maxValue))

Topic: Dynamic Programming (DP), Combinatorics
"""