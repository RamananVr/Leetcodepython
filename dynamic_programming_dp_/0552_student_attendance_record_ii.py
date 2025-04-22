"""
LeetCode Question #552: Student Attendance Record II

Problem Statement:
Given an integer n, return the number of possible attendance records of length n that do not contain more than one 'A' (absent) or more than two continuous 'L' (late). The result may be large, so return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10^5

Example:
Input: n = 2
Output: 8
Explanation: There are 8 valid attendance records of length 2:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL".
Only "AA", "LLL" are invalid.

"""

# Solution
def checkRecord(n: int) -> int:
    MOD = 10**9 + 7

    # dp[i][A][L] represents the number of valid sequences of length i
    # where A is the count of 'A' and L is the count of trailing 'L's.
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 1  # Base case: 1 way to have an empty record

    for i in range(1, n + 1):
        for A in range(2):  # A can be 0 or 1
            for L in range(3):  # L can be 0, 1, or 2
                # Add 'P' (no change to A or trailing L)
                dp[i][A][0] += dp[i - 1][A][L]
                dp[i][A][0] %= MOD

                # Add 'A' (increment A, reset trailing L)
                if A < 1:
                    dp[i][A + 1][0] += dp[i - 1][A][L]
                    dp[i][A + 1][0] %= MOD

                # Add 'L' (increment trailing L, no change to A)
                if L < 2:
                    dp[i][A][L + 1] += dp[i - 1][A][L]
                    dp[i][A][L + 1] %= MOD

    # Sum up all valid sequences of length n
    result = 0
    for A in range(2):
        for L in range(3):
            result += dp[n][A][L]
            result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    print(checkRecord(n))  # Output: 8

    # Test Case 2
    n = 1
    print(checkRecord(n))  # Output: 3

    # Test Case 3
    n = 3
    print(checkRecord(n))  # Output: 19

    # Test Case 4
    n = 4
    print(checkRecord(n))  # Output: 43

    # Test Case 5
    n = 10
    print(checkRecord(n))  # Output: 3536

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through all lengths from 1 to n.
- For each length, it iterates through 2 possible values for A (0 or 1) and 3 possible values for L (0, 1, or 2).
- Thus, the time complexity is O(n * 2 * 3) = O(n).

Space Complexity:
- The dp array has dimensions (n + 1) x 2 x 3, which requires O(n * 2 * 3) = O(n) space.

Topic: Dynamic Programming (DP)
"""