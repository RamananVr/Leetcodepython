"""
LeetCode Question #629: K Inverse Pairs Array

Problem Statement:
Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be very large, return it modulo 10^9 + 7.

An array's inverse pair is a pair of indices (i, j) such that:
- 1 <= i < j <= n
- nums[i] > nums[j]

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] has 0 inverse pairs.

Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The arrays [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Constraints:
- 1 <= n <= 1000
- 0 <= k <= 1000
"""

# Python Solution
def kInversePairs(n: int, k: int) -> int:
    MOD = 10**9 + 7

    # dp[i][j] represents the number of arrays with i elements and j inverse pairs
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to arrange 0 elements with 0 inverse pairs

    for i in range(1, n + 1):
        for j in range(k + 1):
            # Add the number of ways to form arrays with i-1 elements and j inverse pairs
            dp[i][j] = dp[i - 1][j]
            # Subtract the number of ways that exceed the current range of inverse pairs
            if j - i >= 0:
                dp[i][j] -= dp[i - 1][j - i]
            # Ensure the value is within the modulo range
            dp[i][j] += dp[i][j - 1] if j > 0 else 0
            dp[i][j] %= MOD

    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 0
    print(f"Input: n = {n1}, k = {k1} -> Output: {kInversePairs(n1, k1)}")  # Expected: 1

    # Test Case 2
    n2, k2 = 3, 1
    print(f"Input: n = {n2}, k = {k2} -> Output: {kInversePairs(n2, k2)}")  # Expected: 2

    # Test Case 3
    n3, k3 = 4, 2
    print(f"Input: n = {n3}, k = {k3} -> Output: {kInversePairs(n3, k3)}")  # Expected: 5

    # Test Case 4
    n4, k4 = 10, 5
    print(f"Input: n = {n4}, k = {k4} -> Output: {kInversePairs(n4, k4)}")  # Expected: 2002

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution involves filling a DP table of size (n+1) x (k+1).
- Each cell computation takes O(1) time.
- Therefore, the overall time complexity is O(n * k).

Space Complexity:
- The space complexity is O(n * k) due to the DP table.

Topic: Dynamic Programming (DP)
"""