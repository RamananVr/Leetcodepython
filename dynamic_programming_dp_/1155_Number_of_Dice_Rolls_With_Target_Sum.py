"""
LeetCode Problem #1155: Number of Dice Rolls With Target Sum

Problem Statement:
You have `d` dice, and each die has `f` faces numbered from 1 to `f`.
Return the number of possible ways to roll the dice so the sum of the face-up numbers equals `target`.
Since the answer may be too large, return it modulo `10^9 + 7`.

Constraints:
- 1 <= d, f <= 30
- 1 <= target <= 1000
"""

# Solution
def numRollsToTarget(d: int, f: int, target: int) -> int:
    MOD = 10**9 + 7
    
    # dp[i][j] represents the number of ways to roll `i` dice to get a sum of `j`
    dp = [[0] * (target + 1) for _ in range(d + 1)]
    dp[0][0] = 1  # Base case: 0 dice to make sum 0 has exactly 1 way (do nothing)
    
    for i in range(1, d + 1):  # Iterate over dice
        for j in range(1, target + 1):  # Iterate over possible sums
            for k in range(1, f + 1):  # Iterate over face values
                if j >= k:  # Only consider valid sums
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    
    return dp[d][target]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    d1, f1, target1 = 1, 6, 3
    print(numRollsToTarget(d1, f1, target1))  # Expected Output: 1

    # Test Case 2
    d2, f2, target2 = 2, 6, 7
    print(numRollsToTarget(d2, f2, target2))  # Expected Output: 6

    # Test Case 3
    d3, f3, target3 = 2, 5, 10
    print(numRollsToTarget(d3, f3, target3))  # Expected Output: 1

    # Test Case 4
    d4, f4, target4 = 30, 30, 500
    print(numRollsToTarget(d4, f4, target4))  # Expected Output: Some large number modulo 10^9 + 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs `d` times (number of dice).
- The middle loop runs `target` times (possible sums).
- The innermost loop runs `f` times (faces of the dice).
Thus, the total time complexity is O(d * target * f).

Space Complexity:
- We use a 2D DP table of size (d + 1) x (target + 1).
Thus, the space complexity is O(d * target).

Topic: Dynamic Programming (DP)
"""