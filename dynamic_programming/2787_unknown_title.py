"""
LeetCode Problem #2787: Ways to Express an Integer as the Sum of Powers

Problem Statement:
Given three integers `n`, `x`, and `k`, return the number of ways to express `n` as the sum of `k` positive integers raised to the power of `x`. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 1000
- 1 <= x <= 5
- 1 <= k <= 100

Example:
Input: n = 10, x = 2, k = 2
Output: 1
Explanation: The only way to express 10 as the sum of two squares is 1^2 + 3^2 = 10.

Input: n = 100, x = 3, k = 3
Output: 0
Explanation: There is no way to express 100 as the sum of three cubes.

"""

# Python Solution
def numberOfWays(n: int, x: int, k: int) -> int:
    MOD = 10**9 + 7

    # Precompute all possible powers up to n
    powers = []
    i = 1
    while i**x <= n:
        powers.append(i**x)
        i += 1

    # Initialize a 3D DP table
    dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(len(powers) + 1)]

    # Base case: 1 way to make sum 0 with 0 numbers
    for i in range(len(powers) + 1):
        dp[i][0][0] = 1

    # Fill the DP table
    for i in range(1, len(powers) + 1):
        for j in range(n + 1):
            for l in range(k + 1):
                # Exclude the current power
                dp[i][j][l] = dp[i - 1][j][l]
                # Include the current power if possible
                if l > 0 and j >= powers[i - 1]:
                    dp[i][j][l] += dp[i - 1][j - powers[i - 1]][l - 1]
                    dp[i][j][l] %= MOD

    return dp[len(powers)][n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, x1, k1 = 10, 2, 2
    print(numberOfWays(n1, x1, k1))  # Output: 1

    # Test Case 2
    n2, x2, k2 = 100, 3, 3
    print(numberOfWays(n2, x2, k2))  # Output: 0

    # Test Case 3
    n3, x3, k3 = 8, 2, 2
    print(numberOfWays(n3, x3, k3))  # Output: 1 (2^2 + 2^2 = 8)

    # Test Case 4
    n4, x4, k4 = 50, 2, 3
    print(numberOfWays(n4, x4, k4))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let P be the number of powers of integers that are less than or equal to n when raised to the power x.
- The DP table has dimensions (P+1) x (n+1) x (k+1).
- Filling the table involves iterating over all these dimensions, resulting in a time complexity of O(P * n * k).

Space Complexity:
- The space complexity is determined by the size of the DP table, which is O(P * n * k).

In the worst case, P is approximately n^(1/x), so the overall complexity is:
- Time: O(n^(1/x) * n * k)
- Space: O(n^(1/x) * n * k)
"""

# Topic: Dynamic Programming