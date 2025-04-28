"""
LeetCode Problem #1269: Number of Ways to Stay in the Same Place After Some Steps

Problem Statement:
You have a pointer at index 0 in an array of size `arrLen`. At each step, you can move 1 position to the left, 
1 position to the right, or stay in the same place (the pointer should not go beyond the boundaries of the array). 
Given two integers `steps` and `arrLen`, return the number of ways to stay at index 0 after exactly `steps` steps. 
Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= steps <= 500
- 1 <= arrLen <= 10^6

"""

# Solution
def numWays(steps: int, arrLen: int) -> int:
    MOD = 10**9 + 7
    max_pos = min(steps, arrLen - 1)  # The farthest position we can reach
    
    # dp[i][j]: Number of ways to be at position j after i steps
    dp = [[0] * (max_pos + 1) for _ in range(steps + 1)]
    dp[0][0] = 1  # Base case: 1 way to be at position 0 with 0 steps
    
    for i in range(1, steps + 1):
        for j in range(max_pos + 1):
            dp[i][j] = dp[i - 1][j]  # Stay in the same place
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # Move left
            if j < max_pos:
                dp[i][j] += dp[i - 1][j + 1]  # Move right
            dp[i][j] %= MOD  # Take modulo to prevent overflow
    
    return dp[steps][0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    steps = 3
    arrLen = 2
    print(numWays(steps, arrLen))  # Expected Output: 4

    # Test Case 2
    steps = 2
    arrLen = 4
    print(numWays(steps, arrLen))  # Expected Output: 2

    # Test Case 3
    steps = 4
    arrLen = 2
    print(numWays(steps, arrLen))  # Expected Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs for `steps` iterations.
- The inner loop runs for `min(steps, arrLen)` iterations.
- Therefore, the time complexity is O(steps * min(steps, arrLen)).

Space Complexity:
- We use a 2D DP array of size `steps x min(steps, arrLen)`.
- Therefore, the space complexity is O(steps * min(steps, arrLen)).

Topic: Dynamic Programming (DP)
"""