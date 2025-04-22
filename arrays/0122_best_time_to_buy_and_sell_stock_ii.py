"""
LeetCode Question #122: Best Time to Buy and Sell Stock II

Problem Statement:
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the i-th day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a profit since the prices are decreasing.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""

# Solution
def maxProfit(prices):
    """
    Calculate the maximum profit that can be achieved by buying and selling stocks.

    :param prices: List[int] - List of stock prices
    :return: int - Maximum profit
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices1))  # Output: 7

    # Test Case 2
    prices2 = [1, 2, 3, 4, 5]
    print(maxProfit(prices2))  # Output: 4

    # Test Case 3
    prices3 = [7, 6, 4, 3, 1]
    print(maxProfit(prices3))  # Output: 0

    # Test Case 4
    prices4 = [1, 2, 3, 1, 5, 6]
    print(maxProfit(prices4))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the `prices` array once, performing a constant amount of work for each element.
Thus, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity:
The algorithm uses a constant amount of extra space (only the `profit` variable).
Thus, the space complexity is O(1).
"""

# Topic: Arrays