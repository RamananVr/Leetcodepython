"""
LeetCode Problem #1872: Stone Game VIII

Problem Statement:
Alice and Bob take turns playing a game, with Alice starting first.

You are given a list of integers `stones` where `stones[i]` represents the value of the i-th stone in a row of stones. The total score of the game is the sum of the values of all the stones chosen by the players. The game proceeds as follows:

1. Initially, there is a single pile containing all the stones.
2. On each player's turn, they must split one of the existing piles into two smaller piles. The player who splits the pile gets the sum of the values of the stones in the smaller pile with the smaller sum.
3. The game ends when there is no pile with more than one stone.

The goal of the game is to maximize the score difference between Alice and Bob. Return the maximum score difference that Alice can achieve if both players play optimally.

Constraints:
- `2 <= len(stones) <= 10^5`
- `-10^4 <= stones[i] <= 10^4`
"""

# Solution
def stoneGameVIII(stones):
    """
    This function calculates the maximum score difference Alice can achieve
    if both players play optimally.
    """
    n = len(stones)
    # Compute prefix sums
    prefix_sum = [0] * n
    prefix_sum[0] = stones[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i]

    # Initialize dp array
    dp = [0] * n
    dp[-1] = prefix_sum[-1]

    # Fill dp array from right to left
    for i in range(n - 2, 0, -1):
        dp[i] = max(dp[i + 1], prefix_sum[i] - dp[i + 1])

    return dp[1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [-1, 2, -3, 4, -5]
    print(stoneGameVIII(stones1))  # Expected Output: 5

    # Test Case 2
    stones2 = [7, -6, 5, 10, 5, -2, -6]
    print(stoneGameVIII(stones2))  # Expected Output: 13

    # Test Case 3
    stones3 = [1, 2, 3, 4, 5]
    print(stoneGameVIII(stones3))  # Expected Output: 15

"""
Time Complexity Analysis:
- Computing the prefix sum takes O(n) time.
- Filling the dp array also takes O(n) time.
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- The prefix_sum array takes O(n) space.
- The dp array also takes O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Dynamic Programming (DP)
"""