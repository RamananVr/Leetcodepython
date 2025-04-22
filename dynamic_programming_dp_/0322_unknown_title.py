"""
LeetCode Problem #322: Coin Change

Problem Statement:
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. 
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

# Clean and Correct Python Solution
def coinChange(coins, amount):
    """
    Function to calculate the minimum number of coins needed to make up the given amount.

    :param coins: List[int] - List of coin denominations
    :param amount: int - Target amount
    :return: int - Minimum number of coins needed, or -1 if not possible
    """
    # Initialize a DP array with a large value (amount + 1 is effectively "infinity" here)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate over each coin and update the DP array
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[amount] is still "infinity", it means the amount cannot be formed
    return dp[amount] if dp[amount] != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(coinChange(coins1, amount1))  # Output: 3

    # Test Case 2
    coins2 = [2]
    amount2 = 3
    print(coinChange(coins2, amount2))  # Output: -1

    # Test Case 3
    coins3 = [1]
    amount3 = 0
    print(coinChange(coins3, amount3))  # Output: 0

    # Test Case 4
    coins4 = [186, 419, 83, 408]
    amount4 = 6249
    print(coinChange(coins4, amount4))  # Output: 20

    # Test Case 5
    coins5 = [1, 2, 5]
    amount5 = 100
    print(coinChange(coins5, amount5))  # Output: 20

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity is O(n * m), where:
  - n is the amount (size of the DP array)
  - m is the number of coins (length of the coins array)
- For each coin, we iterate through the DP array from `coin` to `amount`.

Space Complexity:
- The space complexity is O(n), where n is the amount. This is due to the DP array of size `amount + 1`.

Overall, the solution is efficient for the given constraints.
"""

# Topic: Dynamic Programming (DP)