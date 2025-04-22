"""
LeetCode Problem #714: Best Time to Buy and Sell Stock with Transaction Fee

Problem Statement:
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying on day 0 (price = 1) and selling on day 3 (price = 8), profit = 8 - 1 - 2 = 5.
- Buying on day 4 (price = 4) and selling on day 5 (price = 9), profit = 9 - 4 - 2 = 3.
Total profit = 5 + 3 = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
- 1 <= prices.length <= 5 * 10^4
- 1 <= prices[i] < 5 * 10^4
- 0 <= fee < 5 * 10^4
"""

# Solution
def maxProfit(prices, fee):
    """
    Calculate the maximum profit with transaction fee.

    :param prices: List[int] - List of stock prices
    :param fee: int - Transaction fee
    :return: int - Maximum profit
    """
    n = len(prices)
    if n == 0:
        return 0

    # Initialize variables to track the maximum profit
    cash = 0  # Maximum profit if we don't hold a stock
    hold = -prices[0]  # Maximum profit if we hold a stock

    for price in prices[1:]:
        # Update cash and hold for the current day
        cash = max(cash, hold + price - fee)  # Sell the stock
        hold = max(hold, cash - price)  # Buy the stock

    return cash

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [1, 3, 2, 8, 4, 9]
    fee1 = 2
    print("Test Case 1 Output:", maxProfit(prices1, fee1))  # Expected Output: 8

    # Test Case 2
    prices2 = [1, 3, 7, 5, 10, 3]
    fee2 = 3
    print("Test Case 2 Output:", maxProfit(prices2, fee2))  # Expected Output: 6

    # Test Case 3
    prices3 = [1, 2, 3, 4, 5]
    fee3 = 1
    print("Test Case 3 Output:", maxProfit(prices3, fee3))  # Expected Output: 3

    # Test Case 4
    prices4 = [5, 4, 3, 2, 1]
    fee4 = 1
    print("Test Case 4 Output:", maxProfit(prices4, fee4))  # Expected Output: 0

    # Test Case 5
    prices5 = [1]
    fee5 = 1
    print("Test Case 5 Output:", maxProfit(prices5, fee5))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- O(n), where n is the length of the prices array. We iterate through the prices array once.

Space Complexity:
- O(1), as we use only two variables (cash and hold) to store the state of the solution.
"""

# Topic: Dynamic Programming