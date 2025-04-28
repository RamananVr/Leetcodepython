"""
LeetCode Question #2318: Number of Distinct Roll Sequences

Problem Statement:
You are given an integer n representing the number of dice rolls. Each die has six faces numbered from 1 to 6. 
The following conditions must be satisfied for a sequence to be valid:
1. No two consecutive rolls can have the same value.
2. If the value of the roll `i` is x, then the value of roll `i+1` cannot be x ± 1.

Return the number of distinct sequences possible modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10^4
"""

# Python Solution
def distinctSequences(n: int) -> int:
    MOD = 10**9 + 7

    # Edge case: If n == 1, all 6 rolls are valid
    if n == 1:
        return 6

    # DP table: dp[i][j][k] represents the number of valid sequences of length i
    # where the last roll is j and the second last roll is k.
    dp = [[[0] * 7 for _ in range(7)] for _ in range(n + 1)]

    # Base case: For sequences of length 1, initialize valid rolls
    for j in range(1, 7):
        dp[1][j][0] = 1

    # Fill the DP table
    for i in range(2, n + 1):
        for j in range(1, 7):  # Current roll
            for k in range(1, 7):  # Previous roll
                if j != k and abs(j - k) > 1:  # Valid transition
                    for m in range(7):  # Second last roll
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][k][m]) % MOD

    # Sum up all valid sequences of length n
    result = 0
    for j in range(1, 7):
        for k in range(1, 7):
            result = (result + dp[n][j][k]) % MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small input
    n = 2
    print(distinctSequences(n))  # Expected output: 30

    # Test Case 2: Larger input
    n = 3
    print(distinctSequences(n))  # Expected output: 150

    # Test Case 3: Edge case with n = 1
    n = 1
    print(distinctSequences(n))  # Expected output: 6

    # Test Case 4: Large input
    n = 10
    print(distinctSequences(n))  # Expected output: A large number modulo 10^9 + 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DP table has dimensions (n x 7 x 7), and for each cell, we iterate over 7 possible values for the second last roll.
- Thus, the time complexity is O(n * 7 * 7 * 7) = O(n).

Space Complexity:
- The DP table requires O(n * 7 * 7) space.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""