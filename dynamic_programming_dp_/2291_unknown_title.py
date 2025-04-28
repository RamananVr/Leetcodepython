"""
LeetCode Problem #2291: Maximum Profit From Trading Stocks

Problem Statement:
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the i-th day, 
and an integer `k` representing the maximum number of transactions you are allowed to make.

A transaction is defined as buying and then selling one share of the stock. 
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Return the maximum profit you can achieve under the given constraints.

Example 1:
Input: prices = [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Example 2:
Input: prices = [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Constraints:
- 0 <= k <= 100
- 0 <= prices.length <= 1000
- 0 <= prices[i] <= 1000
"""

def maxProfit(k: int, prices: list[int]) -> int:
    if not prices or k == 0:
        return 0

    n = len(prices)
    # If k is greater than n // 2, it's equivalent to unlimited transactions
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    # DP table: dp[i][j] represents the max profit using at most i transactions up to day j
    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])

    return dp[k][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [3, 2, 6, 5, 0, 3]
    k1 = 2
    print(maxProfit(k1, prices1))  # Output: 7

    # Test Case 2
    prices2 = [2, 4, 1]
    k2 = 2
    print(maxProfit(k2, prices2))  # Output: 2

    # Test Case 3
    prices3 = [1, 2, 3, 4, 5]
    k3 = 2
    print(maxProfit(k3, prices3))  # Output: 4

    # Test Case 4
    prices4 = [7, 6, 4, 3, 1]
    k4 = 2
    print(maxProfit(k4, prices4))  # Output: 0

    # Test Case 5
    prices5 = []
    k5 = 2
    print(maxProfit(k5, prices5))  # Output: 0

"""
Time Complexity:
- If `n` is the length of the prices array and `k` is the maximum number of transactions:
  - The DP solution involves filling a table of size (k+1) x n.
  - For each transaction (k), we iterate through the prices array (n), resulting in O(k * n) time complexity.

Space Complexity:
- The space complexity is O(k * n) due to the DP table.

Topic: Dynamic Programming (DP)
"""