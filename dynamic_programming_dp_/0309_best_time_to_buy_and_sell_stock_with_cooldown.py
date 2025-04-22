"""
LeetCode Question #309: Best Time to Buy and Sell Stock with Cooldown

Problem Statement:
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
1. After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
2. You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000
"""

# Solution
def maxProfit(prices):
    """
    Function to calculate the maximum profit with cooldown.
    
    :param prices: List[int] - List of stock prices
    :return: int - Maximum profit
    """
    if not prices:
        return 0
    
    n = len(prices)
    # Initialize DP arrays
    hold = [0] * n  # Maximum profit when holding a stock
    sell = [0] * n  # Maximum profit when selling a stock
    cooldown = [0] * n  # Maximum profit during cooldown
    
    # Base cases
    hold[0] = -prices[0]  # If we buy on the first day
    sell[0] = 0           # Cannot sell on the first day
    cooldown[0] = 0       # No cooldown on the first day
    
    for i in range(1, n):
        hold[i] = max(hold[i - 1], cooldown[i - 1] - prices[i])  # Hold or buy
        sell[i] = hold[i - 1] + prices[i]  # Sell the stock
        cooldown[i] = max(cooldown[i - 1], sell[i - 1])  # Cooldown or stay in cooldown
    
    # The result is the maximum profit on the last day when not holding a stock
    return max(sell[-1], cooldown[-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [1, 2, 3, 0, 2]
    print(maxProfit(prices1))  # Output: 3

    # Test Case 2
    prices2 = [1]
    print(maxProfit(prices2))  # Output: 0

    # Test Case 3
    prices3 = [6, 1, 3, 2, 4, 7]
    print(maxProfit(prices3))  # Output: 6

    # Test Case 4
    prices4 = [1, 2, 3, 4, 5]
    print(maxProfit(prices4))  # Output: 4

    # Test Case 5
    prices5 = [5, 4, 3, 2, 1]
    print(maxProfit(prices5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `prices` array once, performing constant-time operations for each day.
- Therefore, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity:
- The algorithm uses three arrays (`hold`, `sell`, `cooldown`) of size n to store intermediate results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""