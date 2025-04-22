"""
LeetCode Question #518: Coin Change II

Problem Statement:
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. 
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: There are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up just with coins of denomination 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000
"""

# Clean, Correct Python Solution
def change(amount: int, coins: list[int]) -> int:
    # Initialize a DP array where dp[i] represents the number of ways to make up amount i
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: There's one way to make amount 0 (use no coins)

    # Iterate over each coin
    for coin in coins:
        # Update the DP array for all amounts that can be formed using the current coin
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    amount1 = 5
    coins1 = [1, 2, 5]
    print(f"Test Case 1: {change(amount1, coins1)}")  # Expected Output: 4

    # Test Case 2
    amount2 = 3
    coins2 = [2]
    print(f"Test Case 2: {change(amount2, coins2)}")  # Expected Output: 0

    # Test Case 3
    amount3 = 10
    coins3 = [10]
    print(f"Test Case 3: {change(amount3, coins3)}")  # Expected Output: 1

    # Test Case 4
    amount4 = 0
    coins4 = [1, 2, 5]
    print(f"Test Case 4: {change(amount4, coins4)}")  # Expected Output: 1

    # Test Case 5
    amount5 = 7
    coins5 = [2, 3, 5]
    print(f"Test Case 5: {change(amount5, coins5)}")  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over each coin (O(n), where n is the number of coins).
- The inner loop iterates over all amounts from the coin's value to the target amount (O(amount)).
- Therefore, the overall time complexity is O(n * amount).

Space Complexity:
- The space complexity is O(amount) because we use a 1D DP array of size (amount + 1).
"""

# Topic: Dynamic Programming