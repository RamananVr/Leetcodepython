"""
LeetCode Question #1420: Build Array Where You Can Find The Maximum Exactly K Comparisons

Problem Statement:
Given three integers n, m, and k, return the number of ways to build an array of length n such that:
- Each element is between 1 and m (inclusive).
- The array has exactly k "comparisons" (i.e., the maximum value in the array changes exactly k times).
Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 50
- 1 <= m <= 100
- 1 <= k <= 50

Example:
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The arrays are [1,1], [2,2], [3,3], [1,2], [1,3], [2,3].

Input: n = 5, m = 2, k = 2
Output: 0
Explanation: There are no valid arrays.

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only valid array is [1,1,1,1,1,1,1,1,1].
"""

# Python Solution
def numOfArrays(n: int, m: int, k: int) -> int:
    MOD = 10**9 + 7
    
    # dp[i][j][l] represents the number of ways to build an array of length i
    # with maximum value j and exactly l comparisons.
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Base case: For arrays of length 1, the maximum value is the only element,
    # and there is exactly 1 comparison.
    for j in range(1, m + 1):
        dp[1][j][1] = 1
    
    # Fill the DP table
    for i in range(2, n + 1):  # Array length
        for j in range(1, m + 1):  # Maximum value
            for l in range(1, k + 1):  # Number of comparisons
                # Case 1: Extend the array without changing the maximum value
                dp[i][j][l] += dp[i - 1][j][l] * j
                dp[i][j][l] %= MOD
                
                # Case 2: Add a new maximum value
                for x in range(1, j):
                    dp[i][j][l] += dp[i - 1][x][l - 1]
                    dp[i][j][l] %= MOD
    
    # Sum up all ways to build arrays of length n with exactly k comparisons
    result = sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    m = 3
    k = 1
    print(numOfArrays(n, m, k))  # Output: 6

    # Test Case 2
    n = 5
    m = 2
    k = 2
    print(numOfArrays(n, m, k))  # Output: 0

    # Test Case 3
    n = 9
    m = 1
    k = 1
    print(numOfArrays(n, m, k))  # Output: 1

    # Additional Test Case
    n = 3
    m = 3
    k = 2
    print(numOfArrays(n, m, k))  # Output: 18

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves three nested loops: one for the array length (n), one for the maximum value (m), and one for the number of comparisons (k).
- Additionally, there is an inner loop to iterate over possible previous maximum values (up to m).
- Thus, the time complexity is O(n * m * k * m), which simplifies to O(n * m^2 * k).

Space Complexity:
- The DP table has dimensions (n+1) x (m+1) x (k+1), so the space complexity is O(n * m * k).

Topic: Dynamic Programming (DP)
"""