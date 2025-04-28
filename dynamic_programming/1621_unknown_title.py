"""
LeetCode Problem #1621: Number of Sets of K Non-Overlapping Line Segments

Problem Statement:
Given an integer n and an integer k, return the number of ways to divide the points [0, 1, ..., n-1] into k non-overlapping line segments. 
A line segment is defined as a pair of points (i, j) where 0 <= i < j < n. Each point can only belong to one line segment at a time.

Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 2 <= n <= 1000
- 1 <= k <= n-1
"""

# Solution
def numberOfSets(n: int, k: int) -> int:
    MOD = 10**9 + 7
    
    # dp[i][j] represents the number of ways to form j line segments using the first i points
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 line segments can always be formed
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Option 1: Do not use the i-th point in the current segment
            dp[i][j] = dp[i - 1][j]
            
            # Option 2: Use the i-th point to extend a segment or start a new segment
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i][j] %= MOD
    
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 4, 2
    print(numberOfSets(n1, k1))  # Expected Output: 5

    # Test Case 2
    n2, k2 = 3, 1
    print(numberOfSets(n2, k2))  # Expected Output: 3

    # Test Case 3
    n3, k3 = 30, 7
    print(numberOfSets(n3, k3))  # Expected Output: 796297179

    # Test Case 4
    n4, k4 = 1000, 999
    print(numberOfSets(n4, k4))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves filling a DP table of size n x k.
- Each cell computation takes constant time.
- Therefore, the time complexity is O(n * k).

Space Complexity:
- The space complexity is O(n * k) due to the DP table.

Topic: Dynamic Programming
"""